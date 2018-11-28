// By mirosuaf v.2.1 modified for CodeJam
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(f,w) ({ bool _ok=true; f _ok=_ok && (w); _ok; })
#define EXISTS(f,w) (!ALL(f,!(w)))
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 




VI x,y,r;

double policz(int p1,int p2) {
	double wynik=sqrt(double((x[p1]-x[p2])*(x[p1]-x[p2])+(y[p1]-y[p2])*(y[p1]-y[p2])))+(r[p1]+r[p2]);
	return wynik/2.0;
}

int main() {
	int ile;
	scanf("%d",&ile);
	FOR(iile,1,ile) {
		int n;
		scanf("%d",&n);
		x.clear();
		y.clear();
		r.clear();
		REP(i,n) {
			x.push_back(0);
			y.push_back(0);
			r.push_back(0);
		}

		double wynik=INF;
		REP(i,n) {
			scanf("%d%d%d",&x[i],&y[i],&r[i]);
		}
		if (n==1) wynik=r[0];
		if (n==2) wynik=max(r[0],r[1]);
		if (n==3) {
			wynik=min(wynik,policz(0,1));
			wynik=min(wynik,policz(1,2));
			wynik=min(wynik,policz(0,2));
		}

		printf("Case #%d: %.7f\n",iile,wynik);
	}
	return 0;
}

