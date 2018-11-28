#include <iomanip>
#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <complex>
#include <cassert>
#include <bitset>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

struct tree {
	double w;
	string f;
	tree *t1,*t2;
	tree(): t1(0),t2(0) {}
	double eval(const set<string>& s) {
		if (t1) {
			if (s.count(f)) return w* (t1->eval(s));
			else return w* (t2->eval(s));
		}
		return w;
	}
};

tree* parse() {
	tree *res = new tree();

	char c;
	cin >> c;
	cin >> res->w;
	cin >> c;
	if (c != ')') {
		cin.unget();
		string s; cin >> s;
		//s = c + s;
		res->f = s;
		res->t1 = parse();
		res->t2 = parse();
		cin >> c;
	}
//	D(res->f);D(res->w)
//	cout << res->f << ' ' << res-> w << endl;
	return res;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int ncas; cin >> ncas;
	forsn(cas,1,ncas+1) {
		cout << "Case #" << cas << ":" << endl;

		int l; cin >> l;
		tree* t = parse();
		scanf("\n");
		int a; cin >> a;

		string s;

		forn(_,a) {
			cin >> s;
			set<string> feat;
			int k; cin >> k;
			forn(__,k) {
				cin >> s;
				feat.insert(s);
			}
			double res = t->eval(feat);
			printf("%0.8lf\n",res);
		}

	}
}
