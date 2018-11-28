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

const int MAXN = 1000 + 100;

tint r,k,n,g[MAXN];
tint take[MAXN], next[MAXN];
tint lastr[MAXN], lastp[MAXN];

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int ncas; cin >> ncas;
    forn(cas,ncas) {
    	cout << "Case #" << cas+1 << ": ";
    	cin >> r >> k >> n;
    	forn(i,n) cin >> g[i];

    	tint i = 0, j = 0, ak = k - g[n-1];
    	while (i < n) {
    		ak += g[(i+n-1)%n];
    		while (g[j] <= ak) {
    			ak -= g[j]; j = (j+1) % n;
    			if (j == i) break;
    		}
    		take[i] = k - ak;
    		next[i] = j;
    		i++;
    	}

    	bool lastones = false;
    	tint res = 0; i = 0;
    	fill(lastr,lastr+n,-1);
    	while (r) {
    		if (lastr[i] == -1 || lastones) {
    			lastr[i] = r;
    			lastp[i] = res;

				res += take[i];
				i = next[i];
				r--;
    		}
    		else {
    			tint len = lastr[i]-r, prof = res - lastp[i];
    			res += (r/len) * prof;
    			r %= len;
    			lastones = true;
    		}
    	}

    	cout << res << endl;
	}
    return 0;
}
