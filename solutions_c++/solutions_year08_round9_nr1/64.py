#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:64000000")

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<bool> vb;
typedef double D;

template<class T> T sqr(T x) { return x * x;            }
template<class T> T abs(T x) { return (x > 0) ? x : -x; }

struct P {
	D x, y;

	P() {}
	P(D x, D y): x(x), y(y) {}

	P operator + (P a) { return P(x + a.x, y + a.y); }
	P operator - (P a) { return P(x - a.x, y - a.y); }
	P operator * (D a) { return P(x * a, y * a); }
	D operator * (P a) { return x * a.y - y * a.x;   }
	D operator ^ (P a) { return x * a.x + y * a.y;   }

	D len2() { return sqr(x) + sqr(y); }
	D len()  { return sqrt(len2());    }
	P orth() { return P(y, -x);        }
};

struct L {
	D a, b, c;

	L() {}
	L(D a, D b, D c): a(a), b(b), c(c) {}
	L(P p1, P p2) {
		a = p1.y - p2.y;
		b = p2.x - p1.x;
		c = -p1.x * a - p1.y * b;
	}
};

struct C {
	P c;
	D r;

	C() {}
	C(P c, D r): c(c), r(r) {}
};

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)((x).size()))

struct Node {
	int x;
	int y;
	int am;
	Node *l, *r;
};

int getam(Node *node) {
	if (!node) return 0;
	return node->am;
}

void recalc(Node *node) {
	if (!node) return;
	node->am = getam(node->l) + getam(node->r) + 1;
}

typedef Node *PNode;

void split(PNode node, int x, PNode &l, PNode &r) {
	if (!node) l = r = NULL;
	else if (x < node->x) {
		split(node->l, x, l, node->l);
		r = node;
	}
	else {
		split(node->r, x, node->r, r);
		l = node;
	}
	recalc(l);
	recalc(r);
}

void insert(PNode &node, int x, int y) {
	if (!node || y > node->y) {
		Node *tmp = new Node;
		tmp->x = x;
		tmp->y = y;
		split(node, x, tmp->l, tmp->r);
		node = tmp;
	}
	else if (x < node->x) insert(node->l, x, y);
	else insert(node->r, x, y);
	recalc(node);
}

int n;
int al[6000], be[6000], ga[6000];
int ind1[6000], ind2[6000];

bool cmp1(int p, int q) {
	return al[p] < al[q];
}

bool cmp2(int p, int q) {
	return be[p] < be[q];
}

struct cmp3 {

bool operator()(int p, int q) const {
	return mp(ga[p], p) < mp(ga[q], q);
}
};

void release(PNode node) {
	if (!node) return;
	release(node->l);
	release(node->r);
	delete node;
}

int query(PNode node, int tmp) {
	if (!node) return 0;
	int res = 0;
	if (tmp <= node->x) res = query(node->l, tmp);
	if (tmp == node->x) res++;
	if (tmp > node->x) res = getam(node->l) + 1 + query(node->r, tmp);
	return res;
}

void solve(int it) {
	fprintf(stderr, "Test %d:\n", it);
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> al[i] >> be[i] >> ga[i];
		ind1[i] = i;
		ind2[i] = i;
	}
	sort(ind1, ind1 + n, cmp1);
	sort(ind2, ind2 + n, cmp2);
	int opt = 0;
	for (int i = 0; i < n; i++) {
		if (i % 500 == 0) fprintf(stderr, "%d\n", i);
		Node *root = NULL;
		for (int j = 0; j < n; j++) {
			if (al[ind2[j]] > al[ind1[i]]) continue;
			if (al[ind1[i]] + be[ind2[j]] > 10000) break;
			insert(root, ga[ind2[j]], rand());
			int cur = query(root, 10000 - al[ind1[i]] - be[ind2[j]]);
			opt = max(opt, cur);
		}
		release(root);
	}
	printf("Case #%d: %d\n", it, opt);
}

int main() {
	srand(0xdead);
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nt;
	cin >> nt;
	for (int it = 1; it <= nt; it++) {
		solve(it);
	}
	return 0;
}
