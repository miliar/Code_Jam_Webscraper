#include <iostream>
#include <algorithm>
#include <utility>
#include <climits>
#include <vector>
#include <list>
#include <set>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forall(it, X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define DBG(a) cerr << #a << " = " << a << endl;
typedef long long int tint;
typedef vector<tint> vint;
typedef vector<vint> vvint;
typedef pair<tint,tint> pii;

int main() {
	tint T,R,k,N;
	cin >> T;
	forn(t,T) {
		cin >> R >> k >> N;
		vint g(N);
		forn(i,N) cin >> g[i];
		vint p(N), f(N);
		forn(i,N) {
			int j=i, sum=0;
			do {
				int x = sum + g[j];
				if(x > k) break;
				sum = x;
				j = (j+1)%N;
			} while(j!=i);
			p[i] = sum;
			f[i] = j;
		}
		tint i=0, gan=0;
		vector<pii> emp(N,pii(-1,0));
		for(tint r=0; r<R; ) {
			tint cycle = r-emp[i].first;
			if(emp[i].first!=-1 && (R-r>=cycle)) {
				tint x = (R-r) / cycle;
				r += x*cycle;
				gan += x*(gan-emp[i].second);
			} else {
				emp[i] = pii(r,gan);
				r++;
				gan += p[i];
				i = f[i];
			}
		}
		cout << "Case #" << t+1 << ": " << gan << endl;
	}
	return 0;
}
