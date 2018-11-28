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

const int MAXN = 1000000 + 100;

vt primes;
bool prime[MAXN];

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    fill(prime,prime+MAXN,true); prime[0] = prime[1] = false;
    for (tint i = 2; i < MAXN; i++) if (prime[i]) {
    	primes.pb(i);
    	for (tint j = 2*i; j < MAXN; j += i) prime[j] = false;
    }

    int ncas; cin >> ncas;
    forn(cas,ncas) {    	
    	cout << "Case #" << cas+1 << ": ";
    	int n; cin >> n;
    	if (n == 1) { cout << 0 << endl; continue; }

    	tint res = 0;
    	forn(i,si(primes)) {
    		int p = primes[i];
    		if (p*p > n) break;
    		tint cnt = 0, pot = 1;
    		for (;;) {
    			if (pot * p <= n) {
    				cnt++; pot *= p;
    			}
    			else break;
    		}
    		res += cnt-1;
    	}
    	cout << res+1 << endl;
    }
}
