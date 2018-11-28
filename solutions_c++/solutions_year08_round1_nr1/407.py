#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <cstdlib>

using namespace std;

typedef long long ll;
typedef vector <ll> vll;

#define fn(n, i)		for(int i = 0; i < (n); ++i)
#define all(a)		a.begin(), a.end()

int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int T, n;
	cin >> T;
	fn(T, test) {
		cin >> n;
		vll a(n), b(n);
		fn(n, i)
			cin >> a[i];
		fn(n, i)
			cin >> b[i];
		sort(all(a));
		sort(all(b));
		ll ans = 0;
		fn(n, i)
			ans += a[i] * b[n-i-1];
		cout << "Case #" << test+1 << ": " << ans << endl;
	}

	return 0;
}