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

int ngroups(string s) 
{
	int r = 0;
	int p = 0;
	while(p < sz(s)) {
		char c = s[p];
		while(p < sz(s) && s[p] == c) p++;
		r++;
	}
	return r;
}

int main() {
	
	int N, K;
	scanf("%d", &N);
	
	char buff[1001];
	
	rep(z, N) 
	{
		scanf("%d", &K);
		scanf("%s", buff);
		
		string s(buff);
		
		vi v;
		rep(i, K) v.pb(i);

		int ret = INT_MAX;
		
		do {
			
			string r = "";
			
			int p = 0;
			while(p < sz(s)) {
				string t = s.substr(p, K);
				rep(i, K) {
					r += t[v[i]];
				}
				p += K;
			}
			
			ret = min(ret, ngroups(r));
			
		} while(next_permutation(all(v)));
		
		printf("Case #%d: %d\n", z + 1, ret);
	}
	
	return 0;
	
}

