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
	
	int t, n, k;
	scanf("%d", &t);
	
	vi v1, v2;
	
	rep(z, t) 
	{
		scanf("%d", &n);
		v1 = vi(n);
		v2 = vi(n);
		
		rep(i, n) scanf("%d", &k), v1[i] = k;
		rep(i, n) scanf("%d", &k), v2[i] = k;
		
		sort(all(v1));
		sort(all(v2));
		
		int mn = INT_MAX;
		
		do {
			int v = 0;
			rep(i, sz(v1))
				v += v1[i] * v2[i];
			mn = min(mn, v);
		} while(next_permutation(all(v2)));
		
		printf("Case #%d: %d\n", z + 1, mn);
	}
	
	return 0;
	
}

