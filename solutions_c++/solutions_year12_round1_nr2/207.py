#include <bits/stdc++.h>
using namespace std;

#define db(x) cerr << #x " == " << x << endl
#define _ <<", "<<
#define fr(a,b,c) for( int a = b ; a < c ; ++a )

typedef pair<int,int> pii;
#define F first
#define S second

pii lst[2111];

int caso = 1, n;

int mark[2222], val[2222];

bool read() {
	scanf("%d", &n);
	memset(mark, 0, sizeof mark);
	
	fr(i,0,n) {	
		int a,b;
		scanf("%d%d", &a, &b);
		lst[2*i] = pii(a,-i-1);
		lst[2*i+1] = pii(b, i+1);
		val[i+1] = b;
	}
	int m = n*2;
	
	sort(lst,lst+m);
	
	int est = 0, res = 0, tot = 0;
	
	while( tot != n ) {
		bool ok = false;
		for( int i = 0 ; i < m && lst[i].F <= est ; ++i ) {
			int b = lst[i].S;
			if( b > 0 && mark[b] < 2 ) { 
				res++;
				est += 2-mark[b];
				mark[b] = 2;
				tot++;
				ok = true;
			}
		}
		
		int meo = 0;
		if( !ok ) for( int i = 0 ; i < m && lst[i].F <= est ; ++i ) {
			int b = -lst[i].S;
			if( b > 0 && mark[b] == 0 ) {
				if( !meo || val[meo] < val[b] ) meo = b;
				ok = true;
			}
		}
		
		if( !ok ) break;
		else if( meo ){
			res++;
			est += 1;
			mark[meo] = 1;
		}
	}
	
	if( tot != n ) printf("Case #%d: Too Bad\n", caso++);
	else printf("Case #%d: %d\n", caso++, res);
	
	return true;
}

int main() {
	int t = -1;
	scanf("%d", &t);
	while( t-- && read() );
	return 0;
}
