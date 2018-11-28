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

string trim(string s) {
	string r = "";
	rep(i, sz(s))
		if(isalnum(s[i]) || s[i] == ' ')
			r += s[i];
	return r;
}

int s, q;
string queries[1010];
string search_engines[110];

int dp[1010][1010][110];

int solve(int index, int changes, int engine) 
{
	if(index == q)
		return changes;
	
	int &ret = dp[index][changes][engine];
	
	if(ret != -1)
		return ret;
	
	ret = INT_MAX;
	
	if(search_engines[engine] != queries[index])
		ret = min(ret, solve(index + 1, changes, engine));
	else 
		rep(i, s) 
			if(i != engine)
				ret = min(ret, solve(index + 1, changes + 1, i));
	
	return ret;
}

int main() {
	
	int n;
	scanf("%d", &n);
	
	string e;
	
	rep(z, n) 
	{
		
		scanf("%d", &s);
		scanf("\n");
		rep(i, s)
			getline(cin, e), search_engines[i] = trim(e);
		
		scanf("%d", &q);
		scanf("\n");
		rep(i, q)
			getline(cin, e), queries[i] = trim(e);		 
		
		rep(i, q) rep(j, q) rep(k, s)
			dp[i][j][k] = -1;
		
		int ret = INT_MAX;
		rep(i, s)
			ret = min(ret, solve(0, 0, i));
		
		printf("Case #%d: %d\n", z + 1, ret);
		
	}
	
	return 0;
	
}

