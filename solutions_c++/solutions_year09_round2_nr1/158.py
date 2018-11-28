#include <cstdio>
#include <algorithm>
#include <string>
using namespace std;

#define For(i,n) for (int i = 0; i < n; ++i)

int T, n, k;
char t[256];
string fea[100];

struct tree {
	double w;
	string s;
	tree *l, *r;
	tree() { w = 0, l = r = 0; }
	tree(double w, tree *l, tree *r) : w(w), l(l), r(r) {}
	~tree() { if (l) delete l; if (r) delete r; }
};

tree *buildtree() {
	char c;
	while ((c = getchar()) != '(' && c != ')');
	if (c == ')') return 0;
	tree *r = new tree();
	char t[16];
	scanf("%lf", &(r -> w));
	while ((c = getchar()) != ')' && !('a' <= c && c <= 'z'));
	if (c == ')') return r;
	for (int i = 0; 'a' <= c && c <= 'z'; ++i) {
		t[i] = c; t[i + 1] = 0; c = getchar();
	}
	r -> s = string(t);
	r -> l = buildtree();
	r -> r = buildtree();
	while ((c = getchar()) != ')');
	return r;
}

tree *root;

double pro(tree *r) {
	if (!(r -> l)) return r -> w;
	if (*lower_bound(fea, fea + k, r -> s) == r -> s)
		return (r -> w)*pro(r -> l);
	return (r -> w)*pro(r -> r);
}

int main() {
	scanf("%d", &T);
	For(r,T) {
		printf("Case #%d:\n", r + 1);
		scanf("%*d");
		root = buildtree();
		scanf("%d", &n);
		For(i,n) {
			scanf("%*s%d", &k);
			For(j,k) scanf("%s", t), fea[j] = string(t);
			sort(fea, fea + k);
			fea[k] = string("");
			printf("%.8lf\n", pro(root));
		}
		delete root;
	}
	return 0;
}
