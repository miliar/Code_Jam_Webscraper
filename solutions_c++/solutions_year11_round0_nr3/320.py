// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:128000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen("c.in", "r", stdin); 
	freopen("c.out", "w", stdout);
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

int n;
int a[1004];
ll sum;

void solve(int test_id) {
	printf("Case #%d: ", test_id);
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", a + i);
	}
	int x = a[0];
	for (int i = 1; i < n; ++i) {
		x ^= a[i];
	}
	if (x != 0) {
		printf("NO\n");
		return;
	}
	sort(a, a + n);
	reverse(a, a + n);
	sum = 0;
	for (int i = 0; i < n-1; ++i) {
		sum += (ll)a[i];
	}
	cout << sum << endl;
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
