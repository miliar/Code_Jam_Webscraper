#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

long long n, m, k, x[1000005];
int sol;

int main(void) {
    freopen("a.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int C, CC, i, j;
    
    scanf("%d", &CC);
    for (C = 1; C <= CC; C++) {
		cin >> n >> m >> k;
      sol = 0;

	if (n * k < m) {
		x[0] = n * k;
		for (i = 1; x[i - 1] * k < m; i++) {
			x[i] = x[i - 1] * k;
		}

		int l = -1, r = i;
		while (l + 1 < r) {
			sol++;
			int d = (r + l) / 2;
			//printf("%d %d\n", d, x[d]);
			if (d - l > r - d) {
				r = d;
			} else {
				l = d;
			}
		}
	}

     	
      printf("Case #%d: %d\n", C, sol);
    }

    exit(0);
}
