#include <cstdio>
#include <cmath>

using namespace std;
const int ten [] = {1, 10, 100, 1000, 10000, 100000, 1000000, 10000000};

int t, a, b;

int calcu (int a, int b) {
	int res = 0;
	for (int i = a; i <= b; ++i)
		for (int j = i + 1; j <= b; ++j) {
			int leni = (int)(log (i) / log (10)) + 1;
			int lenj = (int)(log (j) / log (10)) + 1;
			if (leni == lenj) {
				int len = leni;
				for (int k = 1; k < len; ++k) {
					int p1 = i / ten [len - k];
					int p2 = i % ten [len - k];
					int p = p1 + p2 * ten [k];
					if (p == j) {
						++res;
						break;
					}
				}
			}
		}
	return res;
}

int main () {
	freopen ("2012c.in", "r", stdin);
	freopen ("2012c.out", "w", stdout);
	
	scanf ("%d\n", &t);
	for (int c = 1; c <= t; ++c) {
		scanf ("%d %d\n", &a, &b);
		printf ("Case #%d: %d\n", c, calcu (a, b));
	}
	
	fclose (stdin);
	fclose (stdout);
	return 0;
}
