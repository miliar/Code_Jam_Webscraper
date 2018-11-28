#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <sstream>

#include <cassert>
#include <cmath>
#include <ctime>

#include <map>
#include <set>
#include <bitset>
#include <queue>

using namespace std;

typedef long long int64;

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define all(a) a.begin(), a.end()

const int INF = INT_MAX >> 1;
const double PI = 3.1415926535897932384626433832795;
const double EPS = 1E-8;

struct vertex {
	double prob;
	vertex *l, *r;
	string feature;
};

vector<string> a;
int p;
vertex *root;
set<string> props;

vertex *parse() {
	vertex *ans = new vertex();
	ans->l = ans->r = NULL;
	++p;
	sscanf(a[p++].c_str(), "%lf", &ans->prob);
	if (p < (int)a.size() && a[p] != ")") {
		ans->feature = a[p++];
		ans->l = parse();
		ans->r = parse();
	}
	++p;
	return ans;
}

double go(vertex *v) {
	if (!v->l) return v->prob;
	if (props.count(v->feature)) return v->prob * go(v->l);
	else return v->prob * go(v->r);
}

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int tk;
	scanf("%d\n", &tk);

	for(int tc = 1; tc <= tk; ++tc) {
		printf("Case #%d:\n", tc);

		int L;
		scanf("%d\n", &L);
		string c;
		stringstream S;
		forn(i, L) {
			getline(cin, c);
			forn(j, c.length())
				if (c[j] == '(' || c[j] == ')') S << ' ' << c[j] << ' ';
				else S << c[j];
		}

		a.clear();
		while (S >> c) a.pb(c);
		p = 0;
		
		root = parse();

		int m;
		scanf("%d\n", &m);
		while (m --> 0) {
			cin >> c;
			int k;
			cin >> k;
			props.clear();
			while (k --> 0) {
				cin >> c;
				props.insert(c);
			}
			printf("%.10lf\n", go(root));
		}
	}

	return 0;
}
