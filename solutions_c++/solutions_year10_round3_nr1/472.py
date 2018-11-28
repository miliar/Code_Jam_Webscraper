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

int n, x[1005], y[1005], sol;

int main(void) {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int C, CC, i, j;
    
    scanf("%d", &CC);
    for (C = 1; C <= CC; C++) {
      scanf("%d", &n);
      sol = 0;
      for (i = 0; i < n; i++) {
	scanf("%d%d", &x[i], &y[i]);
	for (j = 0; j < i; j++) {
	  sol += ((x[i] < x[j] && y[i] > y [j]) || (x[i] > x[j] && y[i] < y [j]));
	}
      }

      printf("Case #%d: %d\n", C, sol);
    }

    exit(0);
}
