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

#define MAXN 2000

#define H0 500000000

int N ;
int view[MAXN];

int m[MAXN];
int sl[MAXN] ;
int see[MAXN];
int height[MAXN];

void input() {
	cin >> N ;
	for ( int i=0;i<N-1;++i ) { cin >> view[i] ; --view[i]; }
}

bool solv() {
	// memset ( m, 0, sizeof m ) ;
	memset ( see, -1, sizeof see ) ;
	for ( int i=0;i<N;++i ) m[i] = 1; 
	for ( int i=0;i<N-1;++i ) {
		sl[i] = m[i]; 
		if ( see[view[i]] == -1 ) see[view[i]] = i ;
		for ( int j=i+1;j<view[i];++j ) {
			// if ( m[j] > sl[i] ) return false;
			if ( see[j] != -1 ) return false;
			++ m[j] ;
		}
	}
	return true;
}

int limit[MAXN];
void build() {
	for ( int i=0;i<N;++i ) limit[i] = H0 ;
	memset ( height, -1, sizeof height ) ;
	
	for ( int i=N-1;i>=0;--i ) {
		if ( height[i] == -1 ) {
			height[i] = limit[i] ;
		}
		for ( int j=0;j<i;++j ) {
			if ( view[j] == i ) {
				height[j] = height[i] - sl[j]*(i-j);
				for ( int k=j+1;k<i;++k ) {
					limit[k] = min ( limit[k], height[i]+(k-j)-1 ) ;
				}
			} 
		}
	}
}

int main()
{
	int nCase=1, T;
	
	cin >> T;
	while ( T-- ) {
		input();
		printf ( "Case #%d:", nCase++ ) ;
		if ( !solv() ) printf ( " Impossible\n" ) ;
		else {
			build();
			for ( int i=0;i<N;++i ) {
				printf ( " %d", height[i] );
			} printf ( "\n" ) ;
		}
	}
	
	return 0;
}
