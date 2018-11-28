#include <stdio.h>

typedef long long i64;

int prob, nprob;
int n, A, B, C, D, x0, y0, M;
int x[100], y[100];


int main() {
    //freopen("a.in", "r", stdin);
    //freopen("a.out", "w", stdout);
    
    scanf("%d", &nprob);
    for (prob = 1; prob <= nprob; prob++) {
        scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);
        int X = x0, Y = y0;
        for (int i = 0; i < n; i++) {
            x[i] = X; y[i] = Y;
            X = ((i64)A * (i64)X + (i64)B) % M;
            Y = ((i64)C * (i64)Y + (i64)D) % M;
        }
        
        int ans = 0;
        for (int i = 0; i < n; i++) {
            int x1 = x[i], y1 = y[i];
            for (int j = i+1; j < n; j++) {
                int x2 = x[j], y2 = y[j];
                for (int k = j+1; k < n; k++) {
                    int x3 = x[k], y3 = y[k];
                    
                    if ((x1 + x2 + x3) % 3) continue;
                    if ((y1 + y2 + y3) % 3) continue;
                    
                    ans++;
                }
            }
        }
        
        printf("Case #%d: %d\n", prob, ans);
    }
    
    return 0;
}
