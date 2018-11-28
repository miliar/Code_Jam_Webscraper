#include <cstdlib>
#include <iostream>

using namespace std;

int compare(const void * a, const void * b) {
	return (*(int*) a - *(int*) b);
}

int main() {
	int t, i, n, e;
	int* c;
	cin >> t;
	for (i = 0; i < t; ++i) {
		cin >> n;
		c = new int[n];
		int S1 = 0, S = 0, S2 = 0;
		for (e = 0; e < n; ++e) {
			cin >> c[e];
			S1 ^= c[e];
			S += c[e];
		}
		qsort(c, n, sizeof(c), compare);
		e = 0;
		do {
			S1 ^= c[e];
			S2 ^= c[e];
			S -= c[e];
			++e;
		} while (e < n && S1 != S2);
		cout << "Case #" << i + 1 << ": ";
		if (e == n)
			cout << "NO" << endl;
		else
			cout << S << endl;
		delete[] c;
	}
	return 0;
}
