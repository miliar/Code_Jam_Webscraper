#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <numeric>
using namespace std;

#define FOR(i, a, b) for(int i = (int)a; i < (int)b; ++i)
#define REP(i, n) for(int i = 0; i < (int)n; ++i)
#define TR(it, c) for(typeof(c.begin()) it = c.begin(); it != c.end(); ++it)

#define rAll(c) (c).rbegin(), (c).rend()

#define sz size()
#define pb push_back
#define mp make_pair
#define fi first
#define se second
/*
void print(vector<int> v) {
	REP(i, v.sz) cout << v[i] << " ";
	cout << endl;
}*/

int main() {
	int T, n, tmp; 
	
	
	cin >> T;
	REP(iCase, T) {
		cin >> n;
		vector<long long> a, A, b, B, c, C;
		REP(i, n) {cin >> tmp; if (tmp < 0) a.pb(-tmp); else A.pb(tmp);}
		REP(i, n) {cin >> tmp; if (tmp < 0) b.pb(-tmp); else B.pb(tmp);}
		sort(rAll(a));
		sort(rAll(A));
		sort(rAll(b));
		sort(rAll(B));
		/*
		print(a);
		print(A);
		print(b);
		print(B);
		*/
		long long m1 = min(a.sz, B.sz), m2 = min(b.sz, A.sz), ret = 0;
	
		REP(i, m1) ret -= a[i] * B[i]; 
		//cout << "a[i] = " << a[i] << " * B[i] = " << B[i] << " = " << a[i] * B[i] << endl;}
		FOR(i, m1, a.sz) c.pb(a[i]);
		FOR(i, m1, B.sz) C.pb(B[i]);
		
		REP(i, m2) ret -= b[i] * A[i]; 
		//cout << "b[i] = " << b[i] << " * A[i] = " << A[i] << " = " << b[i] * A[i] << endl;}
		FOR(i, m2, b.sz) C.pb(b[i]);
		FOR(i, m2, A.sz) c.pb(A[i]);
		
		if (c.sz != C.sz) cerr << "mismatch" << endl;
		REP(i, c.sz) ret += c[i] * C[c.sz-1-i];
		cout << "Case #" << iCase + 1 << ": " << ret << endl;
		
	}
	
	
	return 0;
}
