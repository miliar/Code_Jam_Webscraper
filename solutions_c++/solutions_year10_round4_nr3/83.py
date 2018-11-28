#include <stdio.h>
#define N 310
int u[N][N], v[N][N];
int main()
{
	int i, j, t, ts, f, q, i1, i2, j1, j2;
	for(scanf("%d", &ts), t=0; t<ts; t++)
	{
		for(i=0; i<N; i++)
			for(j=0; j<N; u[i][j]=0, j++);
		for(scanf("%d", &q); q; q--)
			for(scanf("%d%d%d%d", &i1, &j1, &i2, &j2), i=i1; i<=i2; i++)
				for(j=j1; j<=j2; u[i][j]=1, j++);
		for(q=0; ; q++)
		{
			f=0;
			for(i=0; i<N; i++)
				for(j=0; j<N; j++)
					if(u[i][j]) f=1;
			if(f==0) break;
			for(i=0; i<N; i++)
				for(j=0; j<N; j++)
					if(i>0 && j>0 && u[i-1][j] && u[i][j-1]) v[i][j]=1;
					else if(u[i][j] && ((i>0 && u[i-1][j]) || (j>0 && u[i][j-1]))) v[i][j]=1;
					else v[i][j]=0;
			for(i=0; i<N; i++)
				for(j=0; j<N; u[i][j]=v[i][j], j++);
		}
		printf("Case #%d: %d\n", t+1, q);
	}
	return 0;
}