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
#include <deque>

#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi; 
typedef vector<string> vs;
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define rep(i, n) for(int i = 0; i < n; ++i) 
#define foreach(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) 
#define INT_INF 0x7FFFFFFF
// BEGIN CUT HERE
#define TRACE(x...) x
#define watch(x) TRACE(cout << #x" = " << x << endl)

string itos(int x) { stringstream ss; ss << x; return ss.str(); }
vector<string> split(string s) { vector<string> r; string t; stringstream ss(s); while(ss >> t) r.push_back(t); return r; }


int main() {
	int T,N,val;
	vi a,b;
	scanf("%d",&T);
	
	rep(i,T) {
		long long res = 0;
		a.clear(); b.clear();
		
		scanf("%d",&N);
		rep(j,N) {
			scanf("%d",&val); 
			a.pb(val);
		}
		rep(j,N) {
			scanf("%d",&val); 
			b.pb(val);
		}
		
		sort(all(a)); sort(all(b));
		reverse(all(b));
		
		
		rep(j,N) {
			res += a[j]*b[j];
		}
		
		
		printf("Case #%d: %d\n", (i+1), res);
	}
}










