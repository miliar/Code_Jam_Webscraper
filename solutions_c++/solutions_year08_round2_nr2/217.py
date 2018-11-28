
#include <stdio.h>

int prob, nprob;
int A, B, P;
int mat[1010][1010];
int lst[1010];
int vis[1010];

int gcd(int a, int b) {
    while (b) {
        int c = a % b;
        a = b; b = c;
    }
    return a;
}

void dfs(int v) {
    vis[v] = 1;
    for (int j = A; j <= B; j++)
        if (mat[v][j] && vis[j] == 0)
            dfs(j);
}

int main() {
 //   freopen("b.in", "r", stdin);
//    freopen("b.out", "w", stdout);

    scanf("%d", &nprob);
    for (prob = 1; prob <= nprob; prob++) {
        scanf("%d%d%d", &A, &B, &P);
        for (int i = A; i <= B; i++) {
            lst[i] = i; vis[i] = 0;
            for (int j = 2; j < P; j++)
                while (lst[i] % j == 0)
                    lst[i] /= j;
        }

        for (int i = A; i <= B; i++)
            for (int j = i+1; j <= B; j++) {
                mat[j][i] = mat[i][j] = (gcd(lst[i], lst[j]) > 1);
            }
            
        int ans = 0;
        for (int i = A; i <= B; i++)
            if (!vis[i]) {
                dfs(i); ans++;
            }
            
        printf("Case #%d: %d\n", prob, ans);
    }    
    
    
    return 0;
}
