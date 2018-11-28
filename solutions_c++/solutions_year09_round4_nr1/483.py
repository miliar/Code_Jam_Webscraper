/*
TASK: 
LANG: C++
USER: smilitude1
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
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)
#define SET(t,v) memset((t), (v), sizeof(t))
#define sz size()
#define pb push_back
#define i64 long long
#define ALL(x) x.begin(), x.end()

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REV(x) reverse( ALL( x ) )

#define IO freopen("a.in","r",stdin); freopen("a.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl
int n;

int main() {
	
	IO

	int t, ncase = 0;
	scanf("%d",&t);
	while( t-- ) {
		scanf("%d",&n);
		
		char line[100];
		vector< int > v;
		REP(i,n) {
			scanf("%s", line );
			int last1 = -1;
			REP(j,n) if( line[j] == '1' ) last1 = j;
			v.pb( last1 );
		}
		
		int ans = 0;
		REP(i,n) if( v[i] > i ) {
			int  b;
			
			FOR(j,i+1,n-1) if( v[j] <= i ) {
				b = j; break;
			}

			ans += b-i;
			for(int j=b; j>i; j--) swap( v[j],v[j-1] );	
		}
		

		printf("Case #%d: %d\n", ++ncase, ans ); 
	}
	
	return 0;
}
