#include <stdio.h>
#define N 510
char m[N][N];
int d[N][N], u[N][N];
int get(int i1, int i2, int j1, int j2) { return d[i2+1][j2+1]-d[i2+1][j1]-d[i1][j2+1]+d[i1][j1]; }
int main()
{
	int i, j, k, r, c, t, ts;
	long long s;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d%d", &r, &c, &k), i=0; i<r; scanf("%s", m[i]), i++);
		for(i=0; i<r; i++)
			for(j=0; j<c; m[i][j]-='0', d[i+1][j+1]=d[i+1][j]+d[i][j+1]-d[i][j]+m[i][j], j++);
		for(k=r<c?r:c; k>=3; k--)
		{
			for(i=0; i+k<=r; i++)
				for(j=0; j+k<=c; u[i][j]=0, j++);
			for(i=0; i+k<=r; i++)
			{
				for(s=0, j=0; j<k; s+=(k-1-2*j)*get(i, i+k-1, j, j), j++);
				for(; j<=c; j++)
				{
					if(s-(m[i][j-k]+m[i+k-1][j-k]-m[i][j-1]-m[i+k-1][j-1])*(k-1)==0) u[i][j-k]++;
					s-=(k-1)*get(i, i+k-1, j-k, j-k);
					s+=2*get(i, i+k-1, j-k+1, j-1);
					s+=(1-k)*get(i, i+k-1, j, j);
				}
			}
			for(j=0; j+k<=c; j++)
			{
				for(s=0, i=0; i<k; s+=(k-1-2*i)*get(i, i, j, j+k-1), i++);
				for(; i<=r; i++)
				{
					if(s-(m[i-k][j]+m[i-k][j+k-1]-m[i-1][j]-m[i-1][j+k-1])*(k-1)==0) u[i-k][j]++;
					s-=(k-1)*get(i-k, i-k, j, j+k-1);
					s+=2*get(i-k+1, i-1, j, j+k-1);
					s+=(1-k)*get(i, i, j, j+k-1);
				}
			}
			for(i=0; i+k<=r; i++)
			{
				for(j=0; j+k<=c; j++)
					if(u[i][j]==2) break;
				if(j+k<=c) break;
			}
			if(i+k<=r) break;
		}
		if(k>=3) printf("Case #%d: %d\n", t+1, k);
		else printf("Case #%d: IMPOSSIBLE\n", t+1);
	}
	return 0;
}