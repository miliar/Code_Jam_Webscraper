/*
TASK:  
ALGO:
LANG: C++
USER: smilitude
DATE: 2010-06-05 Sat 10:23 PM	
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

int b[105][105], n[105][105];


void print() {
	FOR(i,1,6) { FOR(j,1,6) cout << b[i][j]; cout << endl; }
	cout << endl;	
}

int main() {
	int t, ncase = 0;
	cin >> t;
	while( t-- ) {
		int r, x1, x2, y1, y2;
		cin >> r;
		SET( b, 0 );
		while( r-- ) {
			cin >> x1 >> y1 >> x2 >> y2;
			FOR(i,x1,x2) FOR(j,y1,y2) b[j][i] = 1;	
		}

		int ans = 0;
		if( r ) while( 1 ) {

			FOR(i,1,100) FOR(j,1,100) 
				if( b[i][j] ) n[i][j] = b[i][j-1] || b[i-1][j];
				else n[i][j] = b[i][j-1] && b[i-1][j];

			int tot = 0;
			FOR(i,1,100) FOR(j,1,100) b[i][j] = n[i][j], tot += n[i][j];
		
			ans ++;
			if( !tot ) break;
		}
		printf("Case #%d: %d\n", ++ncase, ans );
	}
	return 0;
}

