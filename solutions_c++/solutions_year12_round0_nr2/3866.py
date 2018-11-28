#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; ++test) {
		int n, s, p;
		cin >> n >> s >> p;
		int a;
		int hip = 0, ship = 0;
		for (int i = 0; i < n; ++i) {
			cin >> a;
			if (a >= (p >= 1 ? 3 * p - 2 : 0)) {
				++hip;
			} else if (a >= (p >= 2 ? 3 * p - 4 : (p >= 1 ? 3 * p - 2 : 0))) {
				++ship;
			}
		}
		cout << "Case #" << test << ": " << hip + min(ship, s) << endl;
	}
}
