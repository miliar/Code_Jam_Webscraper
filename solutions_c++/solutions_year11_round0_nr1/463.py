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
		int t[2] = {0, 0}, p[2] = {1, 1};
		int n;
		scanf("%d", &n);
		int rtime = 0;
		for (;n--;) {
			char c;
			int cp;
			scanf(" %c %d", &c, &cp);
			int i = (c == 'B'? 1 : 0);
			int dt = abs(cp - p[i]);
			t[i] = max(t[i] + dt, rtime) + 1;
			p[i] = cp;
			rtime = t[i];
		}
		printf("%d\n", rtime);
	}
	return 0;
}
