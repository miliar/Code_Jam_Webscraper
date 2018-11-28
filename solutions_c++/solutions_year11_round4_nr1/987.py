#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

const int MAX = 5200;
const double eps = 1e-8;
typedef long long LL;
int x, s, r, t, n, top;

int sgn(double x) {
	return x < -eps ? -1 : x > eps;
}

struct Node {
	int l, r, v;
	bool operator<(const Node& node) const {
		return v < node.v;
	}
} node[MAX];

double run() {
	double left = t;
	int x = 0;
	double ret = 0;

	for (int i = 0; i < top; i++) {
		double del = node[i].r - node[i].l;
		x = node[i].r;
		if (sgn(del - left * (node[i].v + r)) >= 0) {
			del -= left * (node[i].v + r);
			ret += left + del / (s + node[i].v);
			left = 0;
		} else {
			ret += del / (node[i].v + r);
			left -= del / (node[i].v + r);
		}
	}

	return ret;
}

int main() {
	int T, cas = 1;

	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &T);
	while (T--) {
		top = 0;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		int last = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d%d%d", &node[top].l, &node[top].r, &node[top].v);
			top++;
			if (node[top - 1].l != last) {
				node[top].l = last;
				node[top].r = node[top - 1].l;
				node[top].v = 0;
				top++;
				last = node[top - 2].r;
			} else {
				last = node[top - 1].r;
			}
		}
		if (last != x) {
			node[top].l = last;
			node[top].r = x;
			node[top].v = 0;
			top++;
		}
		sort(node, node + top);
		printf("Case #%d: %.9f\n", cas++, run());
	}

	return 0;
}
