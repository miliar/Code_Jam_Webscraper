#include <iostream>
#include <sstream>

#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>

#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define MAXN 1000

int N;
double W, L;
double rs[MAXN] ;

int p[MAXN] ;
double x[MAXN], y[MAXN] ;

void input() {
	cin >> N >> W >> L ;
	for ( int i=0;i<N;++i ) {
		cin >> rs[i] ;
	}

	bool mk[MAXN];
	memset ( mk, false, sizeof mk ) ;

	for ( int i=0;i<N;++i ) {
		int m = -1 ;
		for ( int j=0;j<N;++j ) {
			if ( !mk[j] ) {
				if ( m == -1 ) m = j ;
				else if ( rs[j] > rs[m] ) m = j ;
			}
		}
		
		p[i] = m;
		mk[m] = true;
	}
}

void solv() {
	int Y0 = 0 ;
	int X0 = 0 ;
	int dy = -1 ;
	
	for ( int i=0;i<N;++i ) {
		int r = rs[p[i]] ;
		if ( X0 == 0 ) {
			x[p[i]] = X0, y[p[i]] = Y0 ;
			dy = r ;
			X0 += r ;
		} else if ( X0 + r <= W ) {
			x[p[i]] = X0 + r ;
			y[p[i]] = Y0 ;
			X0 += r*2 ;
		} else {
			Y0 += dy + r ;
			x[p[i]] = 0;
			y[p[i]] = Y0 ;
			X0 = r ;
		}
	}
	
	for ( int i=0;i<N;++i ) {
		if ( x[i] > W || y[i] > L ) cout << "fail" << endl;
		printf ( " %.1f %.1f", x[i], y[i] ) ;
	} printf ( "\n" ) ;
	
}

int main()
{
	int nCase=1, T;
	
	cin >> T;
	while ( T-- ) {
		input();
		printf ( "Case #%d:", nCase++ ) ;
		solv() ;
	}
	
	return 0;
}
