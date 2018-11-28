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
typedef long double tipo;

#define MAX 256
const tipo EPS = 1.0E-7;

int t, w, L, U, g;
tipo lx[MAX], ly[MAX], ux[MAX], uy[MAX], cut[MAX], area;
vector<pair<tipo,int> > v;

tipo cuenta(tipo s, tipo e, int l, int u) {

	if (l >= L-1)	l = L-2;
	if (u >= U-1) u = U-2;
	
	tipo a1, b1, x1,y1,x2,y2, a2,b2;
	x1 = lx[l], y1 = ly[l], x2 = lx[l+1], y2 = ly[l+1];
	a1 = (y2-y1)/(x2-x1); b1 = y2-a1*x2;
	
	x1 = ux[u], y1 = uy[u], x2 = ux[u+1], y2 = uy[u+1];
	a2 = (y2-y1)/(x2-x1); b2 = y2-a2*x2;
//		cout << s << " " << e << " " << l << " " << u <<  " ";
	//	cout << a1 << " " << b1 << " " <<a2 << " "  << b2 << " " << 0.5*( (s*(a2-a1) + b2-b1) + (e*(a2-a1) + b2-b1) )*(e-s) << endl;
	return 0.5*( (s*(a2-a1) + b2-b1) + (e*(a2-a1) + b2-b1) )*(e-s);
}

tipo calc(tipo e) {
	tipo res = 0.0;
	int i =2;
	int l=0, u=0;
	while(v[i].first<e-EPS) {
	//	cout << cuenta(v[i-1].first,v[i].first,l,u) << endl;
		res += cuenta(v[i-1].first,v[i].first,l,u);
		if (v[i].second == 0) l++;
		else u++;	
		i++;
	}
//	cout << cuenta(v[i-1].first,e,l,u) << endl;
	res += cuenta(v[i-1].first,e,l,u);
	return res;
}

tipo calc(tipo s, tipo e) { return calc(e)-calc(s);}

void init() {
	v.clear();	
	cut[0] = 0.0;
	
}

int main () {
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	cin >> t;
	forn(rep,t) {
		cin >> w >> L >> U >> g;
		init();
		
		forn(i,L) {
			cin >> lx[i] >> ly[i];
			v.pb(mp(lx[i],0));	
		}
		forn(i,U) {
			cin >> ux[i] >> uy[i];
			v.pb(mp(ux[i],1));	
		}
		
		sort(all(v));
		
		area = calc(0,w);
	//	cout << area << endl;
		
		forn(i,g-1) {
			tipo st = cut[i], end = w, mid = 0.5*(st+end);
			while(end-st > EPS) {
				mid = 0.5*(st+end);
				tipo a = calc(cut[i],mid);
				if (a>area/g) end = mid;
				else st = mid;	
			}
			cut[i+1] = mid;
		}
		cout << "Case #" << rep+1<< ":" << endl;
		forsn(i,1,g) printf("%.8lf\n",(double)cut[i]);
	}
	return 0;
}
