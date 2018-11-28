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

int n;
vi but[2], turn;

void init() {
	forn(i,2) but[i].clear();
	turn.clear();
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ": ";
    	init();

    	cin >> n;
    	forn(i,n) {
    		char c; int p; cin >> c >> p;
    		int r = (c == 'O' ? 0 : 1);
    		turn.pb(r);
    		but[r].pb(p);
    	}

    	int pos[2] = {1,1}, ind[2] = {0,0}, t = 0;
    	bool moved[2];

    	int res = 0;
    	while (t < n) {
    		// check for moves
    		forn(i,2) {
				moved[i] = pos[i] != but[i][ind[i]];
				if (moved[i]) {
					if (pos[i] < but[i][ind[i]]) pos[i]++;
					else pos[i]--;
	    		}
    		}

    		int r = turn[t];
    		if (pos[r] == but[r][ind[r]] && !moved[r]) {
    			ind[r]++;
    			t++;
    		}

    		res++;
    	}
    	cout << res << endl;

    }
}
