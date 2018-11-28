#pragma warning ( disable : 4786 )

#include <iostream>
#include <sstream>

#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>

#include <string>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
using namespace std;

//#define _rep( i, a, b, x ) for( __typeof(b) i = ( a ); i <= ( b ); i += x )
#define _rep( i, a, b, x ) for( i = ( a ); i <= ( b ); i += x )
#define rep( i, n ) _rep( i, 0, n - 1, 1 )

#define ff first
#define ss second

#define pii pair< int, int >
#define psi pair< string, int >

#define pb(x) push_back(x)
#define mp(x, y) make_pair(x, y)

#define set(p) memset(p, -1, sizeof(p))
#define clr(p) memset(p, 0, sizeof(p))

//typedef long long i64;
//typedef __int64 i64;
typedef long double ld;

//const double pi = (2.0*acos(0.0));
const double pi = acos(-1.0);
const double eps = 1e-9;
const int inf = (1<<28);
const int MAX = 105;

int sc[MAX], n, hi, sp;

int main() {
	freopen("B-large.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	
	int i, j, k;
	int test, t = 0, kase=0;
	int ans, cnt;

	scanf("%d", &test);
	while(test--) {
		scanf("%d %d %d", &n, &sp, &hi);
		for(i=0; i<n; i++) scanf("%d", &sc[i]);
		ans = 0;
		cnt = 0;
		for(i=0; i<n; i++) {
			if(sc[i]) {
				if(sc[i] % 3 == 0) {
					if((sc[i]/3) >= hi) ans += 1;
					else {
						if((sc[i]/3)+1 >= hi && cnt < sp) {
							ans += 1;
							cnt += 1;
						}
					}
				}
				else if(sc[i] % 3 == 1) {
					if((sc[i]/3)+1 >= hi) ans += 1;
				}
				else {
					if((sc[i]/3)+1 >= hi) ans += 1;
					else {
						if((sc[i]/3)+2 >= hi && cnt < sp) {
							ans += 1;
							cnt += 1;
						}
					}
				}
			}
			else {
				if(sc[i] == 0) {
					if(hi == 0) ans += 1;
				}
			}
		}
		printf("Case #%d: %d\n", ++t, ans);
	}
	return 0;
}
