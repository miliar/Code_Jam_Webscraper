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

int solve(vector< pair<int, int> > v) {
	int ret = 0, n_trains = 0;
	sort(all(v));
	rep(i, sz(v)) {
		if(v[i].second == 2) {
			if(n_trains == 0)
				ret++;
			else
				n_trains--;
		}
		else 
			n_trains++;
	}
	return ret;
}

int main() {
	
	int n;
	scanf("%d", &n);

	int h1, m1, h2, m2;	

	rep(z, n) 
	{
		int t, na, nb;
		scanf("%d", &t);
		scanf("%d %d", &na, &nb);	

		vector< pair<int, int> > a, b;

		rep(i, na) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			a.pb(make_pair(h1 * 60 + m1, 2));
			b.pb(make_pair(h2 * 60 + m2 + t, 1));
		}
		rep(i, nb) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			b.pb(make_pair(h1 * 60 + m1, 2));
			a.pb(make_pair(h2 *60 + m2 + t, 1));
		}

		printf("Case #%d: %d %d\n", z + 1, solve(a), solve(b));
	}
	
	return 0;
	
}
