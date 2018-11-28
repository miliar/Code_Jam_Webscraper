//head               
#include <cstdlib>   
#include <cstring>   
#include <memory>    
#include <cstdio>    
#include <fstream>   
#include <iostream>  
#include <cmath>     
#include <string>    
#include <sstream>   
#include <stack>     
#include <queue>     
#include <vector>    
#include <set>       
#include <map>       
#include <algorithm> 
#include <deque>     
#include <list>      
                     
using namespace std; 

const int MAXN = 1024;
const int MAXL = 1048576;
const int MAXV = 1048575;
int C[MAXN], N;
int dp[2][MAXL];

int main () {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int nCase = 1; nCase <= T; ++nCase) {
        scanf("%d", &N);
        int sum = 0;
        memset(dp, -1, sizeof(dp));
        int now = 1, pre = 0;
        dp[pre][0] = 0;
        bool can = false;

        for (int i = 0; i < N; ++i) {
            scanf("%d", &C[i]);
            sum += C[i];
        }
        for (int i = 0; i < N; ++i) {
            int Ci = C[i] ^ MAXV;
            memset(dp[now], -1, sizeof(dp[now]));
            for (int j = 0; j < MAXL; ++j) {
                if (dp[pre][j] != -1) {
                    if (dp[pre][j] + C[i] != sum) {
                        dp[now][j^C[i]] = max(dp[now][j^C[i]], dp[pre][j] + C[i]);
                    }
                    dp[now][j^Ci] = max(dp[now][j^Ci], dp[pre][j] + 0);
                }
            }
            swap(pre, now);
        }
        printf("Case #%d: ", nCase);
        if (dp[pre][0] != -1 && dp[pre][MAXV] != -1) {
            printf("%d\n", max(dp[pre][0], dp[pre][MAXV]));
        }
        else {
            printf("NO\n");
        }
    }
    return 0;
}


