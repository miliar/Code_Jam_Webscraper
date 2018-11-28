#include<iostream>
#include<string>
#include<cstdio>

using namespace std;

int main() {
    string c = "welcome to code jam";
    string input;

    int n;
    cin >> n;
    getline(cin, input);
    for(int t=1; t<=n; t++) {
        getline(cin, input);

        int dp[555][20] = {{}};

        for(size_t i=0; i<=input.length(); i++) dp[i][0] = 1;

        for(size_t i=0; i<input.length(); i++) {
            for(size_t j=0; j<c.length(); j++) {
                dp[i+1][j+1] = dp[i][j+1];
                if(input[i] == c[j]) {
                    (dp[i+1][j+1] += dp[i][j]) %= 1000;
                }
            }
        }

        printf("Case #%d: %04d\n", t, dp[input.length()][c.length()]);
    }
}

