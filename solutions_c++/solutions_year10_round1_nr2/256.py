#include <stdio.h>

#define ABS(x) (((x)<0)?(-(x)):(x))
#define MAX(a,b) (((a)<(b))?(b):(a))
#define SEPP ((M)?((MAX(0,ABS(k-j)-1)/M)*I):((j==k)?(0):(1000000000)))

int t, D, I, M, N, a[100], b[100][256];

int main()
{
	scanf(" %d", &t);
	for(int cs=1; cs<=t; cs++)
	{
		scanf(" %d %d %d %d", &D, &I, &M, &N);
		for(int i=0; i<N; i++)
			scanf(" %d", &a[i]);
		for(int i=0; i<N; i++)
			for(int j=0; j<256; j++)
			{
				int v=D;
				if (i) v+=b[i-1][j];
				if (i)
					for(int k=0; k<256; k++)
					{
						if (b[i-1][k]+SEPP+ABS(a[i]-j)<v)
							v=b[i-1][k]+SEPP+ABS(a[i]-j);
					}
				else
					for(int k=0; k<256; k++)
					{
						if (ABS(a[i]-j)<v)
							v=ABS(a[i]-j);
					}
				b[i][j]=v;
			}
		int res=1000000000;
#if 0
		for(int j=5; j>=0; j--)
		{
			for(int i=0; i<N; i++)
				printf("%5d", b[i][j]);
			printf("\n");
		}
#endif
		for(int i=0; i<256; i++)
			if (b[N-1][i]<res) res=b[N-1][i];
		printf("Case #%d: %d\n", cs, res);
	}
	return 0;
}
