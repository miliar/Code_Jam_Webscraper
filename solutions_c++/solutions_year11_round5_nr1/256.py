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
#include <cstring>
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
#define D(a) cerr << #a << "=" << a << endl;
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
typedef pair<double,double> pdd;
typedef vector<pdd> vpdd;

const double EPS = 1e-10;

int w;
vpdd l,u;

double area(const vpdd& a, double x) {
	double res = 0;
	int n = si(a),i;
	for(i = 0; i < n-1 && a[i+1].first <= x; i++)
		res += ((a[i].second + a[i+1].second) / 2.0) * (a[i+1].first - a[i].first);

	if (i < n-1) {
		double distx = a[i+1].first - a[i].first;
		double hx = a[i].second * (a[i+1].first - x) / distx + a[i+1].second * (x - a[i].first) / distx;
		res += ((a[i].second + hx) / 2.0) * (x - a[i].first);
	}

	return res;
}

double area(double x) { return area(u,x) - area(l,x); }

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    cout << setprecision(10) << fixed;

    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ":" << endl;;
    	int nl,nu,g; cin >> w >> nl >> nu >> g;
    	l.clear(); forn(_,nl)  { double x,y; cin >> x >> y; l.pb(mp(x,y)); }
    	u.clear(); forn(_,nu)  { double x,y; cin >> x >> y; u.pb(mp(x,y)); }

    	double ar = area(w);
    	forsn(i,1,g) {
    		double target = (ar/g) * i;
    		double lo = 0, hi = w;
    		while (fabs(lo - hi) > EPS) {
    			double mi = (lo + hi) / 2;
    			if (area(mi) > target - EPS) hi = mi; else lo = mi;
    		}
    		cout << lo << endl;
    	}



    }
}
