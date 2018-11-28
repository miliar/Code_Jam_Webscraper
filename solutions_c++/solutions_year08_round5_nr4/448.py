#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <cmath>
#include <algorithm>
using namespace std;

#define SZ(X) (int)X.size()
#define pb(X,Y) X.push_back(Y)


/*class  {
public:

};*/

bool board[101][101];
int dp[101][101];

int main() {
    int N;
    cin >> N;
    int num;
    for( num = 0; num < N; num++ ) {
        int H,W,R;
        cin >> H >> W >> R;
        int i,j;
        memset(board,true,sizeof(board));
        for( i = 0; i < R; i++ ) {
            int r,c;
            cin >> r >> c;
            board[r-1][c-1] = false;
        }
        memset(dp,0,sizeof(dp));
        dp[0][0] = 1;
        for( i = 0; i < H; i++ ) {
             for( j = 0; j < W; j++ ) {
                 if( i+1 < H && j+2 < W && board[i+1][j+2] ) 
                     dp[i+1][j+2] = (dp[i+1][j+2]+dp[i][j])%10007;
                 if( i+2 < H && j+1 < W && board[i+2][j+1] )
                     dp[i+2][j+1] = (dp[i+2][j+1]+dp[i][j])%10007;
             }
        }
        printf("Case #%d: %d\n",num+1,dp[H-1][W-1]);
    }
    system("pause");
    return 0;
}
