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

#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR(i,a,b) for(__typeof(b) i=(a); i<=(b); i++)

#define sz size()
#define pb push_back
#define ALL(x) x.begin(), x.end()

#define i64 long long
#define SET(t,v) memset((t), (v), sizeof(t))
#define REV(x) reverse( ALL( x ) )

#define IO freopen("C.in","r",stdin); freopen("C.out","w",stdout);
#define debug(x) cerr << __LINE__ <<" "<< #x " = " << x << endl

int memo[505][20];
string s = "welcome to code jam";
string in;

int solve( int pos, int match ) {
	if( match == s.sz ) return 1;
	if( pos == in.sz ) return 0;
	int& ret = memo[ pos ][ match ];
	if( ret != -1 ) return ret;

	ret = 0;
	ret += solve( pos + 1, match );
	if( in[pos] == s[ match ] ) ret += solve( pos+1, match+1 );
	ret %= 10000;
	return ret;
}

int main() {
	
	char b[1000];
	int n, ncase = 0;
	
	IO

	scanf("%d",&n);
	gets( b ); // :(
	while( n-- ) {
		gets( b );
		in = b;
		SET( memo, -1 );
		printf("Case #%d: %04d\n",++ncase, solve(0,0));
	}


	return 0;
}
