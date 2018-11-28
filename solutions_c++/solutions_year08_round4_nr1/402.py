#include <cstdio>

const int maxn = 10100;
const int oo = 2147483647;

struct TNode {
	int c0, c1, chbl, value;
};

int n, m, ans, casei, cases;
TNode node[maxn + 1];

inline void init() {
	scanf("%d%d", &n, &m);
	for (int i = 1; i <= (n - 1) / 2; ++i) {
		scanf("%d%d", &node[i].value, &node[i].chbl);
	}
	int now = (n - 1) / 2;
	for (int i = 1; i <= (n + 1) / 2; ++i) {
		int j;
		scanf("%d", &j);
		if (j == 0) {
			node[i + now].c0 = 0; node[i + now].c1 = -1;
		}
		else {
			node[i + now].c0 = -1; node[i + now].c1 = 0;
		}
		node[i + now].chbl = false;
	}
}

inline void getOR(int now, int plus) {
	if (node[now + now].c1 != -1 && node[now + now + 1].c1 != -1)
		if (node[now + now].c1 + node[now + now + 1].c1 + plus < node[now].c1)
			node[now].c1 = node[now + now].c1 + node[now + now + 1].c1 + plus;

	if (node[now + now].c1 != -1 && node[now + now + 1].c0 != -1)
		if (node[now + now].c1 + node[now + now + 1].c0 + plus < node[now].c1)
			node[now].c1 = node[now + now].c1 + node[now + now + 1].c0 + plus;

	if (node[now + now].c0 != -1 && node[now + now + 1].c1 != -1)
		if (node[now + now].c0 + node[now + now + 1].c1 + plus < node[now].c1)
			node[now].c1 = node[now + now].c0 + node[now + now + 1].c1 + plus;

	if (node[now + now].c0 != -1 && node[now + now + 1].c0 != -1)
		if (node[now + now].c0 + node[now + now + 1].c0 + plus < node[now].c0)
			node[now].c0 = node[now + now].c0 + node[now + now + 1].c0 + plus;
}

inline void getAND(int now, int plus) {
	if (node[now + now].c1 != -1 && node[now + now + 1].c1 != -1)
		if (node[now + now].c1 + node[now + now + 1].c1 + plus < node[now].c1)
			node[now].c1 = node[now + now].c1 + node[now + now + 1].c1 + plus;

	if (node[now + now].c1 != -1 && node[now + now + 1].c0 != -1)
		if (node[now + now].c1 + node[now + now + 1].c0 + plus < node[now].c0)
			node[now].c0 = node[now + now].c1 + node[now + now + 1].c0 + plus;

	if (node[now + now].c0 != -1 && node[now + now + 1].c1 != -1)
		if (node[now + now].c0 + node[now + now + 1].c1 + plus < node[now].c0)
			node[now].c0 = node[now + now].c0 + node[now + now + 1].c1 + plus;

	if (node[now + now].c0 != -1 && node[now + now + 1].c0 != -1)
		if (node[now + now].c0 + node[now + now + 1].c0 + plus < node[now].c0)
			node[now].c0 = node[now + now].c0 + node[now + now + 1].c0 + plus;
}

inline void process() {
	for (int i = (n - 1) / 2; i >= 1; --i) {
		node[i].c0 = oo;
		node[i].c1 = oo;
		if (node[i].value == 0) {
			getOR(i, 0);
			if (node[i].chbl) getAND(i, 1);
		}
		else {
			getAND(i, 0);
			if (node[i].chbl) getOR(i, 1);
		}
		if (node[i].c0 == oo) node[i].c0 = -1;
		if (node[i].c1 == oo) node[i].c1 = -1;
	}
}

inline void print() {
	printf("Case #%d: ", casei);
	if (m == 1) ans = node[1].c1;
	else ans = node[1].c0;
	if (ans == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n", ans);
}

int main() {
//	freopen("in.txt", "r", stdin); freopen("", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);

	scanf("%d", &cases);
	for (casei = 1; casei <= cases; ++casei) {
		init();
		process();
		print();
	}
}
