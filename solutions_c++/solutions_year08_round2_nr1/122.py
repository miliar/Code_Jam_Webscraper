#include<iostream>
#include<vector>
using namespace std;
long long dp[3][3];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	long long n,A,B,C,D,X,Y,m,i,j,k,x1,x2,x3,y1,y2,y3;
	int cas,test=1;
	scanf("%d",&cas);
	while(cas--)
	{
		cin>>n>>A>>B>>C>>D>>X>>Y>>m;
		memset(dp,0,sizeof(dp));
		for(i=0;i<n;i++)
		{
		//	v.push_back(MM(X,Y));	
			dp[X%3][Y%3]++;
			X=(A*X+B)%m;
  			Y=(C*Y+D)%m;
		}
		long long sum=0;
		for(x1=0;x1<3;x1++)
		for(x2=0;x2<3;x2++)
		for(x3=0;x3<3;x3++)
		for(y1=0;y1<3;y1++)
		for(y2=0;y2<3;y2++)
		for(y3=0;y3<3;y3++)
		if((x1+x2+x3)%3==0&&(y1+y2+y3)%3==0)
		{
			if(x1==x2&&x2==x3&&y1==y2&&y2==y3)
			{
				long long temp=dp[x1][y1]*(dp[x2][y2]-1)*(dp[x3][y3]-2);
				if(temp<0) temp=0;
				sum+=temp;
			}
			else if(x1==x2&&y1==y2)
			{
				long long temp=dp[x1][y1]*(dp[x2][y2]-1)*(dp[x3][y3]);
				if(temp<0) temp=0;
				sum+=temp;
				
			}
			else if(x2==x3&&y2==y3)
			{
				long long temp=dp[x1][y1]*(dp[x2][y2])*(dp[x3][y3]-1);
				if(temp<0) temp=0;
				sum+=temp;	
			}
			else if(x1==x3&&y1==y3)
			{
				long long temp=dp[x1][y1]*(dp[x2][y2])*(dp[x3][y3]-1);
				if(temp<0) temp=0;
				sum+=temp;	
			}
			else
			{
				long long temp=dp[x1][y1]*(dp[x2][y2])*(dp[x3][y3]);
				if(temp<0) temp=0;
				sum+=temp;	
			}
		}
		
		printf("Case #%d: ",test++);
		cout<<sum/6<<endl;
	}
	return 0;
}