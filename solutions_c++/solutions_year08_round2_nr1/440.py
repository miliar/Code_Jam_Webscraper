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
	int NC;
	scanf("%d",&NC);
	vector<long long> v1,v2;
	
	rep(i,NC) {
		v1.clear(); v2.clear();
		long long n,a,b,c,d,x0,y0,x,y,m;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld",&n,&a,&b,&c,&d,&x0,&y0,&m);
		v1.pb(x0); v2.pb(y0);
		x=x0;y=y0;
		
		rep(j,n-1) {
			x = (a*x+b)%m;
			y = (c*y+d)%m;
			v1.pb(x); v2.pb(y);
		}
		
		long long res = 0;
		rep(j,n) {
			for (int k = j+1; k < n; k++) {
				for (int l = k+1; l<n; l++) {
					if (((v1[j]+v1[k]+v1[l])%3) == 0 && ((v2[j]+v2[k]+v2[l])%3 == 0) ) res++;
				}
			}
		}
		
		printf("Case #%d: %lld\n", i+1, res);
	}
}










