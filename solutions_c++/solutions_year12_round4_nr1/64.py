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

#define MAXN 10000

struct vine {
	int d, l ; 
	int power;
};

int N, D;
vine v[MAXN];

void input() {
	scanf ( "%d", &N ); 
	for ( int i=0;i<N;++i ) {
		scanf ( "%d%d", &v[i].d, &v[i].l );
		v[i].power = 0 ;
	}
	scanf ( "%d", &D ) ;
}

bool solv() {
	v[0].power = v[0].d ;
	for ( int i=0;i<N;++i ) {
		int limit = v[i].d + v[i].power ;
		if ( limit >= D ) return true;
		for ( int j=i+1;v[j].d<=limit; ++j ) {
			int dd = v[j].d-v[i].d;
			int newpower = (v[j].l>=dd?dd:v[j].l);
			if ( newpower > v[j].power ) v[j].power = newpower ;
		}
	}
	return false ;
}

int main()
{
	int nCase=1, T;
	
	cin >> T;
	while ( T-- ) {
		input();
		printf ( "Case #%d: %s\n", nCase++, (solv()?"YES":"NO") )  ;
	}
	
	return 0;
}
