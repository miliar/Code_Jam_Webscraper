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

int m[2048];
int pr[1024][1024];
int d[1024][1024][16];


int ans(int l, int p, int k) {
	//cout << "lala";
	if (l == -1) {
		return 0;
	}
	if (d[l][p][k] == -1) {
		int a1 = pr[l][p] + ans(l-1, 2*p, k) + ans(l-1, 2*p+1, k);
		int st = p * (1 << (l+1));
		int fin = (p + 1) * (1 << (l+1));
		bool can_skip = true;
		for (int i = st; i < fin; ++i) {
			if (m[i] - k <= 0) {
				can_skip = false;
				break;
			}
		}
		int a2 = a1;
		if (can_skip) {
			a2 = ans(l-1, 2*p, k+1) + ans(l-1, 2*p+1, k+1);
		}
		d[l][p][k] = a1 < a2 ? a1 : a2;
	}
	return d[l][p][k];
}

int main() {
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		printf("Case #%d: ", t);
		
		for (int i = 0; i < 1024; ++i) {
			for (int j = 0; j < 1024; ++j) {
				for (int k = 0; k < 16; ++k) {
					d[i][j][k] = -1;
				}
			}
		}
		
		int p = 0;
		cin >> p;
		for (int i = 0; i < (1<<p); ++i) {
			cin >> m[i];
		}
		for (int i = p-1; i >= 0; --i) {
			for (int j = 0; j < (1 << i); ++j) {
				cin >> pr[p-1-i][j];
			}
		}
		
		int res = ans(p-1, 0, 0);
		
		printf("%d\n", res);
	}
	return 0;
}
