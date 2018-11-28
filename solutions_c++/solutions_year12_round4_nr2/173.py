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
#include <ctime>
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
typedef long double tipo;

#define MAXN 1024
#define mod 1000000
#define EPS 1.0E-3

int T,n;
tint W,L,x[MAXN], y[MAXN],r[MAXN];

tipo dist(tint x1, tint y1, tint x2, tint y2) {
	return sqrt((tipo)((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)));	
	
}

void put(int i) {
	bool puesto = false;
	while(!puesto) {
		tint x0 = ((tint)rand()*(tint)mod + (tint)(rand()%mod))%W;
		tint y0 = ((tint)rand()*(tint)mod + (tint)(rand()%mod))%L;
		bool vale = true;
		forn(j,i) if (dist(x0,y0,x[j],y[j]) < r[i]+r[j]+EPS) {vale = false; break;}
		if (vale) {
			x[i] = x0, y[i] = y0;
			puesto = true;	
		}
	}	
}

bool check() {
	forn(i,n) for(int j = i+1; j<n; j++) {
		if (dist(x[i],y[i],x[j],y[j]) < r[i]+r[j]+EPS) return false;	
	}	
	return true;
}

int main () {
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	srand(time(NULL));
	
	cin >> T;
	
	forn(rep,T) {
		cin >> n >> W >> L;
		forn(i,n) cin >> r[i];
		
		x[0] = 0, y[0] = 0;
		
		forsn(i,1,n) put(i);
		
		cout << "Case #" << rep+1 << ":";
		
		if (!check()) cout << endl << endl << " AS ASDASD ASF AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" << endl << endl;
		
		forn(i,n) cout << " " << x[i] << " " << y[i];
		cout << endl;
	}

	return 0;
}
