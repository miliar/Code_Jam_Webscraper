#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <cmath>
#include <algorithm>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

typedef vector <   int  > vi;
typedef vector <   vi   > vvi;
typedef vector < double > vd;
typedef vector <   vd   > vvd;
typedef vector < string > vs;

int numDigits (ll A) {
	if (A == 0LL)
		return 0;
	return numDigits (A/10) + 1;
}

ll pot10 (int exp) {
	if (exp == 0)
		return 1;
	return 10LL * pot10(exp-1);
}

int howMany (ll x, ll A, ll B, int ndigit) {
	ll pot = pot10(ndigit-1), ini = x;
	int ans = 0;

	set<int> used;
	for (int i = 0; i < ndigit - 1; i++) {
		ll d = x%10;
		x /= 10;

		x += (d * pot);
		
		if (x > ini && x <= B && x >= A && (used.find(x) == used.end())) {
			ans++;
			used.insert(x);
		}
	}

	return ans;
}

int main () {
	int T; cin >> T;

	for (int t = 1; t <= T; t++) {
		ll A, B, ans = 0LL; cin >> A >> B;

		int ndigit = numDigits (A);

		for (ll i = A; i < B; i++) {
			ans += howMany (i, A, B, ndigit);
		}

		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}
