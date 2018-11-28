#include<cstdio>
#include<algorithm>
#include<string>
#include<cstring>
#include<vector>
#include<queue>
#include<iostream>
#include<sstream>
#include<functional>
#include<map>
#include<set>

using namespace std;

typedef long long int64;
typedef pair<int,int> pint;

#define MAXN 12
int dp[MAXN][1<<MAXN];
int m, n;
char box[MAXN][MAXN];

int exist(int mask, int ind)
{
	return mask & (1<<ind);
}
int bound(int ind)
{
	return ind>=0 && ind<n;
}
void ass(int& mask, int ind)
{
	if(bound(ind))
		mask |= (1<<ind);
}
int dfs(int ind, int mask);
int dfs2(int indN, int cur, int next, int indM)
{
	if(indN == n)
	{
		return dfs(indM-1, next);
	}

	int ret = dfs2(indN+1, cur, next, indM);
	
	if(!exist(cur, indN))
	{
		ass(next, indN-1);
		ass(next, indN+1);
		ass(cur, indN+1);
		ret= max(ret, 1+dfs2(indN+1, cur, next, indM));
	}
	return ret;
}
int dfs(int ind, int mask)
{
	if(ind<0)
		return 0;

	int & ret=dp[ind][mask];
	if(ret>=0)
		return ret;
	
	for(int i=0; i<n; ++i)
	{
		if(box[ind][i]=='x')
			ass(mask, i);
	}
	return ret=dfs2(0, mask, 0, ind); 
}
/*
int solve()
{
	int all=1<<n;
	for(int i=m-1; i>=0; i--)
		for(int j=0; j<all; j++)
		{
			int valid=1;
			int next=0;
			for(int k=0; k<n; k++)
			{
				if(exist(j,k))
				{
					if(box[i][j]=='x' 
						|| bound(k+1) && exist(j,k+1)
						|| bound(k-1) && exist(j,k-1))
					{
						valid=0;
						break;
					}
					else
					{
						
					}
				}
			}	
			if(valid)
			{
				dp[i][j]=cnt(mask);
				if(i>0)
					dp[i][j]+=dp[i-1][next];
			}
			else
				dp[i][j]=0;
		}
}*/
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	
	int numCase;
	scanf("%d", &numCase);
	for(int c=1; c<=numCase; c++)
	{
		memset(dp,-1,sizeof(dp));
		scanf("%d%d", &m, &n);

		for(int i=0; i<m; i++)
			scanf("%s", box[i]);
		
		int res=dfs(m-1,0);
		printf("Case #%d: ", c);
		printf("%d\n", res);
	}
	return 0;
}