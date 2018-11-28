#pragma warning(disable: 4786)
#include<stdio.h>
#include<string>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<map>
#include<iostream>
#include<set>
#include<math.h>
#include<queue>
using namespace std;
		


int dp[110][110],dp1[110][110];


void show()
{
	int i,j;
	for(i=1;i<=40;i++)
	{
		for(j=1;j<=40;j++)
		{
			printf("%d",dp[i][j]);
		}
		printf("\n");
	}
}
int main()	
{			
	freopen("C-small-attempt3.in","r",stdin);
	freopen("C-small-attempt3.out","w",stdout);
	
	//freopen("in.txt","r",stdin);
	int T,cs,m,n,i,j,len,r,x1,x2,y1,y2,ans,chek;
	scanf("%d",&T);
	
	for(cs=1;cs<=T;cs++)
	{

		scanf("%d",&r);
		memset(dp,0,sizeof(dp));
		memset(dp1,0,sizeof(dp1));

		while(r--)
		{
			scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
			if(x1>x2)
				swap(x1,x2);
			if(y1>y2)
				swap(y1,y2);
			for(i=y1;i<=y2;i++)
				for(j=x1;j<=x2;j++)
				{
					dp[i][j]=1;
				}
		}
		ans=0;
		chek=1;
		while(chek)
		{
			ans++;
			chek=0;
			for(i=1;i<110;i++)
			{
				for(j=1;j<110;j++)
				{
					if(dp[i][j]==0)
					{
						if(dp[i-1][j] && dp[i][j-1])
						{
							chek=1;
							dp1[i][j]=1;	
						}
						else
							dp1[i][j]=0;

					}
					if(dp[i][j]==1)
					{
						if(dp[i-1][j]==0 && dp[i][j-1]==0)
							dp1[i][j]=0;
						else
						{
							dp1[i][j]=1;
							chek=1;
						}
						

					}
				}
				
			}
			for(i=1;i<=100;i++)
				for(j=1;j<=100;j++)
					dp[i][j]=dp1[i][j];
			//show();
			//printf("\n");
			//cout<<ans;
		}
		
		printf("Case #%d: %d\n",cs,ans);
	}
  	return 0;
}			