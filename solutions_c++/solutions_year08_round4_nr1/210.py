#include<iostream>
#include<string>
#include<algorithm>
#include<map>
#include<memory>
#include<functional>

using namespace std;

const int INF=100000;

int main() {
    int t, m, v;
    int gate[10005];
    int val[10005];
    int dp[10005][2];
    cin >> t;
    for(int c=1; c<=t; c++) {
        cin >> m >> v;
        
        for(int i=1; i<=m; i++) {
            if(2*i+1 <= m) cin >> gate[i] >> val[i];
            else cin >> val[i];
        }
        
        
        
        for(int i=m; i>=1; i--) {
            dp[i][0] = dp[i][1] = INF;
            if(2*i+1 <= m) {
                if(gate[i] == 0) {
                    dp[i][0] = min(dp[i][0], dp[2*i][0] + dp[2*i+1][0]);
                    dp[i][1] = min(dp[i][1], dp[2*i][0] + dp[2*i+1][1]);
                    dp[i][1] = min(dp[i][1], dp[2*i][1] + dp[2*i+1][1]);
                    dp[i][1] = min(dp[i][1], dp[2*i][1] + dp[2*i+1][0]);
                }
                else {
                    dp[i][0] = min(dp[i][0], dp[2*i][0] + dp[2*i+1][0]);
                    dp[i][0] = min(dp[i][0], dp[2*i][1] + dp[2*i+1][0]);
                    dp[i][0] = min(dp[i][0], dp[2*i][0] + dp[2*i+1][1]);
                    dp[i][1] = min(dp[i][1], dp[2*i][1] + dp[2*i+1][1]);
                }
                
                if(val[i] == 1) {
                    dp[i][0] = min(dp[i][0], dp[2*i][0] + dp[2*i+1][0] + 1);
                    dp[i][1] = min(dp[i][1], dp[2*i][0] + dp[2*i+1][1] + 1);
                    dp[i][1] = min(dp[i][1], dp[2*i][1] + dp[2*i+1][1] + 1);
                    dp[i][1] = min(dp[i][1], dp[2*i][1] + dp[2*i+1][0] + 1);
                    
                    dp[i][0] = min(dp[i][0], dp[2*i][0] + dp[2*i+1][0] + 1);
                    dp[i][0] = min(dp[i][0], dp[2*i][1] + dp[2*i+1][0] + 1);
                    dp[i][0] = min(dp[i][0], dp[2*i][0] + dp[2*i+1][1] + 1);
                    dp[i][1] = min(dp[i][1], dp[2*i][1] + dp[2*i+1][1] + 1);
                }
            }
            else {
                if(val[i] == 0) dp[i][0] = 0;
                else dp[i][1] = 0;
            }
        }
        
        
        cout << "Case #" << c << ": ";
        if(dp[1][v] >= INF) cout << "IMPOSSIBLE\n";
        else cout << dp[1][v] << endl;
        
    }
}
