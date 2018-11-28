#include <vector>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define MOD 1000003 
#define INF 1000000000
typedef long long  ll;
typedef unsigned long long  ull;
typedef pair<int,int> pii;

vector <int> adj[1024];
bool mark[1024];
vector <int> topol;
int indeg[1024];

void dfs(int u)
{
	mark[u] = true;
	for(int i = 0; i < adj[u].size(); i ++)
	{
		int v = adj[u][i];
		if(mark[v] == false)
			dfs(v);
	}	
	topol.push_back(u);
}

bool found;
void dfs2(int u)
{
	mark[u] = true;
	for(int i = 0; i < adj[u].size(); i ++)
	{
		int v = adj[u][i];
		if(mark[v] == false)
		{
			dfs2(v);
		}
		else
			found = true;
	}
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, n, k;
	
	cin >> t;
	for(int cas = 1; cas <= t; cas ++)
	{
		cin >> n;
		
		for(int i = 1; i <= n; i ++)
			adj[i].clear();
			
		// memset(indeg, 0, sizeof indeg);
		for(int i = 1; i <= n; i ++)
		{
			cin >> k;
			for(int j = 0; j < k; j ++)
			{
				int next;
				cin >> next;
				adj[i].push_back(next);
				// indeg[next] ++;
			}
		}
		
		topol.clear();
		memset(mark, 0, sizeof mark);
		for(int i = 1; i <= n; i ++)
			if(mark[i] == false)
				dfs(i);
		reverse(topol.begin(), topol.end());
		
		found = false;
		memset(mark, 0, sizeof mark);
		for(int i = 0; i < topol.size(); i ++)
		{
			int u = topol[i];
			if(mark[u] == false)
			{
				memset(mark, 0, sizeof mark);
				dfs2(u);
			}
		}
		cout << "Case #" << cas << ": " << (found == true ? "Yes" : "No") << endl;
	}
	
	return 0;
}














