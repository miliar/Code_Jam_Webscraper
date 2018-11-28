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

const double EPS = 1e-10;


vector<pair<double,double> > c;
int s,r,n;
double t;


int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    cout << setprecision(10);

    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	c.clear();

    	cout << "Case #" << cas+1 << ": ";
    	int x;
    	cin >> x >> s >> r >> t >> n;
    	forn(_,n) {
    		int b,e,w; cin >> b >> e >> w;
    		int l = e-b;
    		c.pb(mp(w,l));
    		x -= l;
    	}
    	c.pb(mp(0,x));
    	sort(all(c));

    	double res = 0;
    	forn(i,si(c)) {
    		if (t == 0) break;
    		double wi = c[i].first, li = c[i].second;
    		if (t * (r + wi) > (li - EPS)) {
    			double run = li / double(r + wi);
    			res += run; t -= run; c[i].second = 0;
    		}
    		else {
    			double run = t;
    			res += run; t = 0; c[i].second -= run * (r + wi);
    		}
    	}

    	forn(i,si(c)) {
			double wi = c[i].first, li = c[i].second;
			res += li / double(s + wi);
    	}

    	cout << res << endl;
    }
}
