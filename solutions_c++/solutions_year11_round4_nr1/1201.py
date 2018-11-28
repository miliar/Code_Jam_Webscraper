#include <bits/stdc++.h>

#define _ << ", " <<
#define db(x) cout << #x " == " << x << endl
#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define rep(i,n) for( int i = 0 ; i < n ; ++i )

using namespace std;

int x, s, r, n;
double t;
typedef pair<int,int> pii;
typedef pair<pii,int> ppi;

#define F first
#define S second
ppi ww[2000];

bool comp(const ppi & a, const ppi & b) {
	return a.S < b.S;
}

bool read() {
	
	cin >> x >> s >> r >> t >> n;
	rep(i,n) cin>> ww[i].F.F >> ww[i].F.S >> ww[i].S, ww[i].S += s;
	int delta = r-s;
	
	sort(ww,ww+n);
	int tt = n;
	if( ww[0].F.F > 0 ) ww[tt++] = ppi(pii(0,ww[0].F.F), s);
	if( ww[n-1].F.S < x ) ww[tt++] = ppi(pii(ww[n-1].F.S,x), s);
	
	fr(i,1,n) {
		if( ww[i].F.F > ww[i-1].F.S ) ww[tt++] = ppi(pii(ww[i-1].F.S,ww[i].F.F), s);
	}
	sort(ww,ww+tt, comp);
	
	double res = 0.0;
	rep(i,tt) {
		//if( t > 0 ) {
			double tempo = (ww[i].F.S-ww[i].F.F)/(double)(ww[i].S+delta);
			double dim = min(t,tempo);
			t -= dim;
			
			double dist2 = ww[i].F.S-ww[i].F.F;
			double dist1 = (ww[i].S+delta)*dim;
			dist2 -= dist1;
			res += dim + dist2/ww[i].S;
			/*if( t > 0 ) ww[i].S += delta;
			else {
				double dist2 = ww[i].F.S-ww[i].F.F;
				double dist1 = (ww[i].S+delta)*dim;
				dist2 -= dist1;
				ww[i].F.F = 0;
				ww[i].F.S = 0;
				res += dim + dist2/ww[i].S;
				ww[i].S = 1;
			}*/
		//} else break;
	}
	//rep(i,tt) res += (ww[i].F.S-ww[i].F.F)/(double)ww[i].S;
	
	static int caso = 1;
	printf("Case #%d: %.8lf\n", caso++, res);
	
	return true;
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}
