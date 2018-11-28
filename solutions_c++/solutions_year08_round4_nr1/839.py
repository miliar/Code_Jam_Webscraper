#include <stdio.h>
#define MAXN 10100

int Left(int n)
{
	return 2*n;
}
int Right(int n)
{
	return 2*n+1;
}
int Fmin(int a,int b)
{
	return a<b?a:b;
}
int main()
{
	int aCase,i,j,n,value,a[MAXN][2],b[MAXN][2];
	scanf("%d",&aCase);
	for(int tt=1;tt<=aCase;tt++)
	{
		scanf("%d%d",&n,&value);
	//	printf("n=%d value=%d\n",n,value);
		for(i=1;i<=(n-1)/2;i++)
			scanf("%d%d",&a[i][0],&a[i][1]);
	//	printf("i=%d,n=%d\n",i,n);
		for(i=(n+1)/2;i<=n;i++)
		{
			scanf("%d",&a[i][0]);
			b[i][a[i][0]]=0;
			if(a[i][0]==0)
				b[i][1]=0x1ffffff;
			else 
				b[i][0]=0x1ffffff;
		}
		for(i=(n-1)/2;i>=1;i--)
		{
			int l=Left(i);
			int r=Right(i);
			int min[2];
			min[0]=min[1]=0x1ffffff;
			if(a[i][1]==0)
			{
				if(a[i][0]==1)
				{
					if(min[1]>b[l][1]+b[r][1])
						min[1]=b[l][1]+b[r][1];
					if(min[0]>Fmin(b[l][0],b[r][0]))
						min[0]=Fmin(b[l][0],b[r][0]);
				}
				else 
				{
					if(min[1]>Fmin(b[l][1],b[r][1]))
						min[1]=Fmin(b[l][1],b[r][1]);
					if(min[0]>b[l][0]+b[r][0])
						min[0]=b[l][0]+b[r][0];
				}
			}
			else if(a[i][1]==1)
			{
				if(a[i][0]==1)
				{
					if(min[1]>b[l][1]+b[r][1])
						min[1]=b[l][1]+b[r][1];
					if(min[1]>Fmin(b[l][1],b[r][1])+1)
						min[1]=Fmin(b[l][1],b[r][1])+1;
					if(min[0]>Fmin(b[l][0],b[r][0]))
						min[0]=Fmin(b[l][0],b[r][0]);
				}
				else
				{
					if(min[1]>Fmin(b[l][1],b[r][1]))
						min[1]=Fmin(b[l][1],b[r][1]);
					if(min[0]>b[l][0]+b[r][0])
						min[0]=b[l][0]+b[r][0];
					if(min[0]>Fmin(b[l][0],b[r][0])+1)
						min[0]=Fmin(b[l][0],b[r][0])+1;
				}
			}
			b[i][0]=min[0];
			b[i][1]=min[1];
		}
		printf("Case #%d: ",tt);
		if(b[1][value]<0x1ffffff)
			printf("%d\n",b[1][value]);
		else 
			printf("IMPOSSIBLE\n");
	}
	return 0;
}
