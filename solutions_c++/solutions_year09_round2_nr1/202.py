#include <algorithm>
#include <cmath>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;

template <class A, class B> void CONV(A& x, B& y) { stringstream s; s << x; s >> y; }
typedef long long LL;
#define FOR(i, a, b) for (int i = a; i < b; ++i)
#define FORE(i, v) FOR(i, 0, v.size())
#define FORU(i, a) for (int i = a; ; ++i)
#define SORT(v) sort(v.begin(), v.end())
#define SET(a, n) memset(a, n, sizeof a)

struct state {
	double p;
	int c;
	state* t, *f;
	
	state(double a = -1, int b = -1) {
		p = a;
		c = b;
		t = f = NULL;
	}
};

bool has[100];
map<string, int> m;
int cnt;

double go(state* root, double p) {
	if (root == NULL) return p;
	p *= root->p;
	if (has[root->c]) return go(root->t, p);
	return go(root->f, p);
}

void get(state* root) {
	while (cin.get() != '(') {}
	cin >> (root->p);
	//cout << (root->p) << endl;
	char c;
	for(;;) {
		c = cin.get();
		if (c == ' ' || c == '\n') continue;
		if (c == ')') return;
		string s(1, c);
		for(;;) {
			c = cin.get();
			if (c == ' ' || c == '\n') break;
			s += c;
		}
/*	string s;
	cin >> s;
	//cout << s << endl;
	if (s[0] != ')') {*/
		if (!m.count(s)) m[s] = cnt++;
		root->c = m[s];
		//cout << s << ' ' << (root->c) << endl;
		root->t = new state();
		get(root->t);
		root->f = new state();
		get(root->f);
		while (cin.get() != ')') {}
		return;
	}
}

int main() {
	int n;
	cin >> n;
	FOR(i, 0, n) {
		int l;
		cin >> l;
		m.clear();
		cnt = 0;
		state* root = new state();
		get(root);
		//cout << (root->p) << ' ' << (root->c) << ' ' << (root->t->p) << ' ' << (root->t->c) << endl;
		cout << "Case #" << i+1 << ":\n";
		int a;
		cin >> a;
		FOR(j, 0, a) {
			string trash;
			int sz;
			cin >> trash >> sz;
			vector<string> v(sz);
			FOR(i, 0, sz) cin >> v[i];
			SET(has, false);
			FORE(i, v) {
				if (m.count(v[i])) has[m[v[i]]] = true;
			}
			cout << fixed << setprecision(7) << go(root, 1) << endl;
		}
	}
}
