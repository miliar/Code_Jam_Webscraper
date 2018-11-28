#include <iostream>

using namespace std;

int gcd(int a, int b) {
	if (a == 0 && b == 0)
		return 0;
	int t;
	while (b) {
		t = b;
		b = a%b;
		a = t;
	}
	return a;
}

int n, pd, pg;
bool possib() {
	int minn = 100/gcd(100, pd);
	if (pg == 0) {
		return pd == 0;
	} else if (pg < 100) {
		return minn <= n;
	} else if (pg == 100) {
		return pd == 100;
	}
}

int main() {
	int T; cin >> T;
	for (int test = 1; test <= T; ++test) {
		cin >> n >> pd >> pg;
		cout << "Case #" << test << ": ";
		if (possib())
			cout << "Possible" << endl;
		else
			cout << "Broken" << endl;
	}
}

