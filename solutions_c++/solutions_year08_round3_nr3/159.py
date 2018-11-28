#include <stdio.h>
#include <string.h>

#define M 1024

int a[M];
int s[M];
int d[M][M];

int main()
{
	int N,n,m;
	int i,j,k,l,t;
	__int64 x,y,z;

	scanf("%d",&N);
	for(k=1;k<=N;k++)
	{
		scanf("%d%d%I64d%I64d%I64d",&n,&m,&x,&y,&z);
		for(i=0;i<m;i++)
		{
			scanf("%d",a+i);
		}
		for(i=0;i<n;i++)
		{
			 s[i]=a[i%m];
			 a[i%m]=(x*a[i%m]+y*(i+1))%z;
		}

		memset(d,0,sizeof(d));
		for(i=0;i<n;i++)
		{
			d[i][i]=1;
		}
		for(l=2;l<=n;l++)
		{
			for(i=0;i<=n-l;i++)
			{
				j=i+l-1;
				d[i][j]=1;
				for(t=i;t<j;t++)
				{
					if(s[j]>s[t])
						d[i][j]=(d[i][j]+d[i][t])%1000000007;
				}
			}
		}

		t=0;
		for(i=0;i<n;i++)
		{
			t=(t+d[0][i])%1000000007;
		}

		printf("Case #%d: %d\n",k,t);
	}

	return 0;
}