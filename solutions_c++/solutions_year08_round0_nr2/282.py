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

pii readh() {
	int a,b;
	pii res;
	scanf("%d:%d",&a,&b);
	res.first = a * 60 + b;
	scanf("%d:%d\n",&a,&b);
	res.second = a * 60 + b;
	return res;
}

int t,na,nb;
vector<pii> at, bt;


void join(vector<pii>& a, vector<pii>& b, int& cnt) {
	forn(i,si(a))
		forn(j,si(b)) if (a[i].second + t <= b[j].first) {
			b[j].first = -1;
			cnt--;
			break;
		}
}

void init() {
	ids.clear();
	at.clear();
	bt.clear();
}


int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	int _t; cin >> _t;
	forsn(cas,1,_t+1) {
		init();
		cin >> t;
		cin >> na >> nb;
		forn(_,na) at.pb(readh());
		forn(_,nb) bt.pb(readh());

		sort(all(at)); sort(all(bt));

		join(at,bt,nb);
		join(bt,at,na);

		cout << "Case #" << cas << ": " << na << ' ' << nb << endl;

	}
	return 0;
}

