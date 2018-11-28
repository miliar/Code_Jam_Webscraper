#include <stdio.h>
#include <stdlib.h>
#include <map>
#include <string>
using namespace std;

map<string, int> name;
int *dp, *dp2, *tmp;
int mem[101], mem2[101];
char str[101];

int main(){
    int n, i, j, N, S, Q, res, min, min2;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d", &N);
    dp = mem;
    dp2 = mem2;
    for (n = 1; n <= N; ++n){
        res = 0;
        name.clear();
        scanf("%d", &S);
        gets(str);
        for (i = 0; i < S; ++i){
            gets(str);
            name[string(str)] = i;
        }
        scanf("%d", &Q);
        if (Q == 0){
            printf("Case #%d: 0\n", n);
            continue;
        }
        gets(str);
        gets(str);
        memset(dp, 0, sizeof(int) * S);
        dp[name[string(str)]] = 1001;   
        
        if (dp[0] >= dp[1]){
            min = 1;
        }
        else {
            min = 0;
        }
        
        for (i = 1; i < Q; ++i){
            gets(str);
            min2 = 0;
            for (j = 0; j < S; ++j){
                if (j == name[string(str)]){
                    dp2[j] = 1001;
                    continue;
                }
                dp2[j] = dp[j];
                if (min != j){
                    dp2[j] <?= dp[min] + 1;
                }
                if (dp2[j] < dp2[min2]) min2 = j;
            }
            tmp = dp;
            dp = dp2;
            dp2 = tmp;
            min = min2;
        }
        printf("Case #%d: %d\n", n, dp[min]);
    }
    return 0;
}
