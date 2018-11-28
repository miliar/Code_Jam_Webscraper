#include <iostream>
#include <queue>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int d[101][101][101];
char rob[101];
int but[101];

struct Node {
    int a, b, c;
    Node(int a, int b, int c) : a(a), b(b), c(c) {}
};

int main() {
    int tott, n;
    scanf("%d", &tott);
    for (int curt = 1; curt <= tott; ++curt) {
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf(" %c%d", &rob[i], &but[i]);
        }

        memset(d, 0xff, sizeof d);
        queue<Node> q;
        d[0][1][1] = 0;
        for (q.push(Node(0, 1, 1)); !q.empty(); q.pop()) {
            int a = q.front().a;
            int b = q.front().b;
            int c = q.front().c;
            for (int nb = max(b - 1, 1); nb <= min(b + 1, 100); ++nb) {
                for (int nc = max(c - 1, 1); nc <= min(c + 1, 100); ++nc) {
                    int na = a;
                    if (rob[a] == 'O' && but[a] == b && b == nb) {
                        na = a + 1;
                    }
                    if (rob[a] == 'B' && but[a] == c && c == nc) {
                        na = a + 1;
                    }
                    if (d[na][nb][nc] == -1) {
                        d[na][nb][nc] = d[a][b][c] + 1;
                        q.push(Node(na, nb, nc));
                    }
                }
            }
        }
        int ans = 1000000000;
        for (int i = 1; i <= 100; ++i) {
            for (int j = 1; j <= 100; ++j) {
                ans = min(ans, d[n][i][j]);
            }
        }
        printf("Case #%d: %d\n", curt, ans);
    }
    return 0;
}

