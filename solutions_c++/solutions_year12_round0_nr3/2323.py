#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

inline int count(int a, int b) {
	
	int ret = 0;
	int d = 1;
	for (int i=a; i; i/=10) d *= 10;

	int c[10];
	for (int i=a; i<b; ++i) {
		int ci = 0;
		for (int j=10; j<d; j*=10) {
			int k = (i/j)+(i%j)*(d/j);
			if (k > i && k <= b) {
				c[ci++] = k;
			}
		}
		if (ci) {
			sort(c, c+ci);
			c[ci] = 0;
			for (int j=0; j<ci; ++j) {
				if (c[j] != c[j+1]) ++ret;
			}
		}
	}

	return ret;
}

int main(void) {
	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; ++tc) {
		int a, b;
		scanf("%d%d", &a, &b);
		printf("Case #%d: %d\n", tc, count(a, b));
	}
	return 0;
}
