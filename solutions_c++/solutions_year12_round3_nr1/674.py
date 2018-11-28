#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <cassert>
using namespace std;

/*========================================Templates=============================================*/
#define REP(i,n)			for(int i=0;i<(n);++i)
#define FOR(i,a,b)		for(int i=(a);i<=(b);++i)
#define FOREACH(i,c)		for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define ALL(x)			(x).begin(),(x).end()
#define S(n)				scanf("%d",&n)
#define DB(x)			cout<<#x<<" : "<<x<<endl;

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int UINT;
/*==============================================================================================*/

vector<int> adj[1007],back[1007];
bool vis[1007];

bool dfs(int idx)
{
	if ( vis[idx] )
		return true;
	
	vis[idx] = true;
	for (int i = 0; i < adj[idx].size(); i += 1)
	{
		if ( dfs(adj[idx][i]) )
			return true;
	}
	return false;
}


int main()
{
	int tc;
	cin>>tc;
	for (int cas = 1; cas <= tc; cas += 1)
	{
		int N;
		cin >> N;
		vector<int> root;
		
		for (int i = 1; i <= N; i += 1)
		{
			adj[i].clear();
			back[i].clear();			
		}
		
		for (int i = 1; i <= N; i += 1)
		{
			int n,x;
						
			cin >> n;
			for (int j = 0; j < n; j += 1)
			{
				cin >> x;
				adj[i].push_back(x);
				back[x].push_back(i);
			}
		}
		
		for (int i = 1; i <=N ; i += 1)
		{
			if (back[i].size()==0)
				root.push_back(i);
		}
		
		bool flag = false;
		for (int i = 0; i < root.size() && !flag; i += 1)
		{
			memset(vis,0,sizeof vis);
			if ( dfs(root[i]) )
				flag = true;
		}
		
		if (flag)
			printf("Case #%d: Yes\n",cas);
		else
			printf("Case #%d: No\n",cas);
	}
}








