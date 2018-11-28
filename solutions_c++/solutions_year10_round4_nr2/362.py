

#include <cstdio>

const int
    MAXP = 15,
    MAXN = 1 << MAXP,
    oo = 2000000000;

int T, tc, sol, P, N;
int M[MAXN], dp[2][MAXN][MAXP + 1];

inline int max(int a, int b){
    if (a > b) return a;
    else return b;
}

int main(){

    scanf("%d", &T);
    
    for (tc = 1; tc <= T; tc++){
    
        scanf("%d", &P);
    
        N = 1 << P;
        
        for (int i = 0; i < N; i++){
            scanf("%d", &M[i]);
            M[i] = P - M[i];
        }
        
        int num = N / 2;
        
        for (int i = 0; i < num; i++){
            int cost;
            scanf("%d", &cost);
        
            int max_child = max(M[2 * i], M[2 * i + 1]);
            for (int j = max_child; j <= P; j++) dp[0][i][j] = 0;
            if (max_child > 0){
                dp[0][i][max_child - 1] = cost;
                for (int j = max_child - 2; j >= 0; j--)
                    dp[0][i][j] = oo;
            }
        }
        
        int x = 1;
        
        for (int i = 0; i < P - 1; i++, x ^= 1){
            
            num /= 2;
            
            for (int j = 0; j < num; j++){
                int cost;
                scanf("%d", &cost);
                
                for (int k = 0; k <= P; k++){
                
                    int choice1 = oo;
                    
                    if (dp[x^1][2 * j][k] < oo && dp[x^1][2 * j + 1][k] < oo)
                        choice1 = dp[x^1][2 * j][k] + dp[x^1][2 * j + 1][k];
                    
                    int choice2 = oo;
                    
                    if (k < P && dp[x^1][2 * j][k + 1] < oo && dp[x^1][2 * j + 1][k + 1] < oo){
                        choice2 = dp[x^1][2 * j][k + 1] + dp[x^1][2 * j + 1][k + 1] + cost;
                    }
                    
                    if (choice1 < choice2)
                        dp[x][j][k] = choice1;
                    else
                        dp[x][j][k] = choice2;
                
                }    
                
            }
            
        }        
        
        sol = dp[x^1][0][0];
    
        printf("Case #%d: %d\n", tc, sol);
    
    }

    return 0;
}
