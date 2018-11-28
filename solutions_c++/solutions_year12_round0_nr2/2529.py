#include <cstdio>
using namespace std;

#define MAXN 105
int i, t, n, s, p, T, res;
int pct[MAXN], a[MAXN], b[MAXN], c[MAXN];

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out","w", stdout);
	
	scanf("%d", &T);
	
	for(t = 1; t <= T; t++) {
		scanf("%d %d %d", &n, &s, &p); 
		for(i = 0; i < n; i++)
			scanf("%d", &pct[i]);
		
		res = 0;
		
		// make them non-surprising
		for(i = 0; i < n; i++) {
			a[i] = b[i] = c[i] = pct[i] / 3;
			if(pct[i] % 3 >= 1) c[i]++;
			if(pct[i] % 3 >= 2) b[i]++;
		}
		
		// turn into surprising those who can become over p
		for(i = 0; i < n; i++)
			if(pct[i] > 1 && pct[i] < 29 && b[i] == c[i] && c[i] == p - 1 && s > 0) {
				s--;
				res++;
			}
			else if(c[i] >= p) res++;
		
		printf("Case #%d: %d\n", t, res);
	}
	
	return 0;
}
