#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAX_N 2050
#define MAX_P 12

int P;
long long DP[4 * MAX_N][MAX_P];
int M[MAX_N];
int cost[4 * MAX_N];

void read() {
    scanf("%d", &P);
    for (int i = 0; i < (1 << P); ++i)
        scanf("%d", &M[i + 1]);
    for (int i = 1; i <= P; ++i) {
        for (int j = (1 << (P - i)); j < (1 << (P - i + 1)); ++j) {
            //printf("%d ", j);
            scanf("%d", &cost[j]);
        }
        //printf("\n");
    }
}

void DF(int nod, int st, int dr) {
    if (st == dr) {
        for (int i = 0; i <= M[st]; ++i)
            DP[nod][i] = 0;
    } else {
        int fs = nod * 2, fd = nod * 2 + 1;
        DF(fs, st, (st + dr) / 2);
        DF(fd, (st + dr) / 2 + 1, dr);

        //printf("nod %d -> %d\n", nod, cost[nod]);
        for (int i = 0; i <= P; ++i) {
            DP[nod][i] = min(DP[nod][i], DP[fs][i] + DP[fd][i] + cost[nod]);
            DP[nod][i] = min(DP[nod][i], DP[fs][i + 1] + DP[fd][i + 1]);
            //printf("-- %d %d - %d -> %lld\n", st, dr, i, DP[nod][i]);
        }
    }
}

void solve() {
    memset(DP, 0x1f, sizeof(DP));
    DF(1, 1, (1 << P));
    printf("%lld\n", DP[1][0]);
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        read();
        printf("Case #%d: ", i);
        solve();
    }

    return 0;
}
