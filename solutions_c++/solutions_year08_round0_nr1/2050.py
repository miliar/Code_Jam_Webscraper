#include <iostream>
#define INF 10000000

int N, S, Q;
char sname[110][10000];
char qname[1100][1000];
bool match[1100][110];
int dp[1100][110];

int main() {
    scanf("%d", &N);
    for (int i = 1; i <= N; ++i) {
        scanf("%d\n", &S);
        for (int j = 1; j <= S; ++j) gets(sname[j]);
        scanf("%d\n", &Q);
        if (Q == 0) {
            printf("Case #%d: 0\n", i);
        } else {
            for (int j = 1; j <= Q; ++j) gets(qname[j]);
            for (int j = 1; j <= Q; ++j) 
                for (int k = 1; k <= S; ++k) match[j][k] = !strcmp(qname[j], sname[k]);
            //printf("debug\n");
            for (int j = 1; j <= Q; ++j) {
                for (int k = 1; k <= S; ++k) {
                     if (match[j][k]) {
                         dp[j][k] = INF;
                     } else {
                         int min = 1;
                         for (int l = 1; l <= S; ++l) 
                             if (dp[j - 1][min] > dp[j - 1][l]) min = l;
                         dp[j][k] = dp[j - 1][k] <? dp[j - 1][min] + 1;
                     }
                }
            }
            int min = 1;
            for (int j = 1; j <= S; ++j)
                 if (dp[Q][min] > dp[Q][j]) min = j;
            printf("Case #%d: %d\n", i, dp[Q][min]);
        }
        /*for (int j = 1; j <= Q; ++j) {
            for (int k = 1; k <= S; ++k) printf("%d ", match[j][k]);
            printf("\n");
        }
        for (int j = 1; j <= Q; ++j) {
            for (int k = 1; k <= S; ++k) printf("%8d ", dp[j][k]);
            printf("\n");
        }*/
    }
}
