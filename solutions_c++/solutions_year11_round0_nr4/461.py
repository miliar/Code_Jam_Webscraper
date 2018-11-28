#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <iostream>
#include <sstream>

using namespace std;

typedef long long i64;

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
		int n;
		scanf("%d", &n);
		int c = 0;
		for (int i = 0; i < n; i++) {
			int a;
			scanf("%d", &a);
			if (i != a - 1) c++;
		}
		/*int k = c / 3;
		c %= 3;
		if (c == 1) {
			c += 3;
			k--;
		}*/
		printf("%.6lf\n", double(c));
	}
	return 0;
}
