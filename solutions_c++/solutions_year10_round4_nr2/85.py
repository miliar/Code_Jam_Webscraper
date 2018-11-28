#include <stdio.h>
#define N 1100
#define L 15
#define M 1000000000
int m[N], c[2*N], d[2*N][L];
int main()
{
	int i, j, k, n, p, t, ts;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d", &p), n=1<<p, i=0; i<n; scanf("%d", &m[i]), i++);
		for(j=n/2, i=0; i<p; j/=2, i++)
			for(k=0; k<j; scanf("%d", &c[j+k]), k++);
		for(i=0; i<n; i++)
			for(j=0; j<L; j++)
				if(p-j>m[i]) d[n+i][j]=M;
				else d[n+i][j]=0;
		for(i=n-1; i; i--)
			for(j=0; j<L; j++)
			{
				d[i][j]=M;
				if(j<L-1 && d[2*i][j+1]!=M && d[2*i+1][j+1]!=M && d[2*i][j+1]+d[2*i+1][j+1]+c[i]<d[i][j]) d[i][j]=d[2*i][j+1]+d[2*i+1][j+1]+c[i];
				if(d[2*i][j]!=M && d[2*i+1][j]!=M && d[2*i][j]+d[2*i+1][j]<d[i][j]) d[i][j]=d[2*i][j]+d[2*i+1][j];
			}
			printf("Case #%d: %d\n", t+1, d[1][0]);
	}
	return 0;
}