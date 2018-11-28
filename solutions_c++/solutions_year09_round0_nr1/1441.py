#include <cstdio>
#include <cstring>

#define Dmax 5015
#define Lmax 16

const int lambda = 30;

int L, D, N;
bool ok[Lmax][256];
char word[Dmax][Lmax];
char sir[Lmax * lambda];

void read() {
    scanf("%d %d %d", &L, &D, &N);

    for (int i = 1; i <= D; ++i)
        scanf("%s", word[i]);
}

void solve() {
    scanf("%s", sir);
    int pos = 0;

    memset(ok, 0, sizeof(ok));
    for (int i = 0; i < L; ++i) {
        if (sir[pos] != '(')
            ok[i][sir[pos++]] = true;
        else {
            ++pos;
            while (sir[pos] != ')')
                ok[i][sir[pos++]] = true;
            ++pos;
        }
    }

    int sol = 0;
    for (int i = 1; i <= D; ++i) {
        bool possible = true;
        for (int j = 0; j < L; ++j)
            if (!ok[j][word[i][j]]) {
                possible = false;
                break;
            }
        if (possible)
            ++sol;
    }
    
    printf("%d\n", sol);
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    read();
    for (int i = 1; i <= N; ++i) {
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
