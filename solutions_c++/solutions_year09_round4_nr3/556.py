#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

typedef __int64 I;
const int N = 110, M = 30;

int _p[N][M];
int _g[N][M];
int _b[N][N];
int _bend[N];
int _end;
int _bst;

void DFS(int n, int d) {
    if (d == n) {
        _bst = min(_bst, _end);
        return;
    }
    int i, j;
    for (i = 0; i < _end; ++i) {
        for (j = 0; j < _bend[i]; ++j) {
            if (_g[d][_b[i][j]]) break;
        }
        if (j < _bend[i]) continue;
        _b[i][_bend[i]++] = d;
        DFS(n, d + 1);
        --_bend[i];
    }
    if (_end < _bst) {
        i = _end++;
        _b[i][_bend[i]++] = d;
        DFS(n, d + 1);
        --_bend[i];
        --_end;
    }
}

int main() {
    freopen("c.small.in.txt", "r", stdin);
    freopen("c.small.out.txt", "w", stdout);
    int tc;
    scanf("%d", &tc);
    for (int ti = 1; ti <= tc; ++ti) {
        memset(_g, 0, sizeof(_g));
        memset(_bend, 0, sizeof(_bend));
        int n, m;
        scanf("%d%d", &n, &m);
        int i, j, k;
        for (i = 0; i < n; ++i) {
            for (j = 0; j < m; ++j) {
                scanf("%d", _p[i] + j);
            }
        }
        for (i = 0; i < n; ++i) {
            for (j = 0; j < i; ++j) {
                for (k = 1; k < m; ++k) {
                    if (I(_p[i][k] - _p[j][k]) 
                        * I(_p[i][k - 1] - _p[j][k - 1]) <= 0L) {
                        _g[i][j] = _g[j][i] = 1;
                        break;
                    }
                }
            }
        }
        _end = 0;
        _bst = n;
        DFS(n, 0);
        printf("Case #%d: %d\n", ti, _bst);
    }
    return 0;
}
