#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

const int INF = 100 * 1000;
vector<int> vec[128 * 128];
int height[128][128];
bool viz[128 * 128];
char let;
char sol[128][128];
int N, M;

// N W E S
const int dx[] = {-1, +0, +0, +1};
const int dy[] = {+0, -1, +1, +0};

inline int node(int x, int y) {
    return (x - 1) * M + (y - 1);
}

inline void add_edge(int n1, int n2) {
    //printf("%d -> %d\n", n1, n2);
    vec[n1].push_back(n2);
    vec[n2].push_back(n1);
}

void dfs(int nd) {
    if (viz[nd]) return;
    int x = nd / M, y = nd % M;
    sol[x][y] = let;
    viz[nd] = 1;
    for (int i = 0; i < vec[nd].size(); ++i) {
        dfs(vec[nd][i]);
    }
}

int main() {
    FILE *f = fopen("b.in", "rt");
    int T;
    fscanf(f, "%d", &T);
    for (int t = 1; t <= T; ++t) {
        fscanf(f, "%d %d", &N, &M);
        for (int i = 0; i <= N + 1; i ++) {
            height[i][0] = height[i][M + 1] = INF;
        }
        for (int i = 0; i <= M + 1; i ++) {
            height[0][i] = height[N + 1][i] = INF;
        }
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= M; ++j) {
                fscanf(f, "%d", height[i] + j);
            }
        }
        /*
        for (int i = 0; i <= N + 1; ++i) {
            for (int j = 0; j <= M + 1; ++j) {
                fprintf(stderr, "%d ", height[i][j]);
            }
            fprintf(stderr, "\n");
        }
        */
        for (int i = 0; i < N * M; ++i) {
            vec[i].clear();
        }
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= M; ++j) {
                int mn = INF, di, dj, md = -INF;
                for (int d = 0; d < 4; ++d) {
                    di = i + dx[d];
                    dj = j + dy[d];
                    if (mn > height[di][dj]) {
                        mn = height[di][dj];
                        md = d;
                    }
                }
                if (md >= 0) {
                    di = i + dx[md];
                    dj = j + dy[md];
                    if (mn < height[i][j]) {
                        add_edge(node(i, j), node(di, dj));
                    }
                }
            }
        }
        let = 'a';
        memset(viz, 0, sizeof(viz));
        for (int i = 1; i <= N; ++i) {
            for (int j = 1; j <= M; ++j) {
                int nd = node(i, j);
                if (viz[nd] == 0) {
                    dfs(nd);
                    ++let;
                }
            }
        }
        printf("Case #%d:\n", t);
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (j) printf(" ");
                printf("%c", sol[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
