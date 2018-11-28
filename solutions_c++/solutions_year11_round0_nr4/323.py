// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen("d.in", "r", stdin); 
	freopen("d.out", "w", stdout);
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

const double eps = 1e-8;

bool mark[1004];
int n;
int p[1004];
int len;

void dfs(int v) {
	mark[v] = true;
	++len;
	if (!mark[p[v]]) {
		dfs(p[v]);
	}
}

void solve(int test_id) {
	printf("Case #%d: ", test_id);
	scanf("%d", &n);
	fi(n) {
		scanf("%d", p + i);
		--p[i];
	}	
	clr(mark);
	int ret = 0;
	fi(n) {
		if (!mark[i]) {
			len = 0;
			dfs(i);
			if (len > 1) {
				ret += len;
			}
		}
	}
	cout << ret << ".000000" << endl;
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
