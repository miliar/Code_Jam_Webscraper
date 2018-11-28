#include <stdio.h>
#include <iostream>
#include <iomanip>
#include <algorithm>
using namespace std;
//welcome to code jam, 19
#define N 1000
#define LL long long
#define MOD 10000
int n, size;
char str[N];
LL dp[N][20];

int main( ){
	int ca = 0, i, j;
	char ch;
	scanf( "%d", &n );
	getchar( );
	for ( ca = 1; ca <= n; ca++ ){
		size = 0;
		while ( ( ch = getchar( ) ) != '\n' ){
			str[size++] = ch;
		}
		memset( dp, 0, sizeof(dp) );
		for ( i = 0; i < size; i++ ){
			if ( str[i] == 'w' )
				dp[i][1] = 1;
			else if ( str[i] == 'e' ){
				for ( j = 0; j < i; j++ ){
					dp[i][2] += dp[j][1];
					dp[i][7] += dp[j][6];
					dp[i][15] += dp[j][14];
				}
				dp[i][2] %= MOD;
				dp[i][7] %= MOD;
				dp[i][15] %= MOD;
			}
			else if ( str[i] == 'l' ){
				for ( j = 0; j < i; j++ ) dp[i][3] += dp[j][2];
				dp[i][3] %= MOD;
			}
			else if ( str[i] == 'c' ){
				for ( j = 0; j < i; j++ ){
					dp[i][4] += dp[j][3];
					dp[i][12] += dp[j][11];
				}
				dp[i][4] %= MOD;
				dp[i][12] %= MOD;
			}
			else if ( str[i] == 'o' ){
				for ( j = 0; j < i; j++ ){
					dp[i][5] += dp[j][4];
					dp[i][10] += dp[j][9];
					dp[i][13] += dp[j][12];
				}
				dp[i][5] %= MOD, dp[i][10] %= MOD, dp[i][13] %= MOD;
			}
			else if ( str[i] == 'm' ){
				for ( j = 0; j < i; j++ ){
					dp[i][6] += dp[j][5];
					dp[i][19] += dp[j][18];
				}
				dp[i][6] %= MOD, dp[i][19] %= MOD;
			}
			else if ( str[i] == ' ' ){
				for ( j = 0; j < i; j++ ){
					dp[i][8] += dp[j][7];
					dp[i][11] += dp[j][10];
					dp[i][16] += dp[j][15];
				}
				dp[i][8] %= MOD, dp[i][11] %= MOD, dp[i][16] %= MOD;
			}
			else if ( str[i] == 't' ){
				for ( j = 0; j < i; j++ ) dp[i][9] += dp[j][8];
				dp[i][9] %= MOD;
			}
			else if ( str[i] == 'd' ){
				for ( j = 0; j < i; j++ ) dp[i][14] += dp[j][13];
				dp[i][14] %= MOD;
			}
			else if ( str[i] == 'j' ){
				for ( j = 0; j < i; j++ ) dp[i][17] += dp[j][16];
				dp[i][17] %= MOD;
			}
			else if ( str[i] == 'a' ){
				for ( j = 0; j < i; j++ ) dp[i][18] += dp[j][17];
				dp[i][18] %= MOD;
			}
		}
		LL ans = 0;
		for ( i = 0; i < size; i++ ) ans = (ans+dp[i][19])%MOD;
		cout << "Case #" << ca << ": " << right << setw(4) << setfill( '0' ) << ans << endl;
		//printf( "Case #%d: %d\n", ca, ans );
	}
}
