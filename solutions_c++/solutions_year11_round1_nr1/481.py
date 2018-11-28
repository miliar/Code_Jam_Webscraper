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
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int d, g;
	int t;
	long long n;
	int i, j, k;
	cin >> t;
	for(k = 1; k <= t; k++) {
		cin >> n >> d >> g;
		if(d && !g || d!=100 && g==100) {
			printf("Case #%d: Broken\n", k);
			continue;
		}
		int d1 = __gcd(100,d), d2 = __gcd(100,g);
		int l1 = 100/d1, l2 = 100/d2;
		if(l1 > n) {
			printf("Case #%d: Broken\n", k);
			continue;
		}
		printf("Case #%d: Possible\n", k);
	}
	return 0;
}
