#include <iostream>
#include <vector>
using namespace std;

const int maxn = 405, maxm = 2005;

int N, M, e[maxn][maxn], f[maxn], g[maxm];

int main()
{
    freopen("d2.in", "r", stdin);
    freopen("d2.out", "w", stdout);
    
    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        cin >> N >> M;
        memset(e, 0, sizeof(e));
        for (int i = 1; i <= M; ++i) {
            int x, y;
            scanf("%d,%d", &x, &y);
            e[x][y] = e[y][x] = i;
        }
        memset(f, -1, sizeof(f));
        vector<int> q(1, 0);
        f[0] = 0;
        for (int i = 0; i < q.size(); ++i)
            for (int j = 0; j < N; ++j)
                if (f[j] == -1 && e[q[i]][j]) {
                    f[j] = f[q[i]] + 1;
                    q.push_back(j);
                }
        for (int i = 1; i <= M; ++i)
            g[i] = -10000000;
        for (int i = 0; i < N; ++i)
            g[e[0][i]] = 0;
        for (int i = 1; i < q.size(); ++i) {
            int s = q[i];
            vector<int> tp;
            for (int j = 0; j < N; ++j)
                if (s != j && f[s] == f[j]) tp.push_back(j);
            for (int j = 0; j < N; ++j) if (f[j] < f[s] && e[j][s])
                for (int k = 0; k < N; ++k) if (f[k] > f[s] && e[s][k]) {
                    int p = 0;
                    for (int l = 0; l < tp.size(); ++l)
                        if (e[s][tp[l]] || e[j][tp[l]] || e[k][tp[l]])
                            ++p;
                    if (g[e[j][s]] + p > g[e[s][k]])
                        g[e[s][k]] = g[e[j][s]] + p;
                }
        }
        int ret1 = f[1] - 1, ret2 = 0;
        if (!ret1) {
            for (int i = 0; i < N; ++i)
                if (e[0][i]) ++ret2;
        }else {
            for (int i = 0; i < N; ++i) if (f[i] == ret1 && e[i][1])
                for (int j = 0; j < N; ++j) if (e[i][j] && f[j] < f[i]) {
                    int tmp = g[e[i][j]];
                    for (int k = 0; k < N; ++k) {
                        if (f[k] == f[i] && k != i && (e[j][k] || e[i][k])) ++tmp;
                        if (f[k] == f[1] && e[i][k]) ++tmp;
                    }
                    if (tmp > ret2) ret2 = tmp;
                }
        }
        cout << "Case #" << t2 << ": " << ret1 << " " << ret2 << endl;
        cerr << t2 << endl;
    }
    
    return 0;
}
