#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long LL;
const LL INF = 1LL<<60;

int nCase=1, T;
int L, t, N, C;
int d[1001];
LL dp[1001][3];

void input() {
	scanf("%d%d%d%d", &L, &t, &N, &C);
	for(int i=1;i<=C;++i) {
		scanf("%d", &d[i]);
	}
	for(int i=C+1;i<=N;++i) {
		d[i] = d[i-C];
	}
}

LL useBooster( LL ti, LL d ) {
	if( ti >= t ) return ti+d;
	LL mt = t-ti;
	if ( mt/2 >= d ) return INF;
	else return ti+d+mt/2;
}

int calc() {
	dp[0][0] = dp[0][1] = dp[0][2] = INF;
	for(int i=0;i<=L;++i) dp[0][i] = 0;
	
	for(int i=1;i<=N;++i) {
		dp[i][2] = dp[i-1][2] + d[i]*2;
		dp[i][1] = min( dp[i-1][1] + d[i]*2, useBooster( dp[i-1][2], d[i] ) );
		dp[i][0] = min( dp[i-1][0] + d[i]*2, useBooster( dp[i-1][1], d[i] ) );
	}
	return min( dp[N][0], min( dp[N][1], dp[N][2] ) );
}

int main()
{
	scanf("%d", &T);
	while(T-->0) {
	    input();
		printf( "Case #%d: %d\n", nCase++, calc() );
	}
	return 0;
}
