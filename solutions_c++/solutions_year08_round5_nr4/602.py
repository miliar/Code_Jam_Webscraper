#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
using namespace std;

#define DEBUG

int W,H,R, r[16],c[16];

int dp[128][128];
bool map[128][128];

int const mod = 10007;

int main(int argc, char *argv[]) {
    int T;
    int res;
    scanf("%d", &T);
    for ( int nc = 1 ; nc <= T ; ++nc ) {
	memset(dp,0, sizeof(dp));
	memset(map, 0, sizeof(map));
	// input
	scanf("%d%d%d", &H, &W, &R);
	for ( int i = 0 ; i < R ; ++i ) {
	    scanf("%d%d", &r[i], &c[i]);
	    map[r[i]-1][c[i]-1] = true;
	}
	dp[0][0] = 1;
	for ( int i = 0 ; i < H ; ++i ) for ( int j = 0 ; j < W ; ++j ) {
	    if ( dp[i][j] == 0 || map[i][j] ) continue;
	    if ( i+2 < H && j+1 < W ) {dp[i+2][j+1] += dp[i][j];dp[i+2][j+1] %= mod; }
	    if ( i+1 < H && j+2 < W ) {dp[i+1][j+2] += dp[i][j];dp[i+1][j+2] %= mod; }
	}
	for ( int i = 0 ; i < H ; ++i ) for ( int j = 0 ; j < W ; ++j ) {
	    if ( map[i][j] ) {
		dp[i][j] = 0;
	    }
	}
	
	// output
	printf("Case #%d: %d\n", nc, dp[H-1][W-1]%mod);
    }
    return 0;
}
