#include <iostream>
#include <cstdio>
#include <set>
#include <vector>
#include <string>
#include <map>
#include <vector>
#include <queue>
using namespace std;
#define For(i,a,b) for(__typeof(a) i=a;i!=b;i++)
#define Rep(i,n) For(i,0,n)
#define set(a,c) memset(a,c,sizeof(a))
#define GI ({int t;scanf("%d",&t);t;})
#define pb push_back
#define INF (int)1e8
typedef pair<int,int> ii;
bool reach[100][100];
int dp[100][100];
int main() {
  int N = GI,test;
  For(test,1,N+1) {
    cout << "Case #" << test << ": ";
    set(dp,0);
    set(reach,0);
    dp[0][0] = 1;
    int H = GI, W = GI;
    int R = GI;
    while (R--) {
      reach[GI-1][GI-1] = 1;
    }
    For(i,1,H) {
      Rep(j,W) {
	if (reach[i][j])
	  continue;
	if (j >= 2 && i >= 1) {
	  dp[i][j] += dp[i-1][j-2];
	  dp[i][j] %= 10007;
	}
	if (j >= 1 && i >= 2) {
	  dp[i][j] += dp[i-2][j-1];
	  dp[i][j] %= 10007;
	}
      }
    }
    cout << dp[H-1][W-1] << endl;
  }
}
