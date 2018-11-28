#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <math.h>
#include <algorithm>
#include <queue>
#include <deque>
#include <string.h>
#include <set>
#include <stdio.h>

using namespace std;

typedef pair<int, int> ii;
typedef long long ll;
typedef long double ld;

#define FOR(I,z,k) for(int I = z; I < (k); I ++)
#define tr(container, it) \
     for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define all(v) (v).begin(), (v).end()
#define PI 3.14159265
#define tovector(arr, type) vector<type>(arr, arr + sizeof(arr)/sizeof(type))


int possible(ll pdx, ll total, ll n) {
	ll minx = min(pdx, total);
	while (1) {
		int found = 0;
		FOR(j, 2, minx/2+1) {
			if (pdx % j == 0 && total % j == 0) {
				found = 1;
				pdx /= j;
				total /= j;
				break;
			}
		}
		if (found) {
			if (total <= n) {
				break;
			}
		} else {
			break;
		}
	}
	if (total > n) {
		return 0;
	}
	return 1;
}

int main() {
	ll t, n, pd, pg;
	cin >> t;

	FOR(i, 0, t) {
		cin >> n;
		cin >> pd;
		cin >> pg;
		if (n < 100 && pd != 0) {
			if (possible(pd, 100, n) == 0) {
				cout << "Case #" << i + 1 << ": Broken" << endl;
				continue;
			}
		}

		if (pg == 0 && pd != 0) {
			cout << "Case #" << i + 1 << ": Broken" << endl;
			continue;
		}
		if (pg == 100 && pd != 100) {
			cout << "Case #" << i + 1 << ": Broken" << endl;
			continue;
		}
		cout << "Case #" << i + 1 << ": Possible" << endl;
	}
}
