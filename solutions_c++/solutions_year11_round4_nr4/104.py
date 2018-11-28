#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
using namespace std;
typedef unsigned long long LLU;
typedef long long LL;
typedef pair<int,int> pii;
#define MP make_pair
const int INF=99999999;
const double PI=3.1415926535897932384626;
const double EPS=1E-11;

vector<int> adj[410];
bool adjm[410][410];
int dp[410][410];
int level[410];
vector<int> levels[410];
bool vis[410];
int calc(int a,int b)
{
//	printf("vis %d %d\n",a,b);
	if(dp[a][b]!=-1)
		return dp[a][b];
	int lev=level[b];
	int best=-INF;
	for(int i=0;i<adj[b].size();i++)
	{
		int c=adj[b][i];
		if(level[c]==lev+1)
		{
			if(c==1)
			{
				best=0;
				break;
			}
			else
			{
				int n=0;
				for(int j=0;j<levels[lev].size();j++)
				{
					int d=levels[lev][j];
					if(!adjm[d][a] && !adjm[d][b] && adjm[d][c])
						n++;
				}
				for(int j=0;j<levels[lev+1].size();j++)
				{
					int d=levels[lev+1][j];
					if(!adjm[d][b] && adjm[d][c])
						n++;
				}
				for(int j=0;j<levels[lev+2].size();j++)
				{
					int d=levels[lev+2][j];
					if(adjm[d][c])
						n++;
				}
				best=max(best,n+calc(b,c)-1);
			}
		}
	}
//	printf("calc %d %d: %d\n",a,b,best);
	dp[a][b]=best;
	return best;
}
int main()
{
	freopen("test.in","r",stdin); freopen("test.out","w",stdout);
	int testn;
	scanf("%d",&testn);
	for(int tn=1;tn<=testn;tn++)
	{
		for(int i=0;i<410;i++)
		{
			adj[i].clear();
			levels[i].clear();
		}
		memset(dp,-1,sizeof(dp));
		memset(level,0,sizeof(level));
		memset(adjm,0,sizeof(adjm));
		memset(vis,0,sizeof(vis));
		
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<m;i++)
		{
			int a,b;
			scanf("%d,%d",&a,&b);
			adjm[a][b]=true;
			adjm[b][a]=true;
			adj[a].push_back(b);
			adj[b].push_back(a);
		}
		levels[0].push_back(0);
		vis[0]=true;
		
		int endlev;
		for(int i=0;i<410;i++)
		{
			if(levels[i].size())
			{
//				printf("level %d\n",i);
				for(int j=0;j<levels[i].size();j++)
				{
					int a=levels[i][j];
//					printf("%d\n",a);
					if(a==1)
						endlev=i;
					for(int k=0;k<adj[a].size();k++)
					{
						int b=adj[a][k];
						if(!vis[b])
						{
							vis[b]=true;
							levels[i+1].push_back(b);
							level[b]=i+1;
						}
					}
				}
			}
		}
		
		
		int t=0;
		for(int j=0;j<levels[1].size();j++)
		{
			int d=levels[1][j];
			if(adjm[0][d])
				t++;
		}
		if(endlev==1)
			printf("Case #%d: %d %d\n",tn,0,t);
		else
		{
			int ans=calc(0,0)-1;
			printf("Case #%d: %d %d\n",tn,endlev-1,ans+t);
		}
	}
}
