#include <string>
#include <iostream>

const int MAX_LEN = 1 << 9;
const int MOD = 10000;
const int lf = 19;

std::string w = "welcome to code jam", s;
int dp[lf][MAX_LEN];

int main () {
    int n, k, p, t;
    std::cin >> n; getline(std::cin,s);
    
    for (int i = 1; i <= n; ++i) {
        getline(std::cin,s);
        //std::cout << s << std::endl;
        memset(dp,0,sizeof(dp));
        
        t = 0;
        for (k = 0; k < s.size(); ++k) if (w[0] == s[k]) dp[0][k] = ++t;
        //for (k = 0; k < s.size(); ++k) printf("%d ", dp[0][k]);
        //printf("\n");
        
        for (p = 1; p < lf; ++p) {
            for (k = 0; k < s.size(); ++k) {
                if (k) dp[p][k] += dp[p][k-1];
                if (w[p] == s[k]) {
                   for (t = k-1; t >= 0; --t) if (w[p-1] == s[t]) break;
                   dp[p][k] += dp[p-1][t];
                   while (dp[p][k] > MOD) dp[p][k] -= MOD;
                }
            }
            //for (k = 0; k < s.size(); ++k) printf("%d ", dp[p][k]);
            //printf("\n");
        }
        
        printf("Case #%d: ", i);
        if (dp[lf-1][s.size()-1] < 1000) printf("0");
        if (dp[lf-1][s.size()-1] < 100) printf("0");
        if (dp[lf-1][s.size()-1] < 10) printf("0");
        printf("%d\n", dp[lf-1][s.size()-1]);
    }
    
    return 0;
}
