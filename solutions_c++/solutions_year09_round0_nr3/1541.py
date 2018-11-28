#include <iostream>
using namespace std;

const string s = " welcome to code jam";
const int MOD = 10000;

int dp[25][505];

int main(){
    int n;
    cin >> n;
    string t;
    getline(cin, t); //end of line with number of cases
    for (int k=0; k<n; ++k){
        getline(cin, t);
        t = " " + t;
        for (int i=0; i<s.size(); ++i) dp[i][0] = 0;
        for (int j=0; j<t.size(); ++j) dp[0][j] = 1;
        for (int i=1; i<s.size(); ++i){
            for (int j=1; j<t.size(); ++j){
                dp[i][j] = dp[i][j-1];
                if (s[i] == t[j]){
                    dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD;
                }
            }
        }       
        printf("Case #%d: %.4d\n", k+1, dp[s.size()-1][t.size()-1]);
    }
    return 0;
}
