#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>

using namespace std;

#define maxn (10000)
#define A first
#define B second
#define MP make_pair
#define PB push_back

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<PII, int> PIII;

int g[maxn][2];
bool flag[maxn][2];
set<PII> two, one;
int n;
/*
inline void refresh(int now) {
	for (int i = 0; i < n; ++i) {
		if (flag[i][1]) {
			f[i] = -1; continue;
		}
		if (now < g[i][0]) {
			f[i] = 0; continue;
		}
		if (now >= g[i][1]) {
			if (flag[i][0]) f[i] = 2;
			else f[i] = 3;
			continue;
		}
		if (flag[i][0]) f[i] = 0;
		else f[i] = 1;
	}
}
*/
void work() {
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d%d", &g[i][0], &g[i][1]);
	}

	memset(flag, 0, sizeof(flag));
	int now = 0, ans = 0, rest = n;
	two.clear(); one.clear();
	for (int i = 0; i < n; ++i)
		two.insert(MP(g[i][1], i));

	while (true) {
		while (!two.empty() && two.begin() -> A <= now) {
			if (flag[two.begin() -> B][0]) now += 1;
			else now += 2;
			flag[two.begin() -> B][1] = flag[two.begin() -> B][0] = true;
			rest--; ans++; two.erase(two.begin());
		}

		if (rest == 0) break;

		int t = -1, p = -1;
		for (int i = 0; i < n; ++i) if (!flag[i][0] && now >= g[i][0] && t < g[i][1])
			t = g[i][1], p = i;

		if (t == -1) {
			ans = -1; break;
		}

		ans++, now++, flag[p][0] = true;
	}

	if (ans == -1) printf("Too Bad");
	else printf("%d", ans);
}

int main() {
	int T; scanf("%d", &T);

	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		work();
		puts("");
	}

	return 0;
}
