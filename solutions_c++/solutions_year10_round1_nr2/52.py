#include <stdio.h>
#define N 110
#define K 257
#define M 1000000000
int d[N][K], m[N], a, b, c;
int ab(int x) { return x<0?-x:x; }
int mn(int x, int y) { return x<y?x:y; }
int get(int d) { return !c?(d>0)*M:(d+!d-1)/c*b; }
int main()
{
	int i, j, k, t, n, ts;
	for(i=0; i<K-1; d[0][i]=M, i++);
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d%d%d", &a, &b, &c, &n), i=1; i<=n; scanf("%d", &m[i]), i++);
		for(i=1; i<=n; d[i][K-1]=d[i-1][K-1]+a, i++)
			for(j=0; j<K-1; j++)
				for(d[i][j]=mn(d[i-1][j]+a, d[i-1][K-1]+ab(m[i]-j)), k=0; k<K-1; d[i][j]=mn(d[i][j], d[i-1][k]+ab(m[i]-j)+get(ab(j-k))), k++);
		for(k=M, j=0; j<K; k=mn(k, d[n][j]), j++);
		printf("Case #%d: %d\n", t+1, k);
	}
	return 0;
}