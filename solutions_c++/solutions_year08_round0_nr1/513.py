#include<iostream>
#include<map>
#include<vector>
#include<string>
using namespace std;
map<string,int>map_k;
vector<int> v;
int dp[1023][105];
int main()
{
//	freopen("A-large.in","r",stdin);
//	freopen("A-large.out","w",stdout);
	char s[200];
	int cas,i,j,k,n,m,test=0;
	string str;
	scanf("%d",&cas);
	while(cas--)
	{
		v.clear();
		map_k.clear();
		scanf("%d",&n);
		gets(s);
		for(i=0;i<n;i++)
		{
			gets(s);
			str=string(s);
			map_k[s]=i;
		}
		scanf("%d",&m);
		gets(s);
		for(i=0;i<m;i++)
		{
			gets(s);
			str=string(s);
			v.push_back(map_k[str]);
		}
		for(i=0;i<n;i++)
		{
			dp[i][0]=0;
		}
		for(i=1;i<=v.size();i++)
		for(j=0;j<n;j++)
		dp[i][j]=1000000000;
		for(i=0;i<v.size();i++)
		{
			for(j=0;j<n;j++)
			{
				for(k=0;k<n;k++)
				{
					if(k==v[i]) continue;
					if(k==j)
					{
					 	dp[i+1][k]<?=dp[i][j];
					}
					else
					{
						dp[i+1][k]<?=dp[i][j]+1;
					}
				}
			
			}
		}
		int ans=INT_MAX;
		for(j=0;j<n;j++)
		{
			if(ans>dp[v.size()][j]) ans=dp[v.size()][j];
		}
		if(ans==INT_MAX) ans=0;
		printf("Case #%d: %d\n",++test,ans);
	}
	return 0;
}