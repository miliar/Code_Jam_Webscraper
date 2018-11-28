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

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int tests;
	cin >> tests;
	for (int t = 1; t <= tests; ++t) {
		printf("Case #%d: ", t);
		
		int n;
		cin >> n;
		vector<int> a(n), b(n);
		for (int i = 0; i < n; ++i) {
			cin >> a[i] >> b[i];
		}
		
		int res = 0;
		for (int i = 0; i < n; ++i) {
			for (int j = i + 1; j < n; ++j) {
				if (a[i] < a[j] && b[i] > b[j]) {
					res++;
				} 
				else if (a[i] > a[j] && b[i] < b[j]) {
					res++;
				}
			}
		}
		printf("%d\n", res);
	}
	return 0;
}
