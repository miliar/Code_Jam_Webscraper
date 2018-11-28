#include <iostream>
#include <sstream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi;
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 

#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)
#define watcharr(i, x) TRACE(cout << #x" = "); rep(i, sz(x)) cout << x[i] << " "; cout << endl

#define INF 1000000

typedef struct Node {
	bool leaf;
	bool change;
	int t;
} node;

vector<node> nodes;

int V;

int dp[10010][2];

int solve(int nd, int v) 
{
	int &ret = dp[nd][v];
	
	if(ret != -1) return ret;
	
	ret = INF;
	
	if(nodes[nd].leaf)  {
		if(nodes[nd].t != v)
			return ret = INF;
		else
			return ret = 0;
	}	
	
	int x1, x2;
	
	if(v == 1) {
		if(nodes[nd].t == 1) {
			x1 = solve( (nd + 1) * 2 - 1, 1);
			x2 = solve( (nd + 1) * 2, 1);
			
			ret = min(ret, x1 + x2);
			
			if(nodes[nd].change) {
				x1 = solve( (nd + 1) * 2 - 1, 0);
				x2 = solve( (nd + 1) * 2, 1);
				
				ret = min(ret, 1 + x1 + x2);
				
				x1 = solve( (nd + 1) * 2 - 1, 1);
				x2 = solve( (nd + 1) * 2, 0);
				
				ret = min(ret, 1 + x1 + x2);
			}
		}
		else {
			x1 = solve( (nd + 1) * 2 - 1, 0);
			x2 = solve( (nd + 1) * 2, 1);
			
			ret = min(ret, x1 + x2);
			
			x1 = solve( (nd + 1) * 2 - 1, 1);
			x2 = solve( (nd + 1) * 2, 0);
			
			ret = min(ret, x1 + x2);
			
			x1 = solve( (nd + 1) * 2 - 1, 1);
			x2 = solve( (nd + 1) * 2, 1);
			
			ret = min(ret, x1 + x2);			
		}
	}
	else {
		if(nodes[nd].t == 1) {
			x1 = solve( (nd + 1) * 2 - 1, 0);
			x2 = solve( (nd + 1) * 2, 0);
			
			ret = min(ret, x1 + x2);
			
			x1 = solve( (nd + 1) * 2 - 1, 0);
			x2 = solve( (nd + 1) * 2, 1);
			
			ret = min(ret, x1 + x2);
			
			x1 = solve( (nd + 1) * 2 - 1, 1);
			x2 = solve( (nd + 1) * 2, 0);
			
			ret = min(ret, x1 + x2);
		}
		else {
			x1 = solve( (nd + 1) * 2 - 1, 0);
			x2 = solve( (nd + 1) * 2, 0);
			
			ret = min(ret, x1 + x2);
			
			if(nodes[nd].change) {
				x1 = solve( (nd + 1) * 2 - 1, 0);
				x2 = solve( (nd + 1) * 2, 1);
				
				ret = min(ret, 1 + x1 + x2);
				
				x1 = solve( (nd + 1) * 2 - 1, 1);
				x2 = solve( (nd + 1) * 2, 0);
				
				ret = min(ret, 1 + x1 + x2);
			}		
		}		
	}
	
	return ret;
}

int main() {
	
	int n;
	scanf("%d", &n);
	
	int m;	
	int g, c;
	
	rep(z, n) 
	{
		nodes.clear();
		
		scanf("%d %d", &m, &V);
		int p;
		for(p = 0; p < (m - 1) / 2; p++) {
			scanf("%d %d", &g, &c);
			node k;
			k.leaf = false;
			k.t = g;
			k.change = (c == 1);
			nodes.pb(k);
		}
		for(; p < m; p++) {
			scanf("%d", &g);
			node k;
			k.leaf = true;
			k.t = g;
			k.change = false;
			nodes.pb(k);
		}
		
		memset(dp, -1, sizeof dp);
		
		int ret = solve(0, V);
		
		if(ret < INF)
			printf("Case #%d: %d\n", z + 1, ret);
		else 
			printf("Case #%d: IMPOSSIBLE\n", z + 1);
	}
	
	return 0;
	
}

