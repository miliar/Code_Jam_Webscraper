#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define _ << ", " <<
#define db(x) cerr << #x " == " << x << endl

int n, w, l, r[1111];

typedef pair<int,int> pii;
#define F first
#define S second
int caso = 1;

pii ent[1111];
int volta[1111];


int x[1111], y[1111];
int go(int a, int b1, int b2, int d1 = 0, int d2 = 0) {
	if( a == n ) return a;
	if( b1 < 0 ) return a;
	
	x[a] = d1, y[a] = d2;
	int nb1 = b1 - 2*r[a];
	int nb2 = b2 - 2*r[a];
	
	int q = go(a+1, nb1, 2*r[a], d1 + 2*r[a], d2);
	return go(q, b1, nb2, d1, d2+2*r[a]);
}

bool read() {
	printf("Case #%d:", caso++);
	
	cin >> n >> w >> l;
	fr(i,0,n) cin >> r[i], ent[i].F = r[i], ent[i].S = i;
	
	bool inv = false;
	if( l < w ) swap(l,w), inv = true;
	sort(ent,ent+n);
	reverse(ent,ent+n);
	fr(i,0,n) r[i] = ent[i].F;
	
	fr(i,0,n) volta[ ent[i].S ] = i;
	
	int Q = go(0, w,l);
	
	//cerr << Q << " " << n << endl;
	
	if( inv ) fr(i,0,n) printf(" %d.0 %d.0", y[volta[i]], x[volta[i]]);
	else fr(i,0,n) printf(" %d.0 %d.0", x[volta[i]], y[volta[i]]);
	puts("");
	
	return true;
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}

