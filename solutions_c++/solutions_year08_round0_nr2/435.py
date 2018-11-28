#include <cstdio>
#include <memory>

const int maxn = 250;

struct TTrip {
	int depart, arrive;
};

int casei, cases, ta, na, nb, ans, ans1, ans2, n;
bool avai[maxn];
int from[maxn];
TTrip trip[maxn];
bool g[maxn][maxn];

inline void getTrip(int now) {
	int n1, n2;
	scanf(" %d:%d", &n1, &n2);
	trip[now].depart = n1 * 60 + n2;
	scanf(" %d:%d", &n1, &n2);
	trip[now].arrive = n1 * 60 + n2;
}

inline void init() {
	scanf("%d", &ta);
	scanf("%d%d", &na, &nb);
	for (int i = 0; i < na; ++i) getTrip(i);
	for (int i = 0; i < nb; ++i) getTrip(na + i);
}

inline void build() {
	memset(g, false, sizeof g);
	for (int i = 0; i < na; ++i)
		for (int j = 0; j < nb; ++j) if (trip[i].arrive + ta <= trip[j + na].depart) g[i][j + na] = true;
	for (int i = 0; i < na; ++i)
		for (int j = 0; j < nb; ++j) if (trip[j + na].arrive + ta <= trip[i].depart) g[j + na][i] = true;
}

inline bool match(int now) {
	if (now == -1) return true;
	for (int i = 0; i < n; ++i) if (g[now][i] && avai[i]) {
		avai[i] = false;
		if (match(from[i])) {
			from[i] = now;
			return true;
		}
	}
	return false;
}

inline void process() {
	build();

	n = na + nb;
	memset(from, 255, sizeof from);
	for (int i = 0; i < n; ++i) {
		memset(avai, true, sizeof avai);
		if (match(i)) ++ans;
	}

	ans1 = 0;
	for (int i = 0; i < na; ++i) if (from[i] == -1) ++ans1;
	ans2 = 0;
	for (int i = 0; i < nb; ++i) if (from[i + na] == -1) ++ans2;
}

inline void print() {
	printf("Case #%d: %d %d\n", casei, ans1, ans2);
}

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
