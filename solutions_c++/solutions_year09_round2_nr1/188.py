#define _CRT_SECURE_NO_DEPRECATE

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <memory.h>
#include <string.h>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <bitset>

using namespace std;

#define pb push_back
#define pf push_front
#define mp make_pair
#define fi(a, b) for (i=a; i<=b; i++)
#define fj(a, b) for (j=a; j<=b; j++)
#define fo(a, b) for (o=a; o<=b; o++)
#define fdi(a, b) for (i=a; i>=b; i--)
#define fdj(a, b) for (j=a; j>=b; j--)
#define fdo(a, b) for (o=a; o>=b; o--)
#define ZERO(x) memset(x, 0, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(y))

typedef long long int64;

#define LEN 90000

int t, test;

int l;

struct Node {
	double p;
	string s;
	Node *l, *r;
};

char str[LEN];
int len;

bool ws(char x) {
	if (x == ' ') return true;
	if (x == '\n') return true;
	return false;
}

char Next() {
	char a;
	do {
		a = getchar();
	} while (ws(a));
	return a;
}

Node *root;

Node *Create(int f = 0) {
	double p;
	string s;
	char x[10];
	Node *t;
	if (!f) Next();
	scanf("%lf", &p);
	len = strlen(str);
	t = new Node;
	t->p = p;
	x[0] = Next();
	x[1] = 0;
	if (x[0] == ')') {
		t->s = "";
		t->l = NULL;
		t->r = NULL;
	} else {
		s = x;
		t->l = NULL;
		t->r = NULL;
		while (1) {
			x[0] = Next();
			if (x[0] == ')') break;
			if (x[0] == '(') {
				t->l = Create(1);
				t->r = Create();
				Next();
				break;
			}
			s += x;
		}
		t->s = s;
	}
	return t;
}

int a;
double ans;
int n;

set <string> tree;

double dfs(Node *x) {
	if (x == NULL) return 1;
	if (tree.find(x->s) != tree.end()) {
		return x->p * dfs(x->l);
	} else {
		return x->p * dfs(x->r);
	}
}

int main() {
	int i, j;
#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	scanf("%d", &test);
	for (t=1; t<=test; t++) {
		scanf("%d", &l);
		root = Create();
		scanf("%d", &a);
		printf("Case #%d:\n", t);
		fi(1, a) {
			scanf("%s", str);
			scanf("%d", &n);
			tree.clear();
			fj(1, n) {
				scanf("%s", str);
				tree.insert(str);
			}
			ans = dfs(root);
			printf("%.8lf\n", ans);
		}
	}
	return 0;
}