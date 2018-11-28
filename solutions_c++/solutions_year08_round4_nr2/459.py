#include <string>
#include <vector>
#include <cmath>
#include <cctype>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <numeric>
#include <complex>

using namespace std;

int main(void)
{
  int n, m, a,aa;
  int N;
	int z;
  cin >> N;
  for (int c = 1; c <= N; c++) {
    cin >> n >> m >> a;
		int x1, y1, x2, y2;
		if(a > n*m) {
	    printf("Case #%d: IMPOSSIBLE\n", c);
			continue;
		}
		//printf("nma: %d %d %d\n", n, m, a);
		for(x1 = 1; x1 <= n; x1++) {
			for(y2 = a/x1; y2 <= m; y2++) {
				z = x1*y2 - a; //printf("z: %d %d %d\n", z, x1, y2);
				if(z < 0) continue;
				for(x2 = 1; x2 <= n; x2++) {
					if(z % x2 == 0 && z >= 0 && z/x2 <= m) {
						y1 = z / x2;
						goto finish;
					}
				}
			}
		}
		printf("Case #%d: IMPOSSIBLE\n", c);
		continue;

		finish:	
		aa = x1*y2-x2*y1;
    printf("Case #%d: %d %d %d %d %d %d\n", c, 0, 0, x1, y1, x2, y2);
  }
}
