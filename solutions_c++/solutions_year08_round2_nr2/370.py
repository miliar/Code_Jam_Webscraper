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

vi primes;

void calcp() {
	for(int i = 2; i < 1000; i++) {
		bool is = true;
		
		for(int j = 2; j <= sqrt(i); j++) {
			if ((i%j) == 0) {
				is = false;
				break;
			}
		}
		
		if (is) primes.pb(i);
	}
}

int main() {
	int NC;
	scanf("%d",&NC);
	calcp();
	
	vector< set<int> > v;
	
	//rep(i,sz(primes)) {
	//	cout << primes[i] << " ";
	//}
	
	rep(i,NC) {
		v.clear();
		long long a,b,p;
		scanf("%lld %lld %lld",&a,&b,&p);
		
		for(int j = a; j <= b; j++) {
			set<int> s;
			s.insert(j);
			v.pb( s );
		}
		
		long long res = 0;
		
		rep(j, sz(primes)) {
			if (primes[j] >= p) {
				int start = 0;
				while (start < a) {
					start += primes[j];
				}
				
				start += primes[j];
				
				for (int k = start; k <= b; k += primes[j]) {
					int before;
					int after;
					
					rep(x,sz(v)) {  //procurando sets
						if (v[x].find( k ) != v[x].end()) {
							before = x;
						}
						if (v[x].find( k - primes[j] ) != v[x].end()) {
							after = x;
						}
					}
					
					if (before != after) {
						v[before].insert( all(v[after]) );
						v[after].clear();
					}
				}
				
			}
		}
		
		rep(j,sz(v)) {
			if (!v[j].empty()) res++;
		}
		
		printf("Case #%d: %lld\n", i+1, res);
	}
}










