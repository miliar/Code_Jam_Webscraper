/*
X X+1 X+2
A B   C

(3A)	(2A1B)	(1A2B)
3X		3X+1	3X+2 -- not surprising

(2A 1C) (1A 1B 1C)	(1A 2C)
3X+2	3X+3		3X+4	 -- surprising
		3(X+1)		3(X+1)+1 -- not surprising

Range: 3X to 3X+4

Remainders:
	Not  [Best]	Sur  [Best]		
0 - 3X   [X]	3X+3 [X+2]
1 - 3X+1 [X+1]	3X+4 [X+2]
2 - 3X+2 [X+1]	3X+2 [X+2]

X+2 <= 10
1 <= X

29[10+9+10], 30[10+10+10] -- confirmed non-surprising
0[0+0+0], 1 [0+0+1] -- confirmed non-surprising
-----------
if best of not surprising is already >= p -- answer++ and continue
elseif total = 3,4,29,30
elseif best of not surprising == p-1 -- answer++, surprising--
*/
#include <cstdio>
using namespace std;

int main() {
	int t,tc,i,curr, r, best, ans;
	int S, N, p;
	scanf("%d", &tc);
	for(t=0;t<tc;t++) {
		ans = 0;
		scanf("%d %d %d", &N, &S, &p);
		for(i=0;i<N;i++) {
			scanf("%d", &curr);
			r = curr % 3;
			best = ((r == 0) ? (curr/3) : (curr/3+1));
//			fprintf(stderr, "%d N %d\n", curr, best);
			if(best >= p) ans++;
			else if ( curr == 0 || curr == 1 || curr == 29 || curr == 30) continue;
			else if ( S > 0 ) {
				best = ((r==2) ? (curr/3+2) : (curr/3+1));
				if(best == p) ans++, S--;
//				fprintf(stderr, "%d N %d\n", curr, best);
			}
		}
		printf("Case #%d: %d\n", t+1, ans);
	}
	return 0;
}
