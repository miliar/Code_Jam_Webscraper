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

/*
int n = 1024;
int a[11][1024][1024];

inline int d(int l, int p, int c) {
	if (a[c][l][p] != -1) {
		return a[c][l][p];
	} 
	if (p <= c*l) {
		a[c][l][p] = 0;
		return 0;
	}
	for (int i = l+1; i < p; ++i) {
		int k = (a[c][i][p] == -1 ? d(i,p,c) : a[c][i][p]);
		int c2 = (a[c][l][i] == -1 ? d(l,i,c) : a[c][l][i]);
		if (c2 > k) {
			k = c2;
		}
		if ((a[c][l][p] == -1) || (k < a[c][l][p])) {
			a[c][l][p] = k;
		}
	}
	a[c][l][p]++;
	return a[c][l][p];
}
*/

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	/*for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			for (int c = 0; c < 11; ++c) {
				a[c][i][j] = -1;
			}
		}
	}*/
	
	int tests;
	cin >> tests;
	
	for (int t = 1; t <= tests; ++t) {
		printf("Case #%d: ", t);
		
		long long l, p, c;
		cin >> l >> p >> c;

		int n = 1;
		long long cur = c*l;
		while (cur < p) {
			n++;
			cur *= c;
		}
		n -= 1;
		//cout << n;
		int res = 30; 
		while (res >= 0 && (((1 << res) & n ) == 0)) {
			res--;
		}
		res++;
		printf("%d\n", res);
	}
	return 0;
}
