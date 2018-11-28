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
typedef pair<tint,tint> pii;

const double PHI = (1.0 + sqrt(5.0)) / 2.0;

pii inter(pii a, pii b) {
	pii res(max(a.first,b.first),min(a.second,b.second));
	res.second = max(res.second,res.first-1);
	return res;
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int ncas; cin >> ncas;
    forn(cas,ncas) {
    	cout << "Case #" << cas+1 << ": ";
    	tint a1,a2,b1,b2;
		cin >> a1 >> a2 >> b1 >> b2;
		tint res = 0;
		forsn(a,a1,a2+1) {
			res += (b2-b1+1);
			tint c1 = (int)round(ceil(a/PHI)), c2 = (int)round(floor(a*PHI));
			pii bad = inter(mp(b1,b2),mp(c1,c2));
			res -= (bad.second-bad.first+1);
		}
		cout << res << endl;
	}
    return 0;
}
