#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

#define forsn(i,s,n) for(int i=(s);i<(n);i++)
#define forn(i,n) forsn(i,0,(n))

typedef long long int tint;

int main() {
	tint T;
	cin >> T;
	forn(icase,T) {
		tint R, k, N;
		cin >> R >> k >> N;
		vector<tint> v(N);
		vector< pair<tint, tint> > amount(N); // groups, total
		forn(i,N) cin >> v[i];
		
		forn(i,N) {
			tint am = 0, w = 0;
			forn(j,N) {
				tint id = (i+j) % N;
				if (w + v[id] <= k) { w += v[id]; am++; }
				else break;
				if (am == N) break;
			}
			amount[i] = make_pair(am, w);
		}
		
		tint ind = 0;
		tint euros = 0;
		
		forn(i,R) {
			euros += amount[ind].second;
			ind = (ind + amount[ind].first) % N;
		}
		cout << "Case #" << (icase+1) << ": " << euros << endl;
		
	}
	return 0;
}
