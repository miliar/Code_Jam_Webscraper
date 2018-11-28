#include <stdio.h>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

struct Command {
	int r, p;
	Command(){}
	Command(int rr, int pp) : r(rr), p(pp) {}
};

int main(void) {
	int T; scanf("%d", &T);
	for(int tc=1; tc<=T; tc++) {
		int res = 0;
		int N; scanf("%d", &N);
		
		vector<int> next;
		vector<Command> cmd;
		for(int i=0;i<N;i++) {
			char t[2];
			int r, p; scanf("%s %d", t, &p);
			r = t[0];

			cmd.push_back( Command(r, p) );
		}
		
		int pos[333]; fill(pos, pos+333, 1);
		int reserve=0;
		int prev_r = 0;
		for(int i=0;i<N;i++) {
			if(prev_r != cmd[i].r) {
				int diff = abs(cmd[i].p - pos[cmd[i].r]);
				res += max(0, diff-reserve)+1;
				reserve = max(0, diff-reserve)+1;
			}
			else {
				int diff = abs(cmd[i].p - pos[cmd[i].r]);
				res += diff+1;
				reserve += diff+1;
			}
			pos[cmd[i].r] = cmd[i].p;
			prev_r = cmd[i].r;
		}

		printf("Case #%d: %d\n", tc, res);
	}
	return 0;
}
