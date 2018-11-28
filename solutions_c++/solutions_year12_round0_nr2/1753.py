
#include <cstdio>
#include <algorithm>
using namespace std;

int nextInt() {int x; scanf("%d", &x); return x;}

int main() {
	int testsCount;
	scanf("%d", &testsCount);
	for (int test = 0; test < testsCount; ++test) {
		int n = nextInt();
		int surprisingCount = nextInt();
		int p = nextInt();
		int res = 0;
		for (int i = 0; i < n; ++i) {
			int t;
			scanf("%d", &t);
			bool gotGivenSurprising = false;
			bool gotAnyways = false;
			for (int a = 0; a <= 10; ++a)
				for (int b = a; b <= min(a + 2, 10); ++b)
					for (int c = b; c <= min(a + 2, 10); ++c) {
						if (a + b + c != t) continue;
						if (c < p) continue;
						if (c - a == 2)
							gotGivenSurprising = true;
						else
							gotAnyways = true;
					}
			if (gotAnyways)
				++res;
			else if (gotGivenSurprising && surprisingCount > 0) {
				++res;
				--surprisingCount;
			}
		}
		printf("Case #%d: %d\n", test + 1, res);
	}
	return 0;
}
