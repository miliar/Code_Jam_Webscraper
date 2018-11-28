#include <vector>
#include <queue>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;

/* tipos */
typedef pair<int,int> pint;
typedef long long tint;
typedef unsigned int mint;
typedef unsigned long long mtint;

typedef vector<int> vint;
typedef vector<vint> vvint;

typedef long double tipo;

/* "funciones" */
#define forn(i,n) for(int ___n=n, i=0;i<___n;++i)
#define dforn(i,n) for(int i=(n)-1;i>=0;--i)
#define forsn(i,s,n) for(int ___n=n, i=s;i<___n;++i)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define forall(it,X) for(typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define dforall(it,X) for(typeof((X).rbegin()) it = (X).rbegin(); it != (X).rend(); ++it)
#define all(X) (X).begin(), (X).end()
#define esta(e, c) (c.find(e) != c.end())
#define DBG(a) cerr << #a << " = " << a << endl;

template<class T> string itos(const T&x) { ostringstream o; o<<x; return o.str(); }

string wrd[5050];
char mp[256][15];

tint mcd(tint a, tint b){return (b==0)?a:mcd(b, a%b);}
int solve(tint n, tint pd, tint pg) {
	if (pg==0) return pd==0;
	if (pg==100) return pd==100;
	tint xd = 100 / mcd(100,pd);
	tint xg = 100 / mcd(100,pg);
	tint md = n/xd;
	if (!md) return 0;
	tint ad = pd*xd/100;
	tint ag = pg*xg/100;
	tint bd = (100-pd)*xd/100;
	tint bg = (100-pd)*xd/100;
	return 1;
}

int main() {
	int tt;
	cin >> tt;
	forn(t, tt) {
		tint res;
		tint n, pd, pg; cin >> n >> pd >> pg;
		res = solve(n,pd,pg);
		const char* resp[2] = {"Broken", "Possible"};
		cout << "Case #" << t+1 << ": " << resp[res] << endl;
	}
	return 0;
}

