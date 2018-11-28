#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <queue>
using namespace std;

int main() {
	//freopen("inputC.txt", "r", stdin);
	//freopen("C-small.out", "w", stdout);

	freopen("input.txt", "r", stdin);
	freopen("A-small.out", "w", stdout);

	long long t;
	cin >> t;
	for (long long e=1; e<=t; e++) {
		cout << "Case #" << e << ": ";
		long long n,k;
		cin >> n >> k;

		if (k == 0) {
			cout << "OFF\n";
			continue;
		}
		bool ans = true;
		for (long long i=0; i<=n-1; i++) {
			if ( !(k & (1LL << i)) )
				ans = false;
		}

		cout << ((ans == true) ? "ON" : "OFF") << endl;

	}

	return 0;
}