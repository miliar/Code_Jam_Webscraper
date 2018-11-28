#include <cstdio>

int opos, ot, bpos, bt;
int T, N;
char opt[2], tar;

inline int abs(int a) {return a<0 ? -a : a;}
inline int max(int a, int b) {return a>b ? a : b ;}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &T);
	for(int c=1; c<=T; c++) {
		opos = bpos = 1;
		ot = bt = 0;
		scanf("%d", &N);
		while(N--) {
			scanf("%s%d", opt, &tar);
			if(opt[0] == 'O') {
				ot += abs(tar-opos)+1;
				opos = tar;
				ot = max(ot, bt+1);
			} else if(opt[0] == 'B') {
				bt += abs(tar-bpos)+1;
				bpos = tar;
				bt = max(ot+1, bt);
			}
//			printf(">> %d %d <<\n", ot, bt);
		}
		printf("Case #%d: %d\n", c, max(ot, bt));
	}
}
