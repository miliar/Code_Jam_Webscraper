// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen("in.txt", "r", stdin); 
	freopen("a.out", "w", stdout);
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <queue>

using namespace std;

#define fr(i,a,b) for ( int i = ( a ); i <= ( b ); ++i )
#define fi( a ) for ( int i = 0; i < ( a ); ++i )
#define fj( a ) for ( int j = 0; j < ( a ); ++j )
#define fk( a ) for ( int k = 0; k < ( a ); ++k )
#define CLR( a, b ) memset( ( a ), ( b ), sizeof ( a ) )
#define clr( a ) CLR( ( a ), 0 )
#define pb push_back
#define mp make_pair
#define all( v ) ( v ).begin(), ( v ).end()

typedef unsigned int uint;
typedef unsigned long long ull;
typedef long long ll;
typedef vector < int > vi;
typedef pair < int, int > pii;

int gcd(int x, int y) {
	if (y == 0) {
		return x;
	} else {
		return gcd(y, x % y);
	}
}

ll doit(int P, ll n) {
	int t = gcd(P, 100);
	P /= t;
	int cur = 100 / t;
	if (cur <= n) {
		return 1;
	}
	return -1;	
}

void solve(int test_id) {
	printf("Case #%d: ", test_id);
	int Pd, Pg;
	ll n;
    scanf("%lld%d%d", &n, &Pd, &Pg);
    if (Pg == 100) {
    	if (Pd != 100) {
			printf("Broken\n");
			return;    		
    	}
    }
    if (Pg == 0) {
    	if (Pd != 0) {
    		printf("Broken\n");
			return;    		
    	}
    }
    ll valD = doit(Pd, n);
	if (valD >= 0) {
		printf("Possible\n");
	} else {
		printf("Broken\n");
	}
}

int main() {
	initf();
	int T, i;
	scanf("%d", &T);
	for (i = 1; i <= T; ++i) { 
		solve(i);
	}
	return 0;
}
