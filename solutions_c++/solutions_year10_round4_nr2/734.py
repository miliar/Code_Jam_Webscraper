#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>

using namespace std;

#define forsn(i,s,n) for(int i=(s); i < (n); i++)
#define forn(i,n) forsn(i,0,(n))
#define dforsn(i,s,n) for(int i=(n)-1;i>=(s);i--)
#define dforn(i,n) dforsn(i,0,(n))

typedef long long tint;

tint p, n;

tint rango(vector<tint> m, int A, int N) {
	forsn(i,A,A+N) {
		if (m[i] > 0) {
			forsn(j,A,A+N) m[j]--;
			return 1 + rango(m,A,N/2) + rango(m,A+N/2,N/2);
		}
	}
	return 0;
}

int main() {
	tint T;
	cin >> T;
	forn(icase,T) {
		cin >> p; n = 1; forn(i,p) n*=2;
		
		vector<tint> m(n);
		vector< vector<tint> > pr(n, vector<tint>(n, 0));
		
		forn(i,n) cin >> m[i];
		forn(i,n) m[i] = p - m[i];
		tint k = n/2;
		forn(i,p) {
			forn(j,k) {
				cin >> pr[i][k];
			}
			k/=2;
		}
		int sol = rango(m, 0, n);
		cout << "Case #" << (icase+1) << ": " << sol << endl;
	}
	return 0;
}
