#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <list>
#include <cmath>
#include <sstream>
using namespace std;
typedef long long LL;
typedef vector < int > VI;
#define SZ(X) ((int)X.size())
int m;
const int mod = 10007;
const int mn = 110;
int dp [mn][mn];
int bad[mn][mn];
int w , h;
bool isvalid ( int r , int c ) {
	return ( r >= 0  && c >= 0 && !bad[r][c] );
}
int main() {
	int t;
	cin >> t;
	for ( int n__ = 1 ; n__ <= t; n__ ++ ) {
		cout << "Case #" << n__ <<": " ;
		memset ( dp , 0 , sizeof ( dp ) );
		memset ( bad , 0 , sizeof ( bad ));
		dp[0][0] = 1;
		int h,w;
		cin >> h >> w;
		int r;
		cin >> r;
		for ( int i=0;i<r;i++ ) {
			int a , b;
			cin >> a>> b;
			bad[a-1][b-1] = 1;
		}
		for ( int i=0;i<h;i++ )
		for ( int j=0;j<w;j++ ) 
		{
			if ( isvalid ( i -1 , j - 2) ) dp[i][j] = (dp[i][j] + dp[i-1][j-2])%mod;
			if ( isvalid ( i-2,j-1 ) ) dp[i][j] = ( dp[i][j] + dp[i-2][j-1]) % mod ;
		}
		cout << dp[h-1][w-1] << endl;
	}
	return 0;
}
