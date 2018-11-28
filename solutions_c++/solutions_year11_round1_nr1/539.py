#include <iostream>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

long long n, pd, pg, a, b, g;

bool run() {
	if (pd != 100 && pg == 100)
		return false;
	if (pd == 0)
		return true;
	if (pd != 0 && pg == 0)
		return false;
	if (pd == 100)
		return true;
	a = pd;
	b = 100;
	g = __gcd(a, b);
	a /= g;
	b /= g;
	if (n >= b)
		return true;
	else
		return false;
}

int main() {
	int T, cas = 1;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> T;
	while (T--) {
		cin >> n >> pd >> pg;
		if (run())
			printf("Case #%d: Possible\n", cas++);
		else
			printf("Case #%d: Broken\n", cas++);
	}

	return 0;
}
