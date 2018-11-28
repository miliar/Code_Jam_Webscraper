#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define FOR(i, L, R) for (int i = (L); i <= (R); ++i)
#define ROF(i, R, L) for (int i = (R); i >= (L); --i)

using namespace std;

int T, R;
int x1, y1, x2, y2;
bool a[107][107];
bool b[107][107];

int main()
{
	scanf("%d", &T);
	FOR(testCase, 1, T) {
		scanf("%d", &R);
		memset(a, 0, sizeof a);
		int X = 0, Y = 0;
		REP(i, R) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			FOR(p, x1, x2)
				FOR(q, y1, y2) a[p][q] = true;
			X = max(X, x2);
			Y = max(Y, y2);
		}
		int ans = 0;
		bool flag = false;
		do {
			flag = false;
			memmove(b, a, sizeof b);
			FOR(i, 1, X)
				FOR(j, 1, Y) {
					if (a[i][j])
						flag = true;
					if (a[i][j] && !a[i - 1][j] && !a[i][j - 1])
						b[i][j] = false;
					if (!a[i][j] && a[i - 1][j] && a[i][j - 1])
						b[i][j] = true;
				}
			memmove(a, b, sizeof a);
			++ans;
		} while (flag);
		printf("Case #%d: %d\n", testCase, ans - 1);
	}
//	system("pause");
}
