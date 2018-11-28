#include<iostream>
using namespace std;


#define mod 10000
#define maxn 510
#define maxm 20

char key[maxm] = {"welcome to code jam"};
char str[maxn];
int dp[maxn][maxm];

int main() {
	freopen("D:\\in.in","r",stdin);
	freopen("D:\\laout.out","w",stdout);
	int T;
	while( scanf("%d\n", &T) != EOF ) {
		for( int ca = 1; ca <= T; ca ++ ) {	
			scanf("%[^\n]%*c", str);
			int lens = strlen( str );
			memset( dp, 0, sizeof(dp) );
			int ans = 0;
			for( int i = 0; i < lens; i ++ ) {
				for( int j = 0; j < 19; j ++ ) {
					if( str[i] == key[j] ) {
						if( j == 0 ) dp[i][j] = 1;
						else {
							for( int k = 0; k < i; k ++ )
								dp[i][j] = (dp[k][j - 1] + dp[i][j]) % mod;
						}
					}
				}
				ans = ( ans + dp[i][18] ) % mod;
			}
			printf("Case #%d: %04d\n", ca, ans);
		}
	}
	return 0;
}