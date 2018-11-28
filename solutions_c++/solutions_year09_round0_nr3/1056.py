#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    freopen("C-large.in","r",stdin);
    freopen("largeout.txt","w",stdout);
    int N;
    string w="welcome to code jam";
    scanf("%d ",&N);
    for( int i=0; i<N; i++ ) {
        int dp[501][30];
        string str;
        getline(cin,str);
        for( int j=0; j<=str.size(); j++ ) {
            for( int k=0; k<=w.size(); k++ ) {
                if(j==0) {
                    dp[j][k]=0;
                    if(k==0) dp[j][k]=1;
                    continue;
                }
                dp[j][k] = dp[j-1][k];

                if( k>=1 && w[k-1] == str[j-1] ) {
                    dp[j][k] += dp[j-1][k-1];
                    dp[j][k]%=10000;
                }
            }
        }


        printf("Case #%d: %04d\n",i+1,dp[str.size()][w.size()]);
    }
    return 0;
}




