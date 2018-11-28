#include <cstdio>
#include <cstring>

#define Nmax 128

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int N, M, count;
int H[Nmax][Nmax];
int B[Nmax][Nmax];

void read() {
    scanf("%d %d", &N, &M);
    memset(H, 0x3f, sizeof(H));
    for (int i = 1; i <= N; ++i)
        for (int j = 1; j <= M; ++j)
            scanf("%d", &H[i][j]);
}

int sink(int x, int y) {
    if (B[x][y] != -1)
        return B[x][y];

    int d0 = -1, x0, y0, low = H[x][y];
    
    for (int d = 0; d < 4; ++d) {
        x0 = x + dx[d];
        y0 = y + dy[d];
        if (H[x0][y0] < low) {
            low = H[x0][y0];
            d0 = d;
        }
    }
    
    if (d0 == -1)
        B[x][y] = ++count;
    else {
        x0 = x + dx[d0];
        y0 = y + dy[d0];
        B[x][y] = sink(x0, y0);
    }

    return B[x][y];
}

void solve() {
    count = 0;
    memset(B, -1, sizeof(B));
    for (int i = 1; i <= N; ++i) {
        for (int j = 1; j <= M; ++j) {
            char sol = 'a' + sink(i, j) - 1;
            printf("%c ", sol);
        }
        printf("\n");
    }
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int T;
    
    scanf("%d", &T);
    for(int i = 1; i <= T; ++i) {
        printf("Case #%d:\n", i);
        read();
        solve();
    }

    return 0;
}
