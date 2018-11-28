#include <algorithm>
#include <numeric>
#include <fstream>
#include <iostream>
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
#define all(c) (c).begin(), (c).end()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> pii;

map<string, map<string, int> > ids;
int id(string cat, string s) {
	map<string,int>& m = ids[cat];
	if (m.count(s) == 0) m[s] = si(m)-1;
	return m[s];
}


set<string> s, tmp;

void init() {
	ids.clear();
	s.clear();
	tmp.clear();
}



int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int t; cin >> t;
	forsn(cas,1,t+1) {
		init();
		int ns; scanf("%d\n",&ns);
		forn(_,ns) {
			string x;
			getline(cin,x);
			s.insert(x);
		}

		int nq; scanf("%d\n",&nq);
		int res = 0;
		forn(_,nq) {
			string x; getline(cin,x);
			if (s.count(x) && !(tmp.count(x))) tmp.insert(x);
			if (si(tmp) == ns) {
				res++;
				tmp.clear(); tmp.insert(x);
			}
		}
		cout << "Case #" << cas << ": " << res << endl;
	}
	return 0;
}

