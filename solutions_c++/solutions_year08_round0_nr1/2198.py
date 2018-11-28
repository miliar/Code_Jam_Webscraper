#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

map <string, int> m;
int dp[1024][128];
vector <string> q;

int main() {
    
    int numTests;
    int testCase;
    int N, S, Q;
    string s;
    char szBuff[128];
    
    scanf("%d", &numTests);
    for (testCase = 1; testCase <= numTests; testCase++ ) {
        scanf("%d\n", &S);
        for (int i = 0; i < S; i++) {
            gets(szBuff);
            s.clear();
            s += szBuff;
            m[s] = i;
        }
    
        scanf("%d\n", &Q);
    
        for (int i = 1; i <= Q; i++) {
            gets(szBuff);
            s.clear();
            s += szBuff;
            for (int j = 0; j < S; j++) {
                dp[i][j] = INT_MAX/2;
                if (m[s] != j) {
                    for (int k = 0; k < S; k++) {
                        dp[i][j] = min(dp[i][j], dp[i-1][k] + ((j==k)?0:1));
                    }
                }
            }
        }
    
        int ans = INT_MAX;
    
        for (int i = 0; i < S; i++) {
            ans = min(ans, dp[Q][i]);
        }
    
        printf("Case #%d: %d\n", testCase, ans);
    
    }
return 0;
}
