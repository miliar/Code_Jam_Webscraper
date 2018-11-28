#include <cstdio>
#include <cmath>
#include <algorithm>
#define MAXL 4
using namespace std;
int main() {
	int cas, cs = 1;
	scanf("%d", &cas);
	while(cas--) {
		int n, opos = 1, bpos = 1, ot = 0, bt = 0, pos, t;
		char rob[MAXL];
		scanf("%d", &n);
		for(int i = 0; i < n; ++i) {
			scanf("%s%d", rob, &pos);
			if(rob[0] == 'O') {
				t = ot + abs(pos - opos);
				ot = max(t, bt) + 1;
				opos = pos;
			}
			else {
				t = bt + abs(pos - bpos);
				bt = max(t, ot) + 1;
				bpos = pos;
			}
		}
		printf("Case #%d: %d\n", cs, max(ot, bt));
		++cs;
	}
	return 0;
}
