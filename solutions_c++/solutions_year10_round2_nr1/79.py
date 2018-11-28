#include <stdio.h>
#include <math.h>
#include <string.h>
#include <utility>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define TRACE(x...)
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x << " = " << endl)

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define _foreach(it, b, e) for (typeof(b) it = (b); it != (e); ++it)
#define foreach(x...) _foreach(x)
#define rep(i, n) foreach(i, 0, n)

#define MSET(c, v) memset(c, v, sizeof(c))

const int INF = 0x3f3f3f3f; const int NEGINF = 0xC0C0C0C0;
const int NULO = -1;
double EPS = 1.e-10;

inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
set<string> dir;
char buf[100010];
int main() {
	TRACE(setbuf(stdout, NULL));
	int T;
	scanf("%d", &T);
	rep(_42, T) {
		int N, M;
		scanf("%d %d", &N, &M);
		dir.clear();
		rep(i, N) {
			scanf(" %s", buf);
			dir.insert(buf);
		}
		int ans = 0;
		rep(i, M) {
			scanf(" %s", buf);
			while (!dir.count(buf)) {
				ans++;
				dir.insert(buf);
				int j;
				for (j = strlen(buf)-1; buf[j] != '/'; j--);
				buf[j] = '\0';
				if (j == 0) break;
			}
		}
		printf("Case #%d: %d\n", _42+1, ans);
	}
	return 0;
}
