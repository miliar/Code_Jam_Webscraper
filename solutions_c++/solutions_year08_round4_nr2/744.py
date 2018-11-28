#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#include <iostream>
#include <utility>
#include <algorithm>
#include <set>
#include <map>
#include <vector>

using namespace std;

#define TRACE(x) x
#define DEBUG(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << x << endl)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f;

typedef long long LL;

int main() {
	int C;
	scanf(" %d", &C);
	for (int _42=1; _42 <= C; _42++) {
		int N, M, A;
		int x1,y1,x2,y2,x3,y3;
		scanf(" %d %d %d", &N, &M, &A);
		for (LL bx=0; bx <= N; bx++) {
			for (LL ay=0; ay <= M; ay++) {
				LL ax_by = A + ay*bx;
				for (LL ax=0; ax <= N; ax++) {
					for (LL by=0; by <= M; by++) {
						if (ax*by > ax_by) break;
						if (ax*by != ax_by) continue;

						x1=0;
						y1=0;

						x2=ax;
						y2=ay;

						x3=bx;
						y3=by;

						goto fim;
					}
				}
			}
		}
		printf("Case #%d: IMPOSSIBLE\n", _42);
		continue;

fim: ;
		printf("Case #%d: %d %d %d %d %d %d\n", _42, x1, y1, x2, y2, x3, y3);
	}


	return 0;
}

