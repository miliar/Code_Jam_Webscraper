#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <list>
#include <string>
#include <algorithm>

#define FOREACH(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define REP(i, n) for(int i = 0; i < (n); i++)
#define CLEAR(a) memset(a, 0, sizeof(a))

using namespace std;

const int maxp = 10;
const int INF = -999999999;

struct node {
  node *left, *right;
  int m, c, d;
  int a[maxp];
};

int p;

void f(node *x) {
  if (x->d < p-1) {
    f(x->right);
    f(x->left);
    REP(k, x->d+1) {
      int t1 = max(x->left->a[k] + x->right->a[k], INF);
      int t2 = max(x->c + x->left->a[k+1] + x->right->a[k+1], INF);
      x->a[k] = max(t1, t2);
    }
  }
  else {
    REP(k, x->m)
      x->a[k] = x->c;
    x->a[x->m] = 0;
    for (int k = x->m+1; k < p; k++)
      x->a[k] = INF;
  }
}

int main() {
  int T;
  cin >> T;
  for (int C = 1; C <= T; C++) {
    cin >> p;
    list<node *> q;
    int s = 0;
    for (int k = p; k >= 0; k--)
      REP(i, 1<<k) {
	node *n = new node;
	n->d = k;
	if (k < p) {
	  n->left = q.front();
	  q.pop_front();
	  n->right = q.front();
	  q.pop_front();
	  n->m = min(n->left->m, n->right->m);
	  cin >> n->c;
	  s += n->c;
	}
	else {
	  n->left = n->right = NULL;
	  cin >> n->m;
	}
	q.push_back(n);
      }
    node *r = q.front();
    f(r);
    cout << "Case #" << C << ": " << s - r->a[0] << endl;
  }
}
