#include <cstdio>
#include <algorithm>

using namespace std;
const int MAXN = 100; 

int t, n, s, p, big;
int tot [MAXN]; 

bool cmp (int a, int b) {
	return a > b;
}

int main () {
	freopen ("2012b.in", "r", stdin);
	freopen ("2012b.out", "w", stdout);

	scanf ("%d\n", &t);
	for (int c = 1; c <= t; ++c) {
		scanf ("%d %d %d", &n, &s, &p);
		for (int i = 0; i < n; ++i)
			scanf ("%d\n", tot + i);
		sort (tot, tot + n, cmp);
		
		int res = 0;
		for (int i = 0; i < n; ++i) {
			if (tot [i] % 3 == 0)
				big = tot [i] / 3;
			else
				big = tot [i] / 3 + 1;
			if (big >= p)
				++res;
			else if (tot [i] % 3 == 1)
				continue;
			else if	(big + 1 >= p && s > 0 && tot [i] != 0 && tot [i] != 29)
				++res, --s;
		}
		
		printf ("Case #%d: %d\n", c, res);
	}
	fclose (stdin);
	fclose (stdout);
	return 0;
}
