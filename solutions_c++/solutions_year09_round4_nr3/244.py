#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <algorithm>
using namespace std;


const int maxn = 301;
const int maxm = 301;
//init
int N,M,match[maxm];
vector<int> g[maxn];
//end of init
int mk[maxm];
int dfs(int v)
{
	int i,t,u;
	for (i = g[v].size()-1 ; i >= 0 ; i--)
	{
		if (mk[u=g[v][i]]) continue;
		mk[u]=1;
		t = match[u];
		match[u] = v;
		if (t == -1 || dfs(t)) return 1;
		match[u] = t;
	}
	return 0;
}
int Match()
{
	int i,ans=0;
	for (i = 0 ; i < N ; i++)
	{
		memset(mk,0,sizeof mk);
		if (dfs(i)) ans++;
	}
	return ans;
}


int n,k,sn;
vector<int> sts[110],st[110];
char gg[110][110];
int cros(vector<int>& a, vector<int>& b)
{
	int i;
	if(a[0]==b[0]) return 0;
	else if(a[0]<b[0])
	{
		for (i = 1 ; i < k ; i++)
			if(a[i]>=b[i]) return 0;
		return 1;
	}
	else
	{
		for (i = 1 ; i < k ; i++)
			if(a[i]<=b[i]) return 0;
		return -1;
	}
}
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,ca,i,j,t,ans;
	scanf("%d",&T);
	for (ca = 1 ; ca <= T ; ca++)
	{
		scanf("%d%d",&n,&k);
		for (i = 0 ; i < n ; i++)
		{
			sts[i].clear();
			for (j = 0 ; j < k ; j++)
			{
				scanf("%d",&t);
				sts[i].push_back(t);
			}
		}
		for (i = 0 ; i < n ; i++)
		{
			for (j = 0 ; j < n ; j++)
				gg[i][j]=(cros(sts[i],sts[j])==1);
		}
		N = M = n;
		for (i = 0 ; i < N ; i++) g[i].clear();
		memset(match,-1,sizeof match);
		for (i = 0 ; i < n ; i++)
		{
			for (j = 0 ; j < n ; j++)if(i!=j&& gg[i][j])
				g[i].push_back(j);
		}
/*
		for (i = 0 ; i < n ; i++)
		{
			for (j = 0 ; j < n ; j++)
				cout<<(g[i][j]?'1':'0')<<' ';
			cout<<endl;
		}cout<<endl;*/
		
		printf("Case #%d: %d\n",ca,n-Match());
	}

	return 0;
}
