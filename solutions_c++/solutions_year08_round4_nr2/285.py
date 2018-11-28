#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a):(-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))

#define pii pair < int, int >
#define MP make_pair
#define X first
#define Y second 


#define TYPE long long

TYPE a, n, m;

int main () {
	int i, j, T;

	scanf("%d", &T);
	
	for (int cas = 1; cas <= T; cas++) {

		scanf("%lld%lld%lld", &n, &m, &a);

		TYPE x1, x2, y1, y2;
		bool ok = false;

		for (x1 = 0; x1 <= n && !ok; x1++) {
			for (x2 = 0; x2 <= n && !ok; x2++) {
				for (y1 = 0; y1 <= m && !ok; y1++) {
					for (y2 = 0; y2 <= m && !ok; y2++) {
						if (x1*y2 - x2*y1 == a) {
							ok = true;
							break;
						}
					}
					if (ok) break;
						
				}
				if (ok) break;
			}
			if (ok) break;
		}
			

		printf("Case #%d:", cas);
		if (ok) {
			printf(" 0 0 %lld %lld %lld %lld\n", x1, y1, x2, y2);
		}
		else {
			printf(" IMPOSSIBLE\n");
		}	
	}

	return 0;
}