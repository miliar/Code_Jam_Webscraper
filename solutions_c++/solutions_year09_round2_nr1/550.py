#include <set>
#include <map>
#include <list>
#include <cmath>
#include <queue>
#include <deque>
#include <vector>
#include <bitset>
#include <string>
#include <memory>
#include <cstdio>
#include <cstring>
#include <sstream>
#include <cassert>
#include <iostream>
#include <algorithm>
using namespace std;
#define pb push_back
#define mp make_pair
#define s(c) ((int)((c).size()))
#define all(c) (c).begin(),(c).end()
#define mset(a, v) memset(a, v, sizeof(a))
#define f(i, lo, hi) for (int i = (lo), Max = (hi); i <= Max; ++i)
#define rf(i, hi, lo) for (int i = (hi), Min = (lo); i >= Min; --i)
#define c(i, c) f(i, 0, s(c) - 1)
#define rc(i, c) rf(i, s(c) - 1, 0)
#define it(type, it, c) for (type::iterator it = (c).begin(); it != (c).end(); ++it)
#define rit(type, it, c) for (type::reverse_iterator it = (c).rbegin(); it != (c).rend(); ++it)
typedef vector<int> vint;
typedef long long lint;

typedef set<string> Sstr;
typedef vector<Sstr> VSstr;

struct Node {
	double w;
	string f;
	Node *a, *b;
	Node(double w): w(w) {f = "";};
	Node(double w, string ff, Node* a, Node* b): w(w), a(a), b(b) {f = ff;};
};

string ex;
int a;
VSstr vs;

bool let(char c) {
	return c >= 'a' && c <= 'z';
}

bool dig(char c) {
	return c >= '0' && c <= '9';
}

Node* go(int& i) {
	double w;
	while (!dig(ex[i])) ++i;
	sscanf(&ex[i], "%lf", &w);
	while (ex[i] != ' ' && ex[i] != ')') ++i;
	while (ex[i] == ' ') ++i;
	if (ex[i] == ')') {
		return new Node(w);
	} else {
		char f[32];
		sscanf(&ex[i], "%s", f);
		while (let(ex[i])) ++i;
		while (ex[i] == ' ') ++i;
		Node *a = go(i); ++i;
		while (ex[i] == ' ') ++i;
		Node* b = go(i); ++i;
		while (ex[i] == ' ') ++i;
		return new Node(w, string(f), a, b);
	}
}

double calc(Node* r, int an) {
	if (r->f == "") {
		return r->w;
	} else if (vs[an].count(r->f)) {
		return r->w * calc(r->a, an);
	} else {
		return r->w * calc(r->b, an);
	}
}

void solve(int t) {
	int L, n;
	char b[128];
	scanf("%d\n", &L);
	ex = "";
	f(i, 1, L) {
		gets(b);
		ex += string(b) + " ";
	}
	scanf("%d", &a);
	vs.resize(a + 1, Sstr());
	c(i, vs) vs[i].clear();
	f(i, 1, a) {
		scanf("%s", &b);
		scanf("%d", &n);
		f(j, 1, n) {
			scanf("%s", &b);
			vs[i].insert(string(b));
		}
	}
	int i = 0;
	while (ex[i] == ' ') ++i;
	Node* r = go(i);
	printf("Case #%d:\n", t);
	f(i, 1, a) {
		printf("%.7lf\n", calc(r, i));
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	f(i, 1, t)
	solve(i);
	return 0;
}
