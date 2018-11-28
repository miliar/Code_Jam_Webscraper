#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cstdarg>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <queue>
#include <set>
#include <map>

using namespace std;

typedef long long LL;
typedef long double LD;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()

#define pb push_back
#define mp make_pair
#define fs first
#define sc second
#define y1 y1_gedjcdgfce
#define y0 y0_sadasdasdsa
#define ws ws_sadsadsada
#define left left_asdsadsadsadsa
#define right right_asdasdsadasda
#define hash hash_asdasdasdsad

#ifdef DEBUG
#define eprintf(...) {fprintf(stderr,__VA_ARGS__),fflush(stderr);}
#else
#define eprintf(...) {}
#endif

#define forn(i,n) for( int i = 0 ; i < (n) ; i++ )
#define forit(it,c) for( __typeof((c).begin()) it = (c).begin() ; it != (c).end() ; it++ )

#ifdef WIN32
#define INT64 "%I64d"
#else
#define INT64 "%lld"
#endif

#define TASK "task"

const int maxn = 239;

int valid(int a,int b,int c) {
	if( a < 0 || a > 10 ) return 0;
	if( b < 0 || b > 10 ) return 0;
	if( c < 0 || c > 10 ) return 0;
	if(abs(a-b) > 2 || abs(a-c) > 2 || abs(b-c) > 2) return 0;
	return 1;	
}

int surp(int a,int b,int c) {
	return ( abs(a-b) == 2 || abs(b-c) == 2 || abs(c-a) == 2 );
}
int max(int a, int b, int c) {
	return max(a,max(b,c));
}


int dp[maxn][maxn];
int mem[maxn][2][maxn];
int t[maxn];

int go(int tot, int fl, int mx ) {
	int &res = mem[tot][fl][mx];
	if( res != -1 ) return res;
	res = 0;
	forn(a, 11) forn(b, 11) forn(c, 11) {
		if( tot == a + b + c && valid(a,b,c) ){
			 if(surp(a, b, c) == fl && max(a,b,c) >= mx ) res = 1;
		}
	}
	return res;
}

int main(){
	#ifdef DEBUG
	assert(freopen(TASK".in","rt",stdin));
	assert(freopen(TASK".out","wt",stdout));
	#endif
	int T; scanf("%d",&T);
	memset(mem, -1, sizeof mem);
	for( int test = 1 ; test <= T ; test++ ) {
		memset(dp, -1, sizeof dp);
		int n, s; scanf("%d%d",&n,&s);
		int p; scanf("%d",&p);
		forn(i,n) scanf("%d",&t[i]);
		dp[0][0] = 0;
		for( int i = 0 ; i < n ; i++ ) {
			for( int j = 0 ; j < n ; j++ ) {
				if(dp[i][j]<0) continue;
				if( go(t[i],1,p) ) dp[i+1][j+1] = max(dp[i][j]+1,dp[i+1][j+1]);
				if( go(t[i],0,p) ) dp[i+1][j]   = max(dp[i][j]+1,dp[i+1][j]);
				if( go(t[i],1,0) ) dp[i+1][j+1] = max(dp[i][j],dp[i+1][j+1]);
				if( go(t[i],0,0) ) dp[i+1][j] = max(dp[i][j],dp[i+1][j]);
			}
		}
		//forn(i, n + 1 ){
		//	forn(j, n + 1 ) printf("%d%c",dp[i][j]," \n"[j==n]);
		//}
		printf("Case #%d: %d\n", test, max(dp[n][s],0) );
	}
	return 0;
}
