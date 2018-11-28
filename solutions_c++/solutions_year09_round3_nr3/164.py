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

#define IO freopen("c.in","r",stdin); freopen("c.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl

int memo[400][400];
int p[105], np;
bool open[10005]; // one based
int bad[400], nbad;
int n;

int solve( int l, int r ) {
	if( l >= r ) return 0;
	int& ret = memo[l][r];
	if( ret != -1 ) return ret;

	ret = (1<<30);
	int cost = bad[r] - bad[l];
	bool dumb = 0;
	FOR(i,l,r) {
		if( open[ bad[i] ] ) ret = min( ret, cost + solve(l,i-1) + solve( i+1, r ) ), dumb = 1 ;
	}
	if( !dumb ) ret = 0; // no prison break in this region
//	printf("%d %d (%d - %d) = %d\n", l, r, bad[l], bad[r], ret);
	return ret;
}

int main() {
	int t, ncase = 0;
	
	IO
	
	scanf("%d",&t);
	while( t-- ) {
		scanf("%d %d",&n,&np);
		SET( open, 0 );
		REP(i,np) {
			scanf("%d",&p[i]);
			open[p[i]] = true; 
		}
		nbad = 0;
		FOR(i,1,n) if( i == 1 || i == n || open[i] || ( i && open[i-1] ) || ( i < n && open[i+1] ) ) {
			bad[ nbad++ ] = i;
		}
		
	//	REP(i,nbad) cout << bad[i] << endl;

		SET( memo, -1 );
		int ans = solve( 0, nbad-1 );
		printf("Case #%d: %d\n", ++ncase, ans );
	}

	return 0;
}
