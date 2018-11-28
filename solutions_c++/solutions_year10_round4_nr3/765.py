#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<stack>
#define MAX 110
#include<memory.h>
using namespace std;

int val[MAX][MAX];
int dp[MAX][MAX];
int main()
{
	int C;
	int R;
	int i,j;
	int x1,y1,x2,y2;
	int z=0;
	int n=0;
	int p;
	scanf("%d",&C);
	while(C--)
	{
		memset(val,0,sizeof(val));
		scanf("%d",&R);
		for(p=0;p<R;p++)
		{
			scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
			for(i=x1;i<=x2;i++)
			{
				for(j=y1;j<=y2;j++)
				{
					val[i][j]=1;
					n=max(x2,n);
					n=max(y2,n);
				}
			}
		}
		int c=0;
		while(1)
		{
			/*for(i=1;i<=n;i++)
			{
				for(j=1;j<=n;j++)
				{
					printf("%d",val[i][j]);
				}
				printf("\n");
			}*/
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=n;j++)
				{
					if(val[i][j])
						break;
				}
				if(j!=n+1)
					break;
			}
			if(i==n+1)
				break;
			for(i=1;i<=n;i++)
			{
				for(j=1;j<=n;j++)
				{
					if(val[i][j]&&val[i-1][j]+val[i][j-1]==0)
						dp[i][j]=0;
					else if(!val[i][j]&&val[i-1][j]+val[i][j-1]==2)
						dp[i][j]=1;
					else
						dp[i][j]=val[i][j];
				}
			}
			memcpy(val,dp,sizeof(val));
			c++;
		}
		label:
		printf("Case #%d: %d\n",++z,c);
	}
	return 0;
}
