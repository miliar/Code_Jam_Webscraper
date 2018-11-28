#include<stdio.h>
#include<stdlib.h>
int map[802][802];
int main()
{
	freopen("a-large.in","r",stdin);
	freopen("a-large.out","w",stdout);
	int tt,t;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n*4;i++)
			for(int j=0;j<n*4;j++)
				map[i][j]=-1;
		for(int i=0;i<n;i++)
			for(int j=n-1-i;j<=n-1+i;j+=2)
				scanf("%d",&map[i][j]);
		for(int i=0;i<n-1;i++)
			for(int j=i+1;j<=2*n-i-3;j+=2)
				scanf("%d",&map[n+i][j]);
		int y=n-1;
		int x=n-1;
		int ans=10000;
		for(int i=0;i<2*n-1;i++)
		{
			for(int j=0;j<2*n-1;j++)
			{
				int gg=0;
				if(n+abs(y-i)+abs(x-j)>=ans) continue;
				
				int k;
				for(k=0;k<2*n-1;k++)
				{
					int l;
					int l2=j+1;
					for(l=j-1;l>=0;l--,l2++)
					{
						if(map[k][l]==-1 || map[k][l2]==-1) continue;
						if(map[k][l]!=map[k][l2]) break;
					}
					if(l>=0) break;
				}
				if(k<2*n-1) gg=1;
				
				for(k=0;k<2*n-1;k++)
				{
					int l;
					int l2=i+1;
					for(l=i-1;l>=0;l--,l2++)
					{
						if(map[l][k]==-1 || map[l2][k]==-1) continue;
						if(map[l][k]!=map[l2][k]) break;
					}
					if(l>=0) break;
				}
				if(k<2*n-1) gg=2;
				

//				printf("%d %d :: %d\n",i,j,gg);
				if(gg==0)
				{
					ans=n+abs(y-i)+abs(x-j);
//					printf("!!%d %d\n",i,j);
				}
			}
		}
		printf("Case #%d: ",t);
		printf("%d\n",ans*ans-n*n);
	}
	return 0;
}
