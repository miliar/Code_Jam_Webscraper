#include <cstdio>
using namespace std;

#define REP(a, b) for(int a = 0; a < (b); a++)

int t, n, s, p, a, res, c;

int main() {
	scanf("%d", &t);
	while(t--) {
		c++;
		scanf("%d%d%d", &n, &s, &p);
		res = 0;
		REP(i, n) {
			scanf("%d", &a);
			if((a/3+((a%3)>0))>=p)
				res++;
			else if(s>0) {
				if(a>0 && a%3==0 && (a/3+1)>=p) {
					res++;
					s--;
				}
				else if(a%3==2 && (a/3+2)>=p) {
					res++;
					s--;
				}
			}
		}
		printf("Case #%d: %d\n", c, res);
	}
	return 0;
}
