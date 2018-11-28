#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long i64;
typedef unsigned long u32;
template<class T> int size(const T &a) {
	return int(a.size());
}
template<class T> T sqr(const T &a) {
	return a * a;
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int itest = 1; itest <= T; itest++) {
		printf("Case #%d: ", itest);
		int xsum = 0, sum = 0, mn = int(2e9);
		int n;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			int a;
			scanf("%d", &a);
			xsum ^= a;
			sum += a;
			mn = min(a, mn);
		}
		if (xsum == 0) {
			printf("%d\n", sum - mn);
		} else {
			printf("NO\n");
		}
	}
	return 0;
}
