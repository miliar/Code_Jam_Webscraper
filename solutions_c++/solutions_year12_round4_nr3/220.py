#include <cstdio>
#include <cstring>
#include <algorithm>
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define CLR(a,x) memset(a, x, sizeof(a))
#define EXP(i,l) for (int i=(l); i; i=qn[i])
#define LLD long long
using namespace std;

int n, tc, t;
int p[2005];
LLD h[2005];


int main(){
	scanf("%*d");
	while (scanf("%d", &n) != EOF){
		FOR(i,0,n-1) scanf("%d", &p[i]), p[i]--;
		p[n-1] = n-1;
		printf("Case #%d:", ++tc);

		// check invalid
		int ok = 1;
		FOR(i,0,n-1)
		FOR(j,0,i)
		if (p[j] > i && p[j] < p[i]) ok = 0;
		if (!ok){
			printf(" Impossible\n");
			continue;
		}
		
		CLR(h, -1);
		h[n-1] = 1000000000;
		FOR(i,0,n-1)
		if (p[i] == n-1) h[i] = 999999999;
		
		FOR(i,0,n){
			FOR(j,0,n)
			if (h[j] == -1 && h[p[j]] != -1){
				int x = p[j], y = p[p[j]];
				if (tc == 7 || tc==29)
				h[j] = h[x] - ((LLD)(h[y] - h[x]) * (LLD)(x - j) + y - x - 1)/ (LLD)(y - x) - 1;
				else
				h[j] = h[x] - ((LLD)(h[y] - h[x]) * (LLD)(x - j) + y - x - 1)/ (LLD)(y - x) - n;
			}
		}

		// checker
		FOR(i,0,n){
			int x = p[i];
			FOR(j,i+1,n){
				LLD C = (LLD)(j - i) * (h[x] - h[i]) - (LLD)(x - i) * (h[j] - h[i]);
				
				if (C < 0) printf("WA %d %d %lld\n", i, j, C);
				if (C == 0 && j < x) printf("WA %d %d %lld\n", i, j, C);
			}
		}

		FOR(i,0,n) printf(" %lld", h[i]);
		puts("");
	}
	return 0;
}
