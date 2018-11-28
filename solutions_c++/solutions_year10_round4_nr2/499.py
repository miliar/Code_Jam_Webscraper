/* Rajat Goel (C++) */
#include <algorithm>
#include <iostream>
#include <iterator>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <cstdio>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;
typedef pair<int,int>  pii;
typedef long long      LL;
typedef long double    LD;
const int    INF =     INT_MAX/2-1;
const LL    LINF =     LLONG_MAX/2-1;
const LD     EPS =     1e-7;
#define loop(i, n)     for (int i = 0; i < int(n); ++i)
#define foreach(i, a)  for (typeof((a).begin()) i = (a).begin();i != (a).end(); ++i)
inline int fCMP(LD x, LD y = 0, LD tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

vector<int> M;

struct tree {
	LL cost, start, end;
	struct tree *left, *right;
};

tree* newTree(LL x) {
	tree* tmp = new tree();
	tmp->start = tmp->end = x;
	tmp->left = tmp->right = NULL;
	tmp->cost = 0;
	return tmp;
}

void freeTree(tree* root) {
	if (!root) return;

	freeTree(root->left);
	freeTree(root->right);
	delete root;
}

tree* makeTree(LL c, tree* l, tree* r) {
	tree* tmp = new tree();
	tmp->start = l->start;
	tmp->end = r->end;
	tmp->cost = c;
	tmp->left = l;
	tmp->right = r;
	return tmp;
}

void printTree(tree* root) {
	if (!root) return;

	printTree(root->left);
	cout << root->start << " " << root->end << " " << root->cost << endl;
	printTree(root->right);
}

map<pair<tree*, int>, LL> dp;

LL getMin(tree* root, int k) {
	if (root->start == root->end) return 0;
	if (dp.find(make_pair(root, k)) != dp.end()) return dp[make_pair(root, k)];

	LL ret = root->cost + getMin(root->left, k) + getMin(root->right, k);

	if (count(M.begin() + root->start, M.begin() + root->end + 1, k) == 0) {
		ret = min(ret, getMin(root->left, k+1) + getMin(root->right, k+1));
	}
	return dp[make_pair(root, k)] = ret;
}

int main(int argc, char *argv[]) {
	int T; scanf(" %d", &T);
	for (int X = 1; X <= T; ++X) {
		dp.clear();

		int P; cin >> P;
		M.resize(1<<P);
		loop (i, 1<<P) cin >> M[i];

		queue<tree*> q;
		loop (i, 1<<P) {
			q.push(newTree(i));
		}

		loop (i, (1<<P)-1) {
			LL fees; cin >> fees;
			tree* l = q.front(); q.pop();
			tree* r = q.front(); q.pop();
			q.push(makeTree(fees, l, r));
		}
		assert(q.size() == 1);
		tree* root = q.front(); q.pop();

		LL res = getMin(root, 0);

		printf("Case #%d: %Ld\n", X, res);
	}
	return 0;
}
