#include <stdio.h>
#define N 16
int d[1<<N], m[N][30], a[N][N];
int main()
{
	int i, j, k, t, ts, l, h, n;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d%d", &n, &k), i=0; i<n; i++)
			for(j=0; j<k; scanf("%d", &m[i][j]), j++);
		for(i=0; i<n; i++)
			for(j=0; j<n; j++)
				if(i==j) a[i][i]=1;
				else
					for(a[i][j]=1, h=m[i][0]<m[j][0]?1:-1, l=0; l<k; l++)
						if(h*(m[i][l]-m[j][l])>=0) a[i][j]=0;
		for(i=1; i<(1<<n); i++)
		{
			for(k=0, j=0; j<n; k+=(i>>j)&1, j++);
			if(k==1) { d[i]=1; continue; }
			for(d[i]=1, j=0; j<n; j++)
				if((i>>j)&1)
					for(k=0; k<n; k++)
						if(((i>>k)&1) && !a[j][k]) d[i]=0;
			if(d[i]==1) continue;
			for(d[i]=0, j=i; j; j--, j&=i)
			{
				if(!d[j] || !d[i^j]) continue;
				l=d[j]+d[i^j];
				if(!d[i] || l<d[i]) d[i]=l;
			}
		}
		printf("Case #%d: %d\n", t+1, d[(1<<n)-1]);
	}
	return 0;
}