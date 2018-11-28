// AlexFetisov
// Accepted

#define _CRT_SECURE_NO_DEPRECATE
#pragma comment (linker, "/STACK:32000000")

#include <iostream>
#include <stdio.h>
#include <cstring>

void initf() 
{ 
	freopen("a.in", "r", stdin); 
	freopen("a.out", "w", stdout);
}

#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <deque>

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
pii comm[104];
int cc = 0;
int dp[104][104][104];

void relax(int & a, int b) {
	if (a == -1 || a > b) {
		a = b;
	}
}

void solve(int test_id) {
	printf("Case #%d: ", test_id);
	cin >> n;
	for (int i = 0; i < n; ++i) {
		char c;
		int x;
		cin >> c;
		cin >> x;
		int c1 = 0;
		if (c == 'B') {
			c1 = 1;
		}
		comm[i] = mp(c1, x);
	}
	CLR(dp, -1);
	dp[0][1][1] = 0;
	for (int c = 0; c < n; ++c) {
		for (int p1 = 1; p1 <= 100; ++p1) {
			for (int p2 = 1; p2 <= 100; ++p2) {
				if (dp[c][p1][p2] != -1) {
					for (int np = 1; np <= 100; ++np) {
						if (comm[c].first == 0) {
							int nt = max(abs(comm[c].second - p1) + 1, abs(np - p2));
							relax(dp[c+1][comm[c].second][np], dp[c][p1][p2] + nt);	
						} else {
							int nt = max(abs(comm[c].second - p2) + 1, abs(np - p1));
							relax(dp[c+1][np][comm[c].second], dp[c][p1][p2] + nt);	
						}
					}
				}
			}
		}	
	}
	int ret = (1 << 30);
	for (int p1 = 1; p1 <= 100; ++p1) {
		for (int p2 = 1; p2 <= 100; ++p2) {
			if (dp[n][p1][p2] != -1) {
				ret = min(ret, dp[n][p1][p2]);
			}
		}
	}	
	printf("%d\n", ret);
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
