#include <cstdio>
#include <cstring>
#include <algorithm>

const int dx[4] = {-1, 0, 0, 1};
const int dy[4] = {0, -1, 1, 0};

int height[100][100];
bool used[100][100];
int f[10000];
int label[10000];
int N, M;

int find(int x) {
    int y = x, z;
    while (f[y] != -1) y = f[y];
    while (x != y) {
        z = x;
        x = f[x];
        f[z] = y;
    }
    return y;
}

int main() {
    int caseSize;
    scanf("%d", &caseSize);
    for (int T = 1; T <= caseSize; T++) {
        scanf("%d%d", &N, &M);
        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                scanf("%d", &height[i][j]);
        memset(used, false, sizeof(used));
        memset(f, -1, sizeof(f));
        for (int x0 = 0; x0 < N; x0++)
            for (int y0 = 0; y0 < M; y0++)
                if (!used[x0][y0]) {
                    int Min = 0x7fffffff, i = x0, j = y0;
                    while (true) {
                        used[i][j] = true;
                        for (int k = 0; k < 4; k++) {
                            int x = i + dx[k], y = j + dy[k];
                            if (x < 0 || x >= N || y < 0 || y >= M) continue;
                            Min = std::min(Min, height[x][y]);
                        }
                        if (Min >= height[i][j]) break;
                        for (int k = 0; k < 4; k++) {
                            int x = i + dx[k], y = j + dy[k];
                            if (x < 0 || x >= N || y < 0 || y >= M) continue;
                            if (height[x][y] == Min) {
                                f[find(i * M + j)] = x * M + y;
                                i = x; j = y;
                                break;
                            }
                        }
                        if (used[i][j]) break;
                    }
                }
        memset(label, -1, sizeof(label));
        memset(used, false, sizeof(used));
        int size = 0;
        printf("Case #%d:\n", T);
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (j != 0) printf(" ");
                int x = find(i * M + j);
                if (label[x] == -1)
                    label[x] = size++;
                printf("%c", label[x] + 'a');
            }
            printf("\n");
        }
    }
    return 0;
}
