#include <cstdio>
#include <deque>
#include <cstring>
#include <utility>
#include <algorithm>

using namespace std;

int main(){
	freopen("input", "r", stdin);
	int cases;
	scanf("%d\n", &cases);
	deque<pair<char, int> > q;
	for(int i = 0; i < cases; i++) {
		int num; scanf("%d\n", &num);
		int o_pos = 1, b_pos = 1, time = 0;
		for(int j = 0; j < num; j++) {
			char t; scanf("%c ", &t);
			int x; scanf("%d ", &x);
			q.push_back(make_pair(t, x));
		}
		while(q.size()) {
			pair<char, int> top = q.front();
			q.pop_front();
			bool b = top.first == 'B';
			int j;
            for (j = 0; j < q.size(); j++) if(q[j].first == (b?'O':'B')) break;
			int move_distance = abs((b?b_pos:o_pos) - top.second);
			time += move_distance + 1;
			(b?b_pos : o_pos) = top.second;
			if (j != q.size()) {
				bool forward = (b?o_pos:b_pos) < q[j].second;
				(b?o_pos:b_pos) += (forward?1:-1)*min(abs((b?o_pos:b_pos) - q[j].second), move_distance+1);
			}
		}
		printf("Case #%d: %d\n", i+1, time);
	}
	return 0;
}





