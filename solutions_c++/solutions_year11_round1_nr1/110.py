#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {
		cout << "Case #" << tt << ": ";
		long long n, pd, pg;
		cin >> n >> pd >> pg;
		long long g = __gcd(100LL, pd);
		long long x = pd / g;
		long long d = 100LL / g;
		if (d > n) {
			cout << "Broken" << endl;
			continue;
		}
		if (pg != 100) {
			if (pg == 0) {
				if (pd == 0) {
					cout << "Possible" << endl;
				} else {
					cout << "Broken" << endl;
				}
				continue;
			}
			cout << "Possible" << endl;
		} else {
			if (pd == 100) {
				cout << "Possible" << endl;
			} else {
				cout << "Broken" << endl;
			}
		}
	}
}