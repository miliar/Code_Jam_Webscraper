#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c-out.txt", "w", stdout);
	int tests;
	cin >> tests;
	for(int test = 0; test < tests; test++) {
		int n;
		cin >> n;
		vector<int> a(n);
		for(int i = 0; i < n; i++) {
			cin >> a[i];
		}
		int endElement = (1 << n) - 1;
		int startElement = 1;
		int maxSum = 0;
		for (int i = startElement; i < endElement; i++) {
			int sE = 0;
			int xP = 0;
			int xE = 0;
			int ti = i;
			for (int j = 0; j < n; j++) {
				int p = ti & 1;
				ti >>= 1;
				if (p) {
					sE += a[j];
					xE ^= a[j];
				}else {
					xP ^= a[j];
				}
			}
			if(xP == xE) {
				maxSum = max(sE, maxSum);
			}
		}
		if(maxSum == 0) {
			cout << "Case #" << test + 1 << ": NO\n";
		}else {
			cout << "Case #" << test + 1 << ": " << maxSum << endl;
		}
	}
	return 0;
}