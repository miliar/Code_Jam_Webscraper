#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <map>

using namespace std;

string readLine() {
	char sz[1000];
	fgets(sz, 1000, stdin);
	int l = strlen(sz);
	if (sz[l-1] == '\n') sz[l-1] = 0;
	return sz;
}

int readIntLine() {
	string s = readLine();
	return atoi(s.c_str());
}

vector<int> readVI() {
	int n;
	scanf("%d ", &n);
	vector<int> v(n);
	for (int i = 0; i < n; i++) scanf("%d ", &v[i]);
	return v;
}

class Tree {
public:
	void st(int i) { g = -1, v = i, a = NULL, b = NULL; }
	void st(int G, int C, Tree *x, Tree *y) {
		g = G;
		c = C;
		a = x;
		b = y;
		if (g) v = a->v && b->v;
		else v = a->v || b->v;
	}

	int force(int n) {
		if (n == v) return 0;
		if (g < 0) return 1000000;
		if (n) {
			if (g) {
				if (c) {
					if (a->v || b->v) return 1;
					return min(a->force(1), b->force(1))+1;
				} else {
					int ct = 0;
					if (!a->v) ct += a->force(1);
					if (!b->v) ct += b->force(1);
					return ct;
				}
			} else {
				return min(a->force(1), b->force(1));
			}
		} else {
			if (g) {
				return min(a->force(0), b->force(0));
			} else {
				if (c) {
					if (!a->v || !b->v) return 1;
					return min(a->force(0), b->force(0))+1;
				} else {
					int ct = 0;
					if (a->v) ct += a->force(0);
					if (b->v) ct += b->force(0);
					return ct;
				}
			}
		}
		return 10000000;
	}

	int g, c, v;
	Tree *a;
	Tree *b;
};

long long solveIt(int V, vector<int> &g, vector<int> &c, vector<int> &v) {
	vector<Tree> t(g.size()+v.size());

	for (int i = 0; i < v.size(); i++) t[i+g.size()].st(v[i]);
	for (int i = g.size()-1; i >= 0; i--) {
		int c2 = (i+1)*2, c1 = c2-1;
		t[i].st(g[i], c[i], &t[c1], &t[c2]);
	}

	return t[0].force(V);
}

int main() {
	int N = readIntLine();
	for (int cn = 1; cn <= N; cn++) {
		int M, V, m12;
		scanf("%d %d ", &M, &V);
		m12 = (M-1)/2;

		vector<int> g(m12), c(m12), v(m12+1);

		for (int i = 0; i < m12; i++) scanf("%d %d ", &g[i], &c[i]);
		for (int i = 0; i <= m12; i++) scanf("%d ", &v[i]);

		long long res = solveIt(V, g, c, v);

		if (res >= 1000000)
			printf("Case #%d: IMPOSSIBLE\n", cn);
		else
			printf("Case #%d: %lld\n", cn, res);
	}
	return 0;
}

