#include <iostream>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdarg>
#include <cassert>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <set>
#include <list>
#include <algorithm>
#include <utility>
#include <unistd.h>
#include <cstdlib>
#include <map>
#include <sstream>
using namespace std;

#define REP(i,N) for(int i = 0;i < (N); ++i )
#define REPV(i,ar) for(int i = 0;i < (ar).sz; ++i )
#define EACH(it,mp) for( __typeof(mp.begin()) it(mp.begin()); it != mp.end(); ++it )
#define FOR(i,a,b) for(int i = (a); i <= (b); ++i )
#define sz size()
#define pb push_back
#define mkp make_pair
#define INF (int(1e9))
#define GI ({int t;scanf("%d",&t);t;})
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long int LL;


int Memo[ 512 ][ 32 ];
const char str[] = "welcome to code jam";
char S[512];

int MOD = 10000;

int go( int l , int p ) {
	int& ret = Memo[ l ][ p ];
	if( ret != -1 ) return ret;
	
	ret = 0;
	if( !str[p] ) return 1;
	if( !S[l] ) return 0;
	
	if( S[l] == str[p] ) ret += go( l+1 , p+1 ) , ret %= MOD;
	ret += go( l+1 , p );
	ret %= MOD;
	return ret;
}

int main(){
	int T = GI;
	getchar();
	freopen( "temp.cpp.out" , "w", stdout );
	REP(tt,T){
		memset( Memo , -1, sizeof( Memo ) );
		gets( S );
		printf("Case #%d: %04d\n", tt+1 , go( 0 , 0 ) );
	}
	
	return 0;
	
}