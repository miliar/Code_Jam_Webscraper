/*
ID: gupan881
PROG: Goro
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
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int t, k, i, j;
	cin >> t;
	for(k = 1; k <= t; k++) {
		int n, tmp;
		cin >> n;
		double ans = 0;
		for(i = 1; i <= n; i++) {
			cin >> tmp;
			ans += (tmp!=i);
		}
		printf("Case #%d: %.6lf\n", k, ans);
	}
	return 0;
}
