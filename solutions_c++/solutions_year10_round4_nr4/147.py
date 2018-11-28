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
#include <cstring>
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

#define sqr(a) (a*a)

typedef double tipo;

const tipo pi = 2*acos(0.0);

struct pt {
	tipo x;
	tipo y;
};

tipo operator*(pt a, pt b) {
	return a.x*b.x + a.y*b.y;
}

tipo dd(pt a, pt b) {
	return sqrt( (a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y) );
}

tipo norm(pt a) {
	pt origen;
	origen.x = 0.0, origen.y = 0.0;
	return dd(origen,a);
}

tipo ang(pt p, pt a, pt b) {
	pt u,v;
	u.x = p.x-a.x, u.y = p.y-a.y;
	v.x = b.x-a.x, v.y = b.y-a.y;
	if (norm(u) == 0 || norm(v)==0) return pi/2;
	return acos(u*v/(norm(u)*norm(v)) );
}

tipo cuenta(tipo r, tipo alfa) {
	return pi*r*r*(alfa/(2*pi)) - r*r*0.5*sin(alfa);
}


int main () {
	freopen("D.in","r",stdin);
	freopen("D.out","w",stdout);

	int T; cin >> T;
	forn(rep,T) {
		int n,m; cin >> n >> m;

		pt a, b, p;
		cin >> a.x >> a.y >> b.x >> b.y;
//		cout << a.x << " " << a.y << " " << b.x << " " << b.y << endl;
		cout << "Case #" << rep+1 << ":";
		forn(i,m) {
			cin >> p.x >> p.y;
			double ra = dd(a,p), rb = dd(b,p);
			double alfa = ang(p,a,b), beta = ang(p,b,a);
//			cout << dd(p,a) << endl;
//			cout << endl << ra << " " << rb <<" " << alfa << " " << beta << endl;
			double res = cuenta(ra,2*ang(p,a,b)) + cuenta(rb,2*ang(p,b,a));
			printf(" %.7f",res);
		}
		cout << endl;
	}
	return 0;
}
