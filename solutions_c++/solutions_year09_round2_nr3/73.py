#include <cstdio>
#include <string>
#include <queue>

using namespace std;

#define MAXN 22
#define MAXV 255

char m[MAXN][MAXN];
const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, 1, 0, -1};

string can[MAXV * 2][MAXN][MAXN];

#define stare pair<int, pair<int, int> >
#define sV first
#define sX second.first
#define sY second.second
#define make_stare(a, b, c) make_pair(a, make_pair(b, c))
queue<stare> Q;

inline int solLess(const string &a, const string &b) {
    if (a.length() < b.length()) {
        return 1;
    }
    if (a.length() > b.length()) {
        return 0;
    }
    return a < b;
}

int main() {
    freopen("C.in", "rt", stdin);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        printf("Case #%d:\n", t);

        int N, Queries;
        scanf("%d %d", &N, &Queries);
        for (int i = 0; i < 2 * MAXV; i++) {
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    can[i][j][k] = "";
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                scanf(" %c", m[i] + j);
                if (m[i][j] != '+' && m[i][j] != '-') {
                    can[m[i][j] - '0' + MAXV][i][j] = m[i][j];
                    Q.push(make_stare(m[i][j] - '0', i, j));
                }
            }
        }

        for (; !Q.empty(); Q.pop()) {
            stare cur = Q.front();
            /*
            printf("%d %d %d\n", cur.sV, cur.sX, cur.sY);
            printf("%s\n", can[cur.sV][cur.sX][cur.sY].c_str());
            fflush(stdout);
            */

            for (int k = 0; k < 4; k++) {
                int _x = cur.sX + dx[k];
                int _y = cur.sY + dy[k];

                if (_x < 0 || _x >= N || _y < 0 || _y >= N) {
                    continue;
                }

                int _val = cur.sV;
                if (m[_x][_y] != '+' && m[_x][_y] != '-') {
                    if (m[cur.sX][cur.sY] == '+') {
                        _val += m[_x][_y] - '0';
                    } else {
                        _val -= m[_x][_y] - '0';
                    }
                }
                if (_val >= MAXV || _val < -MAXV) {
                    continue;
                }

                if (can[_val + MAXV][_x][_y] == "" ||
                    solLess(can[cur.sV + MAXV][cur.sX][cur.sY] + m[_x][_y], can[_val + MAXV][_x][_y])) {
                    can[_val + MAXV][_x][_y] = can[cur.sV + MAXV][cur.sX][cur.sY] + m[_x][_y];
                    Q.push(make_stare(_val, _x, _y));
                }
            }
        }

        for (; Queries; Queries -= 1) {
            int val;
            scanf("%d", &val);
            string rez = "";
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (can[val + MAXV][i][j] == "") {
                        continue;
                    }

                    if (rez == "" || solLess(can[val + MAXV][i][j], rez)) {
                        rez = can[val + MAXV][i][j];
                    }
                }
            }
            printf("%s\n", rez.c_str());
        }
    }

    return 0;
}


