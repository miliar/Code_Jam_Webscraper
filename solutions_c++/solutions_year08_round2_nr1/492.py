#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <queue>
#include <vector>
#include <string>
using namespace std;
#define		MAX(a,b)	((a)>(b)?(a):(b))
#define		MIN(a,b)	((a)<(b)?(a):(b))


int main() {
	int N;
	scanf("%d", &N);
	for (int i = 0; i < N; i ++) {
		__int64 n, A, B, C, D, x0, y0, M;
		vector <pair<__int64, __int64> > db;
		scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d", &n, &A, &B, &C, &D, &x0, &y0, &M);
		__int64 X = x0, Y = y0;
//		printf("%d %d\n", X, Y);
		db.push_back(make_pair(X, Y));
		for (int k = 1; k <= n-1; k ++) {
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
//			printf("%d %d\n", X, Y);
			db.push_back(make_pair(X, Y));
		}
		__int64 ans = 0;

		int size = db.size();

		for (int a = 0; a < size; a ++) {
			for (int b = a; b < size; b ++) {
				for (int c = b; c < size; c ++) {
					if (db[a].first == db[b].first && db[a].second == db[b].second) continue;
					if (db[a].first == db[c].first && db[a].second == db[c].second) continue;
					if (db[b].first == db[c].first && db[b].second == db[c].second) continue;

					__int64 cx = db[a].first + db[b].first + db[c].first;
					__int64 cy = db[a].second + db[b].second + db[c].second;

					if (cx % 3 == 0 && cy % 3 == 0) {
						ans ++;
						/*
						for (d = 0; d < size; d ++) {
							if (db[d].first == cx && db[d].second == cy)
								break;
						}

						if (d != size) {
							if (d != a && d != b && d != c)
								ans ++;
						}*/
					}
				}
			}
		}

		printf("Case #%d: %I64d\n", i+1, ans);
	}
	return 0;
}