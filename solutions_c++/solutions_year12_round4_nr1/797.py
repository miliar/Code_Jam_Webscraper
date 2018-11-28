#include <bits/stdc++.h>
using namespace std;

#define fr(a,b,c) for( int a = b ; a < c ; ++a )
#define _ << ", " <<
#define db(x) cerr << #x " == " << x << endl

int n, d[1<<20], l[1<<20], D;

typedef pair<int,int> pii;
#define F first
#define S second

int vai[1<<18];
priority_queue<pii> heap;

int caso = 1;
bool read() {
	printf("Case #%d: ", caso++);
	cin >> n;
	
	fr(i,0,n) cin >> d[i] >> l[i];
	cin >> D;
	
	/*
	int x = 0, y = d[i];
	
	while( x < n ) {
		if( y >= D-d[x] ) {
			puts("YES");
			return true;
		}
		if( x == n-1 ) x = n;
		int w = upper_bound(d,d
	}
	puts("NO");
	
	return true;*/
	memset(vai,0,sizeof vai);
	
	vai[0] = d[0];
	heap.push( pii(d[0], 0) );
	
	while( !heap.empty() ) {
		pii at = heap.top();
		heap.pop();
		int x = at.S, y = at.F;
		if( vai[x] != y ) continue;
		if( at.F >= D-d[at.S] ) {
			puts("YES");
			return true;
		}
		
		for( int i = x+1 ; i < n ; ++i ) {
			int w = d[i]-d[x];
			if( y < w ) break;
			w = min(l[i], w);
			if( vai[i] >= w ) continue;
			vai[i] = w;
			heap.push( pii(w,i) );
		}
	}
	puts("NO");
	
	cerr << ".";
	
	return true;
}

int main() {
	int t = -1;
	cin >> t;
	while( t-- && read() );
	return 0;
}

