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

int dp[2][10001];
int gate[10001];
int canchange[10001];
int v[10001];

int main() {
    int N,M,V;
    cin >> N;
    int num;
    for( num = 0; num < N; num++ ) {
        cin >> M >> V;
        memset(dp,-1,sizeof(dp));
        int i,j;
        for( i = 1; i <= (M-1)/2; i++ ) cin >> gate[i] >> canchange[i];
        for( ; i <= M; i++ ){
            int buf;
            cin >> buf;
            if( buf == 0 ) dp[0][i] = 0;
            else dp[1][i] = 0;
        }
        for( i = (M-1)/2; i >= 1; i-- ) {
            if( gate[i] == 1 ) {
                if( dp[1][2*i] > -1 && dp[1][2*i+1] > -1 ) dp[1][i] = dp[1][2*i]+dp[1][2*i+1];
                int tmp = 100000;
                if( dp[0][2*i] > -1 && dp[1][2*i+1] > -1 ) tmp = dp[0][2*i]+dp[1][2*i+1];
                if( dp[1][2*i] > -1 && dp[0][2*i+1] > -1 ) {
                    if( tmp > dp[1][2*i]+dp[0][2*i+1] ) tmp = dp[1][2*i]+dp[0][2*i+1];
                }
                if( dp[0][2*i] > -1 && dp[0][2*i+1] > -1 ) {
                    if( tmp > dp[0][2*i]+dp[0][2*i+1] ) tmp = dp[0][2*i]+dp[0][2*i+1];
                }
                if( tmp < 100000 ) dp[0][i] = tmp;
            }
            else {
                if( dp[0][2*i] > -1 && dp[0][2*i+1] > -1 ) dp[0][i] = dp[0][2*i]+dp[0][2*i+1];
                int tmp = 100000;
                if( dp[0][2*i] > -1 && dp[1][2*i+1] > -1 ) tmp = dp[0][2*i]+dp[1][2*i+1];
                if( dp[1][2*i] > -1 && dp[0][2*i+1] > -1 ) {
                    if( tmp > dp[1][2*i]+dp[0][2*i+1] ) tmp = dp[1][2*i]+dp[0][2*i+1];
                }
                if( dp[1][2*i] > -1 && dp[1][2*i+1] > -1 ) {
                    if( tmp > dp[1][2*i]+dp[1][2*i+1] ) tmp = dp[1][2*i]+dp[1][2*i+1];
                }
                if( tmp < 100000 ) dp[1][i] = tmp;    
            }
            if( canchange[i] ) {
                if( gate[i] == 1 ) {
                    if( dp[0][2*i] > -1 && dp[0][2*i+1] > -1 ) {
                        if( dp[0][i] < 0 || dp[0][i] > dp[0][2*i]+dp[0][2*i+1]+1 ) 
                            dp[0][i] = dp[0][2*i]+dp[0][2*i+1]+1;
                    }
                    int tmp = 100000;
                    if( dp[0][2*i] > -1 && dp[1][2*i+1] > -1 ) tmp = dp[0][2*i]+dp[1][2*i+1]+1;
                    if( dp[1][2*i] > -1 && dp[0][2*i+1] > -1 ) {
                        if( tmp > dp[1][2*i]+dp[0][2*i+1]+1 ) tmp = dp[1][2*i]+dp[0][2*i+1]+1;
                    }
                    if( dp[1][2*i] > -1 && dp[1][2*i+1] > -1 ) {
                        if( tmp > dp[1][2*i]+dp[1][2*i+1]+1 ) tmp = dp[1][2*i]+dp[1][2*i+1]+1;
                    }
                    if( tmp < 100000 )
                        if( dp[1][i] < 0 || dp[1][i] > tmp ) dp[1][i] = tmp;
                }
                else {
                    if( dp[1][2*i] > -1 && dp[1][2*i+1] > -1 ) {
                        if( dp[1][i] < 0 || dp[1][i] > dp[1][2*i]+dp[1][2*i+1]+1 )
                            dp[1][i] = dp[1][2*i]+dp[1][2*i+1]+1;
                    }
                    int tmp = 100000;
                    if( dp[0][2*i] > -1 && dp[1][2*i+1] > -1 ) tmp = dp[0][2*i]+dp[1][2*i+1]+1;
                    if( dp[1][2*i] > -1 && dp[0][2*i+1] > -1 ) {
                        if( tmp > dp[1][2*i]+dp[0][2*i+1]+1 ) tmp = dp[1][2*i]+dp[0][2*i+1]+1;
                    }
                    if( dp[0][2*i] > -1 && dp[0][2*i+1] > -1 ) {
                        if( tmp > dp[0][2*i]+dp[0][2*i+1]+1 ) tmp = dp[0][2*i]+dp[0][2*i+1]+1;
                    }
                    if( tmp < 100000 )
                        if( dp[0][i] < 0 || dp[0][i] > tmp )dp[0][i] = tmp;
                }
            }
        }
        printf("Case #%d:",num+1);
        if( dp[V][1] < 0 ) printf(" IMPOSSIBLE\n");
        else printf(" %d\n",dp[V][1]);
    }
    system("pause");
    return 0;
}
