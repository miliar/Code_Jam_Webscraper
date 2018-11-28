/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2010-05-09 Sun 01:18 AM	
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
void print( bool x ) {
	printf("Case #%d: %s\n", ++ncase, ( x ? "ON" : "OFF" ) );	
}

int main() {
	int t, n, k;
	scanf("%d",&t);

	while( t-- ) {
		scanf("%d %d",&n,&k);
		i64 fin = (1LL<<n) - 1, tot = fin+1;
		print( ( k % tot ) == fin );
	}

	return 0;
}

