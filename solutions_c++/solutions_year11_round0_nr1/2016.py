#include <cstdio>
#include <iostream>
using namespace std;

int T, N;
int next[2][105];
int ts[2][105];
int op, bp;

int main() {
	cin>>T;
	for(int z = 1; z <= T; z++) {
		cin>>N;
		op = bp = 0;
		char rob[2], but[5];
		for(int i = 0; i < N; i++) {
			scanf("%s%s", rob, but);
			if(rob[0] == 'O') {
				next[0][op] = atoi(but);
				ts[0][op++] = i;
			}
			else {
				next[1][bp] = atoi(but);
				ts[1][bp++] = i;
			}
		}
		int op2 = 0, bp2 = 0;
		int ans = 0;
		int ocp = 1, bcp = 1;
		while(op2 < op || bp2 < bp) {
			if(bp2 == bp || (op2 != op && ts[0][op2] < ts[1][bp2])) {
				int extra = abs(ocp-next[0][op2]) + 1;
				ans += extra;
				ocp = next[0][op2];
				op2++;
				if(abs(bcp-next[1][bp2]) <= extra)
					bcp = next[1][bp2];
				else if(bcp > next[1][bp2])
					bcp -= extra;
				else
					bcp += extra;
			}
			else {
				int extra = abs(bcp-next[1][bp2]) + 1;
				ans += extra;
				bcp = next[1][bp2];
				bp2++;
				if(abs(ocp-next[0][op2]) <= extra)
					ocp = next[0][op2];
				else if(ocp > next[0][op2])
					ocp -= extra;
				else
					ocp += extra;
			}
		}
		cout << "Case #" << z << ": " << ans << endl;
	}
	return 0;
}
