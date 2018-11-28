#include <iostream>
#include <string>
#include <vector>
#include <utility>
using namespace std;



int main() {
    int N, aux, aux2, cases = 0;
    string ref = "welcome to code jam";
    int TAM = ref.size();
    scanf("%d", &N);
    cin.ignore();
    while (N--) {
        string line;
        getline(cin, line);

        int dp[501][TAM];

        for (int i = 0; i < TAM; ++i) dp[0][i] = 0;
        for (int i = 1; i <= line.size(); ++i) dp[i][0] = dp[i-1][0] + (line[i-1] == 'w');

        for (int j = 1; j < TAM; ++j) {
            for (int i = 1; i <= line.size(); ++i) {
                dp[i][j] = (line[i-1] == ref[j] ? dp[i-1][j-1] + dp[i-1][j] : dp[i-1][j])%10000;
            }
        }

        printf("Case #%d: %.4d\n", ++cases, dp[line.size()][TAM-1]);
    }
}

