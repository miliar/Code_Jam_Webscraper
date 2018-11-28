#include <cstdio>
#include <cstring>


#define Nmax 512
#define Lmax 32
#define MOD 10000

int N, L = 19;
char gcj[] = " welcome to code jam";
char sir[Nmax];
int D[Nmax][Lmax];

void read() {
    fgets(sir + 1, Nmax, stdin);
    N = strlen(sir + 1);
}

void solve() {
    memset(D, 0, sizeof(D));
    for (int i = 0; i <= N; ++i)
        D[i][0] = 1;

    for (int i = 1; i <= N; ++i)
        for (int j = 1; j <= L; ++j) {
            D[i][j] = D[i - 1][j];
            if (sir[i] == gcj[j])
                D[i][j] += D[i - 1][j - 1];
            D[i][j] %= MOD;
        }
    printf("%.4d\n", D[N][L]);
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int T;

    scanf("%d\n", &T);
    for (int i = 1; i <= T; ++i) {
        printf("Case #%d: ", i);
        read();
        solve();
    }

    return 0;
}
