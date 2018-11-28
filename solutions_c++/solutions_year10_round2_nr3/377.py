#include <cstdio>
#include <cstring>
#include <algorithm>
#define M 600

using namespace std;

int f[M][M], c[M][M], ans[M];

int dp(int x, int k) {
    if(f[x][k]) {
        return f[x][k];
    }
    for(int i = max(1, 2 * k - x); i < k;  i ++) {
        f[x][k] = (f[x][k] + dp(k, i) * c[x - k - 1][k - i - 1]) % 100003;
    }
    return f[x][k];
}

void pre_done(){
    for(int i = 1; i <= 500; i ++) {
        f[i][1] = 1;
    }
    for(int i = 0; i <= 500; i ++) {
        c[i][i] = c[i][0] = 1;
    }
    for(int i = 2; i <= 500; i ++) {
        for(int j = 1; j < i; j ++) {
            c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % 100003;
        }
    }
    for(int n = 2; n <= 500; n ++) {
        ans[n] = 0;
        for(int i = 1; i < n; i ++) {
            ans[n] = (ans[n] + dp(n, i)) % 100003;
        }
    }
}
int main() {
    freopen("small.in", "r", stdin);
    freopen("small.out", "w", stdout);
    int nca;
    pre_done();
    scanf("%d", &nca);
    for(int ii=1;ii<=nca;ii++){
        int n;
        scanf("%d", &n);
        printf("Case #%d: %d\n", ii, ans[n]);
    }
    return 0;
}
