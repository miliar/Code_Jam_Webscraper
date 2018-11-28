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

int main() {
	
	int c, n, m, t;
	scanf("%d", &c);
	
	int a, b;
	
	int milk[11];
	vector< pair<int, int> > cust[101];
	
	rep(z, c) 
	{
		scanf("%d", &n);
		scanf("%d", &m);
		
		rep(i, m) {
			scanf("%d", &t);
			cust[i] = vector< pair<int, int> >(t);
			rep(j, t) scanf("%d %d", &a, &b), cust[i][j] = make_pair(a - 1, b);
		}
		
		bool has_valid = false;
		
		int mn = INT_MAX;
		string ret = "";
		
		rep(i, (1 << n)) 
		{
			rep(j, n)
				if((i & (1 << j)) != 0)
					milk[j] = 1;
				else 
					milk[j] = 0;
			
			bool ok = true;
			
			rep(j, m) 
			{
				bool cust_ok = false;
				rep(k, sz(cust[j]))
					if(cust[j][k].second == milk[cust[j][k].first])
						{ cust_ok = true; break; }
				
				if(!cust_ok) {
					ok = false;
					break;
				}
			}			
			
			if(ok) {
				has_valid = true;
				int tot = accumulate(milk, milk + n, 0);
				if(tot < mn) {
					mn = tot;
					ret = "";
					rep(j, n) ret += (milk[j] == 1 ? "1 " : "0 ");
					ret = ret.substr(0, sz(ret) - 1);
				}
			}
		}
		
		if(!has_valid) printf("Case #%d: IMPOSSIBLE\n", z + 1);
		else printf("Case #%d: %s\n", z + 1, ret.c_str());

	}
	
	return 0;
	
}

