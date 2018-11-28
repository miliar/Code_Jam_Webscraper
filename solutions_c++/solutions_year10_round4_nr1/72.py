#include <stdio.h>
#define N 210
int m[N][N];
int main()
{
	int ts, t, i, j, k, n, r, c;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(scanf("%d", &n), i=0; i<2*n-1; i++)
			if(i<n)
			{
				for(j=0; j<2*n-1; j++)
					if(j>=n-1-i && j<=n-1+i && (j+n-1+i)%2==0) scanf("%d", &m[i][j]);
					else m[i][j]=-1;
			}
			else
			{
				for(j=0; j<2*n-1; j++)
					if(j>=n-1-(2*n-2-i) && j<=n-1+(2*n-2-i) && (j+n-1+i)%2==0) scanf("%d", &m[i][j]);
					else m[i][j]=-1;
			}
		for(r=2*n-1, i=0; i<2*n-1; i++)
		{
			for(k=1; i-k>=0 && i+k<2*n-1; k++)
			{
				for(j=0; j<2*n-1; j++)
					if(m[i-k][j]!=-1 && m[i+k][j]!=-1 && m[i-k][j]!=m[i+k][j]) break;
				if(j<2*n-1) break;
			}
			if(i-k<0 || i+k>=2*n-1)
			{
				if(i>2*n-2-i) r=i<r?i:r;
				else r=2*n-2-i<r?2*n-2-i:r;
			}
		}
		for(c=2*n-1, j=0; j<2*n-1; j++)
		{
			for(k=1; j-k>=0 && j+k<2*n-1; k++)
			{
				for(i=0; i<2*n-1; i++)
					if(m[i][j-k]!=-1 && m[i][j+k]!=-1 && m[i][j-k]!=m[i][j+k]) break;
				if(i<2*n-1) break;
			}
			if(j-k<0 || j+k>=2*n-1)
			{
				if(j>2*n-2-j) c=j<c?j:c;
				else c=2*n-2-j<c?2*n-2-j:c;
			}
		}
		printf("Case #%d: %d\n", t+1, (n+r-n+1+c-n+1)*(n+r-n+1+c-n+1)-n*n);
	}
	return 0;
}