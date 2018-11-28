#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <functional>
#include <algorithm>

using namespace std;

#define	PI	3.14159265358979323846

int cost[12][1024];

int count(int *m, int n, int p, int g)
{
	if (p <= 0) return 0;

	int i, c = 0, found = 0, must = 0;
	for (i = 0; i < n; i++)
		if (m[i] >= p) {
			must = 1;
			break;
		}
	if (must) {
		c = cost[p][g];
		for (i = 0; i < n; i++) m[i]--;
		c += count(m, n / 2, p - 1, g * 2) + count(m + n / 2, n / 2, p - 1, g * 2 + 1);
		for (i = 0; i < n; i++) m[i]++;
	} else {
		for (i = 0; i < n; i++) {
			if (m[i] > 0) {
				found = 1;
				break;
			}
		}
		if (found) {
			for (i = 0; i < n; i++) m[i]--;
			int c1 = cost[p][g] + count(m, n / 2, p - 1, g * 2) + count(m + n / 2, n / 2, p - 1, g * 2 + 1);
			for (i = 0; i < n; i++) m[i]++;
			int c2 = count(m, n / 2, p - 1, g * 2) + count(m + n / 2, n / 2, p - 1, g * 2 + 1);
			c = min(c1, c2);
		}
	}

	return c;
}

int main(int argc, char *argv[])
{
	int nc, ci;
	int i, j, k, n, p, t;
	static int m[2048];
	
	scanf("%d", &nc);
	for (ci = 1; ci <= nc; ci++) {
		scanf("%d", &p);
		n = 1 << p;
		for (i = 0; i < n; i++) {
			scanf("%d", &m[i]);
			m[i] = p - m[i];
		}
		memset(cost, 0, sizeof(cost));
		for (k = p - 1; k >= 0; k--) {
			for (i = 0; i < (1 << k); i++)
				scanf("%d", &cost[p - k][i]);
		}
		
		printf("Case #%d: %d\n", ci, count(m, n, p, 0));
	}

	return 0;
}
