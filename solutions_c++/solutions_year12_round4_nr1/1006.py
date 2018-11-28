#define FILEIO

#define INPUT "in"
#define OUTPUT "out"

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cctype>
#include <vector>
#include <cassert>

#define mp make_pair
#define pb push_back
#define foreach(i,T) for(__typeof(T.begin()) i = T.begin(); i != T.end(); ++i)

using namespace std;

namespace Solve {
	const int MAXN = 20000;

	inline int ScanInt(void) {
		int r = 0, c, d;
		while (!isdigit(c = getchar()) && c != '-');
		if (c != '-') r = c - '0'; d = c;
		while ( isdigit(c = getchar())) r = r * 10 + c - '0';
		return d=='-'?-r:r;
	}

	int a[MAXN], d[MAXN], n, D;
	int vis[MAXN];
	inline void solve(void) {
		memset(vis, 0, sizeof vis);
		n = ScanInt();
		for (int i = 1; i <= n; i++) d[i] = ScanInt(), a[i] = ScanInt(); D = ScanInt();
		vis[1] = d[1];
		for (int i = 2; i <= n; i++) {
			for (int j = 1; j <= i - 1; j++) if (d[i] - d[j] <= vis[j]) {
				vis[i] = max(vis[i], min(d[i] - d[j], a[i]));
			}
		}
		bool OK = false;
		for (int i = 1; i <= n; i++) if (vis[i] >= D - d[i]) {
			OK = true; break;
		}
		if (OK) puts("YES"); else puts("NO");
	}
}

int main(void) {
	#ifdef FILEIO
		freopen(INPUT, "r", stdin);
		freopen(OUTPUT, "w", stdout);
	#endif
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		printf("Case #%d: ", i);
		Solve::solve();
	}
	return 0;
}
