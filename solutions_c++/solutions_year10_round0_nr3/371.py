#include <stdio.h>
#define N 1010
#define L 30
int m[N];
__int64 d[L][N], p[L][N], a;
int main()
{
	int i, j, n, k, r, t, ts, h;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d%d", &r, &k, &n), i=0; i<n; scanf("%d", &m[i]), i++);
		for(i=0; i<n; d[0][i]=h, p[0][i]=(i+j)%n, i++)
			for(h=0, j=0; j<n && h+m[(i+j)%n]<=k; h+=m[(i+j)%n], j++);
		for(j=1; j<L; j++)
			for(i=0; i<n; d[j][i]=d[j-1][i]+d[j-1][p[j-1][i]], p[j][i]=p[j-1][p[j-1][i]], i++);
		for(i=0, j=0, a=0; r; r/=2, j++)
			if(r&1) { a+=d[j][i]; i=p[j][i]; }
		printf("Case #%d: %I64d\n", t+1, a);
	}
	return 0;
}