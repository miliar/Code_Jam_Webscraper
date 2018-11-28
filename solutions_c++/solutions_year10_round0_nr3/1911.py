/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2010-05-09 Sun 12:34 AM	
*/

#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for( __typeof(b) i=(a); i<=(b); i++)
#define FORD(i,a,b) for(__typeof(a) i=(a); i>=(b); i--) 
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REV(x) reverse( ALL( x ) )
#define IO freopen("","r",stdin); freopen("","w",stdout);
#define bug(x) if(1) cerr << __LINE__ <<" "<< #x " = " << x << endl
#define VI vector<int>
#define VS vector<string>

int ncase;

void print( i64 ans ) {
	printf("Case #%d: ", ++ncase );
	cout << ans << endl;
}

int main() {
	int t;
	scanf("%d",&t);

	while( t-- ) {
		int R, K, n;
		int g[1005], en[1005];
		i64 gain[1005];

		scanf("%d %d %d",&R, &K, &n);
		REP(i,n) scanf("%d",&g[i]);

		REP(i,n) {
			i64 top = 0;
			int j = i, cool = 1;	
			while( cool || j != i ) {
				cool = 0;
				top += g[j];
				if( top > K ) {
					top -= g[j];
					break;
				}
				j = ( j+1 ) % n;
			}
			gain[i] = top;
			en[i] = j;
		}
		
		i64 ans = 0;
		int top = 0;
		REP(_,R) {
			ans += gain[ top ];
			top = en[ top ];
		}
		
		print( ans );
	}

	return 0;
}

