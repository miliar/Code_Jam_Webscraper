#include <iostream>
#include <algorithm>
#include <utility>
#include <climits>
#include <vector>
#include <list>
#include <set>
#include <cmath>
using namespace std;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forsn(i, s, n) for(int i=(s); i<(int)(n); ++i)
#define forall(it, X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define abs(a) ((a)>0 ? (a):-(a))
#define DBG(a) cerr << #a << " = " << a << endl;
typedef vector<int> vint;
typedef vector<vint> vvint;

int gcd(int a, int b) {
	if(!b) return a;
	for(;;) {
		a %= b;
		if(!a) return b;
		b %= a;
		if(!b) return a;
	}
}

int main() {
	int C;
	cin >> C;
	forn(c,C) {
		int N;
		cin >> N;
		vint t(N);
		forn(i,N)
			cin >> t[i];
		int res = abs(t[1]-t[0]);
		forsn(i,2,N)
			res = gcd(res, abs(t[i]-t[i-1]));
		int y = res - t[0];
		while(y < 0) y += res;
//		cout << gcd(t[0]+y, res) << endl;
		cout << "Case #" << c+1 << ": " << y << endl;
	}
	return 0;
}
