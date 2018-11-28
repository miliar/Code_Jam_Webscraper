#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int tt, cas;
	cin >> tt;
	for (cas = 1; cas <= tt; cas ++) {
		long long n, pd, pg, a, b;
		cin >> n >> pd >> pg;
		d = 100 / __gcd(100ll, pd);
		g = 100 / __gcd(100ll, pg);
		cout << "Case #" << cas << ": "; 
		if (d <= n && !(pd < 100 && pg == 100) && !(pd > 0 && pg == 0))
			cout << "Possible" << endl;
		else cout << "Broken" << endl;
	}
	return 0;
}
