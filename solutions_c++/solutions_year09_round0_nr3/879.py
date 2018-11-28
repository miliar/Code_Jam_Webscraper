#include <iostream>
#include <string.h>
#include <stdio.h>
#define maxn 510
#define M 1000
#define len(a) int((a).size())
using namespace std;

const char eps[] = "welcome to code jam";

int N;
int dp[maxn][20];
string line;

int solve(){
    memset(dp, 0, sizeof dp);
    getline(cin, line);
    //cerr << "|" << line << endl;
    
    dp[0][0] = 1;
    
    for (int i = 1; i <= len(line); i++){
        dp[i][0] = 1;
        for (int j = 1; j <= 19; j++){
            dp[i][j] = dp[i-1][j];
            if (eps[j-1] == line[i-1]){
                dp[i][j] += dp[i-1][j-1];
            }
            //if (dp[i][j] > 0) cout << i << " " << j << " = " << dp[i][j] << endl; 
            dp[i][j] %= 10000;
        }    
    }
    
    return dp[len(line)][19];
    
}

int main(){
    cin >> N;
    string w;
    getline(cin, w);
    //char ch;
    //cin >> ch;
    
    
    for (int i = 1; i <= N; i++){
        //cout << "Case #" << i << ": " << solve() << endl;
        printf("Case #%d: %.4d\n",i,solve());   
        //break;
    }
    return 0;    
}
