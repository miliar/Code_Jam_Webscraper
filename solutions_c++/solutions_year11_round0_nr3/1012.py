/*
ID: gupan881
PROG: Candy
LANG: C++
*/
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <bitset>
#include <vector>
#include <stack>
#include <list>
#include <utility>
#include <queue>
#include <set>
#include <map>
using namespace std;
int
main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int t, k, i, j, n;
	cin >> t;
	for(k = 1; k <= t; k++) {
		cin >> n;
		int tmp;
		int sum = 0, xsum = 0;
		int m = 1000000007;
		for(i = 0; i < n; i++) {
			cin >> tmp;
			xsum ^= tmp;
			sum += tmp;
			m = min(m, tmp);
		}
		if(xsum)
			printf("Case #%d: NO\n", k);
		else
			printf("Case #%d: %d\n", k, sum-m);
	}
	return 0;
}
