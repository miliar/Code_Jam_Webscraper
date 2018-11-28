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
#include <cmath>
#include <cstring>
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


#define MAX 1001000

bool criba[MAX];
vector<tint> p;

tint t,n;

void fillcriba() {
	memset(criba,true,sizeof(criba));
	criba[0] = criba[1] = false;
	for(tint q = 2; q<MAX; q++) if (criba[q]) {
		p.pb(q);
		for(tint k = 2*q; k<MAX; k+=q) criba[k] = false;	
	}
}

int main () {
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	fillcriba();
	
	cin >> t;
	forn(rep,t) {
		cin >> n;	
		int ans = 0;
		if (n>1) {
			ans++;
			for(int i = 0; i<si(p) && p[i]*p[i]<= n; i++) {
				tint q = p[i]*p[i];	
				while(q<=n) {
					q*=p[i];
					ans++;
				}
			}
		}
		
		cout << "Case #" << rep+1 << ": " << ans << endl;
		
	}
	return 0;
}
