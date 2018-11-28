#pragma comment(linker,"/STACK:256000000")

#ifdef __GNUC__
#define int64 long long
#else /* MSVC, say */
#define int64 __int64
#endif 

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <memory.h>
#include <ctype.h>
#include <stdlib.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <assert.h>

using namespace std;

#define MAX(a,b) (((a) > (b)) ? (a) : (b))
#define MIN(a,b) (((a) < (b)) ? (a) : (b))

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int tests;
	scanf("%d", &tests);
	for (int test = 1; test <= tests; test++) {
		printf("Case #%d: ", test);
		int a, n, m;
		scanf("%d %d %d", &n, &m, &a);
		bool ok = false;
		for (int x1 = -n; x1 <= n; x1++) {
			for (int y1 = 0; y1 <= m; y1++) {
				for (int x2 = x1; x2 <= n; x2++) {
					for (int y2 = 0; y2 <= m; y2++) {
						int area = abs(x1 * y2 - x2 * y1);			
						int dx = MAX(0, MAX(- x1, - x2));
						if (area == a && dx <= n && !ok) {
							int ansx1 = x1 + dx;
							int ansy1 = y1;
							int ansx2 = x2 + dx;
							int ansy2 = y2;
							int ansx3 = dx;
							int ansy3 = 0;
							if ((0 <= ansx1 && ansx1 <= n) &&
							(0 <= ansx2 && ansx2 <= n) &&
							(0 <= ansx3 && ansx3 <= n) &&
							(0 <= ansy1 && ansy1 <= m) &&
							(0 <= ansy2 && ansy2 <= m) &&
							(0 <= ansy3 && ansy3 <= m)) {
								ok = true;
								printf("%d %d %d %d %d %d", ansx1, ansy1, ansx2, ansy2, ansx3, ansy3);
							}
						}
					}
				}
			}
		}
		if (!ok) {
			printf("IMPOSSIBLE");
		}
		printf("\n");
	}

	return 0;
}
