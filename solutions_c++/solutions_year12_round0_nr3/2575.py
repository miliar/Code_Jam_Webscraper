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

const int MAXN = 2000000 + 100;

int pot10(int x) {
	int res = 1;
	while (res <= x) res *= 10;
	return res / 10;
}


int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ": ";
    	int a,b; cin >> a >> b;

    	set<pii> res;
    	forsn(x,a,b) {
    		int p1 = pot10(x), p2 = 10;
    		while (p1 >= 10) {
    			int nx = (x % p2) * p1 + x / p2;
    			if (x < nx && nx <= b) res.insert(mp(x,nx));
    			p1 /= 10; p2 *= 10;
    		}
    	}
    	cout << si(res) << endl;
    }
}
