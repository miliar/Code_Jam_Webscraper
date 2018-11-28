#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int UF[1001];

int find(int x) {
	if( UF[x]>0 ) {
		return UF[x] = find( UF[x] );
	} else {
		return x;
	}
}

void Union(int x, int y) {
	int rx = find(x), ry = find(y);
	if(rx==ry) return;

	if( UF[rx] > UF[ry] ) {
		UF[ry] += UF[rx];
		UF[rx] = ry;
	} else {
       	UF[rx] += UF[ry];
		UF[ry] = rx;
	}
}

void initUF() {
	memset( UF, -1, sizeof UF);
}

double calc(int sz) {
	int res = 0;
	for(int i=1;i<=sz;++i) {
		if(UF[i]<-1) res -= UF[i];
	}
	return (double)res;
}

int main()
{
	int nCase = 1, T;
	int N, p;

	cin >> T;
	while(T-->0) {
		cin >> N;
		initUF();
		for( int i = 1 ; i <= N ; ++i ) {
			cin >> p;
			Union(p, i);
		}
		printf( "Case #%d: %.6f\n", nCase++, calc(N));
	}
	return 0;
}
