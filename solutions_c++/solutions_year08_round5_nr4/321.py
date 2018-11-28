#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define forn(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(__typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define UNIQUE(a) SORT(a),(a).resize(unique(ALL(a))-a.begin())
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
typedef long long ll;
#define MOD 10007
int W, H, R;
int dp[111][111];
int mat[111][111];
int main(){
	int i, j, k;int casos;
	scanf("%i", &casos);
	for(int h = 0 ;h  < casos ; h++ ){
		memset(mat, 0, sizeof(mat));
		memset(dp, 0, sizeof(dp));
		scanf("%i %i %i", &H, &W, &R);
		for(i=0;i<R;i++){
			int r, c;
			scanf("%i %i", &r, &c); mat[r-1][c-1] = 1;
		}
		
		for(i=H-1;i>=0;i--){
			for(j=W-1;j>=0;j--){
				if( mat[i][j] ) continue;
				if( i == H-1 && j == W-1 ){
					dp[i][j] = 1;
					continue;
				}
				dp[i][j] = (dp[i+1][j+2] + dp[i+2][j+1])%MOD;
				if( i==0 && j == 0 ) {
// 					printf("%i %i\n", dp[i+1][j+2], dp[i+2][j+1]);
				}
			}
		}
		printf("Case #%i: %i\n", h+1, dp[0][0]%MOD);
	}return 0;
}














