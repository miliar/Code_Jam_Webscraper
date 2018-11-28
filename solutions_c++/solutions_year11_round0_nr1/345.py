#include<iostream>
#include<stdio.h>
#include<string>
#include<string.h>
#include<vector>
#include<algorithm>

using namespace std;
int dp[110][110];
int tim[110],pos[110],id[110];
char s[10];

const int inf = 100000000;
void solve(int i,int j,int k)
{
	for(int t=1;t<=100;t++)
	{
		if(abs(t-j)<=k)
			dp[i][t]=1;
	}
}
int main()
{
	int t,n,i,j,k;
	int cas=1;
	freopen("A-large.in","r",stdin);
	freopen("temp.txt","w",stdout);
	cin>>t;
	while(t--)
	{
		memset(dp,0,sizeof(dp));
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			cin>>s>>pos[i];
			if(s[0]=='O')
				id[i]=0;
			else id[i]=1;
		}
		tim[0]=pos[0];
		for(i=1;i<=100;i++)
			if(i-1<=pos[0])
				dp[0][i]=1;
		for(i=1;i<n;i++)
		{
			if(id[i-1]==id[i])
			{
				tim[i]=tim[i-1]+abs(pos[i]-pos[i-1])+1;
				for(j=1;j<=100;j++)
					if(dp[i-1][j])
						solve(i,j,abs(pos[i]-pos[i-1])+1);
			}
			else
			{
				int temp=inf;
				for(j=1;j<=100;j++)
					if(dp[i-1][j])
						temp = min(temp,abs(pos[i]-j));
				//cout<<temp<<endl;
				temp++;
				tim[i]=tim[i-1]+temp;
				solve(i,pos[i-1],temp);	
			}
		}
		printf("Case #%d: %d\n",cas++,tim[n-1]);
	}
}