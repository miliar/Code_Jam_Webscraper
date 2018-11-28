#include <stdio.h>
#include <memory.h>
#define MN 1000
int R, k, N;
int g[MN], w[MN];
long long r, c[MN];
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T, t, p, i, s, j;
	long long S;

	scanf("%d",&T);
	for (t = 1; t <= T; t++) {
		printf("Case #%d: ",t);
		scanf("%d%d%d",&R,&k,&N);
		S = 0;
		for (i = 0; i < N; i++) {
			scanf("%d",&g[i]);
			S += g[i];
		}
		memset(w,0,sizeof(w));
		r = 0; p = 0;
		c[p] = 0; w[p] = 0;
		for (i = 1; i <= R; i++) {
			s = 0;
			for (;;) {
				if (s == S || s+g[p]>k) break;
				s += g[p]; p = p+1<N?p+1:0;
			}
			r += s;
			if (w[p]) {
				r += (r-c[p])*((R-i)/(i-w[p]));
				for (j = 0; j < N; j++) {
					if (w[j] == w[p]+(R-i)%(i-w[p]))
						r += c[j]-c[p];
				}
				break;
			}
			c[p] = r; w[p] = i;
		}
		printf("%lld\n",r);
	}
	return 0;
}