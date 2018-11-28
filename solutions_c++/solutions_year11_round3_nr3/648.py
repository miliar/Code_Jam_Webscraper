#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <climits>

#define MAX_SIZE 111111

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int test = 0;
	int test_count;

	cin >> test_count;

	while (test < test_count) {
		test++;

		int n, a[11111];
		int l, h;
		
		cin >> n >> l >> h;

		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}

		int ans = 0;

		for (int i = l; i <= h; i++) {
			bool is_ok = true;

			for (int j = 0; j < n; j++) {
				if ((a[j] > i && a[j] % i != 0) || 
					(i > a[j] && i % a[j] != 0)) {
					is_ok = false;
				}
			}

			if (is_ok) {
				ans = i; 
				break;
			}
		}

		if (ans == 0) {
			cout << "Case #" << test << ": NO" << endl;
		} else {
			cout << "Case #" << test << ": " << ans << endl;
		}

		
	}

	return 0;
}