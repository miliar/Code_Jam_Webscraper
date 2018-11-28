#include <iostream>
#include <cmath>
#include <cstdio>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cstdlib>
#include <cassert>

using namespace std;

char b[60][60];
char tmp[60];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		printf("Case #%d: ", t);
		
		int n, k;
		cin >> n >> k;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				cin >> b[i][j];
			}
		}
		
		for (int i = 0; i < n; ++i) {
			int cur = n-1;
			for (int j = n-1; j >= 0; --j) {
				if (b[i][j] != '.') {
					tmp[cur--] = b[i][j];
				}
			}
			for (int j = n-1; j > cur; --j) {
				b[i][j] = tmp[j];
			}
			for (int j = cur; j >= 0; --j) {
				b[i][j] = '.';
			}
		}
		/*for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				printf("%c", b[i][j]);
			}
			printf("\n");
		}*/
		bool red = false;
		bool blue = false;
		for (int i = 0; i <= n-k; ++i) {
			for (int j = 0; j < n; ++j) {
				bool ok = true;
				for (int kk = 1; kk < k; ++kk) {
					if (b[i][j] != b[i+kk][j]) {
						ok = false; break;
					}
				}
				if (ok) {
					if (b[i][j] == 'R') red = true;
					else if (b[i][j] == 'B') blue = true;
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j <= n-k; ++j) {
				bool ok = true;
				for (int kk = 1; kk < k; ++kk) {
					if (b[i][j] != b[i][j+kk]) {
						ok = false; break;
					}
				}
				if (ok) {
					if (b[i][j] == 'R') red = true;
					else if (b[i][j] == 'B') blue = true;
				}
			}
		}

		for (int i = 0; i <= n-k; ++i) {
			for (int j = 0; j <= n-k; ++j) {
				bool ok = true;
				for (int kk = 1; kk < k; ++kk) {
					if (b[i][j] != b[i+kk][j+kk]) {
						ok = false; break;
					}
				}
				if (ok) {
					if (b[i][j] == 'R') red = true;
					else if (b[i][j] == 'B') blue = true;
				}
			}
		}

		for (int i = k-1; i < n; ++i) {
			for (int j = 0; j <= n-k; ++j) {
				bool ok = true;
				for (int kk = 1; kk < k; ++kk) {
					if (b[i][j] != b[i-kk][j+kk]) {
						ok = false; break;
					}
				}
				if (ok) {
					if (b[i][j] == 'R') red = true;
					else if (b[i][j] == 'B') blue = true;
				}
			}
		}
		
		if (red and blue) {
			printf("Both");
		}
		else if (red) {
			printf("Red");
		}
		else if (blue) {
			printf("Blue");
		}
		else {
			printf("Neither");
		}
		printf("\n");

	}
	return 0;
}
