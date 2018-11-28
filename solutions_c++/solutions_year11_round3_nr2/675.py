#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string>
#include <climits>
#include <vector>

#define MAX_SIZE 11111

using namespace std;

__int64 min(__int64 a, __int64 b) {
	if (a < b)
		return a;
	else
		return b;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int test = 0;
	int test_count;

	cin >> test_count;

	while (test < test_count) {
		test++;
		__int64 ans = 0;

		__int64 l, t, n, c, a[MAX_SIZE];

		cin >> l >> t >> n >> c;
		for (int i = 0; i < c; i++) {
			cin >> a[i];
			int k = 1;
			while (k*c + i < n) { a[k*c+i] = a[i]; k++; }
		}

		__int64 sum = 0;
		long cnt = 0;
		__int64 pt[MAX_SIZE];
		__int64 sum_arr[MAX_SIZE];

		for (int i = 0; i < n; i++) {
			if (sum + a[i]*2 >= t) {
				pt[cnt++] = min((sum + a[i]*2 - t)/2, a[i]);
			}
			sum += a[i]*2;

			ans += a[i]*2;
		}

		sort(&pt[0], &pt[cnt]);

		for (int i = cnt-1; i >= (cnt - l); i--) {
			ans -= pt[i];
		}


		cout << "Case #" << test << ": " << ans << endl;
	}


	return 0;
}