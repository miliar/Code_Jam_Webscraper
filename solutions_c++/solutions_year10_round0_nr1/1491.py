#include <iostream>
#include <vector>

using namespace std;

void solve(int c) {
	int n; cin >> n;
	int k; cin >> k;
	long long p = 1;

	for (int i = 0; i < n; i++) p *= 2;
	cout << "Case #" << c << ": " << ((k + 1) % p == 0?"ON":"OFF") << endl;
}

int main () {
	int nt; cin >> nt; int c = 1;
	while (nt-- != 0) solve(c++);

	return 0;
}
