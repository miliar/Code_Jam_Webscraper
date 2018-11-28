#include <cstdio>
#include <cstring>

const int MAX_N = 40000;
const int MAX_W = 150;
const int dir[][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} };

struct DSet {
    int p[MAX_N];
    void init(int size = MAX_N) { memset(p, 0xff, sizeof(int) * size); };
    inline int find(int x) { return (p[x] == -1) ? x : (p[x] = find(p[x])); };
    void setFriend(int i, int j) { if (find(i) != find(j)) p[find(i)] = find(j); };
    bool isFriend(int i, int j) { return find(i) == find(j); };
};

DSet dset;
int t, T, h, w, i, j, k, tonum, minn, nx, ny, count, id;
int mat[MAX_W][MAX_W];
char conn[MAX_N];
int to[10];

int main() {
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        scanf("%d%d", &h, &w);
        for (i = 0; i < h; i++)
            for (j = 0; j < w; j++)
                scanf("%d", &mat[i][j]);
        dset.init(h * w);
        for (i = 0; i < h; i++)
            for (j = 0; j < w; j++) {
                tonum = 0;
                minn = mat[i][j] - 1;
                for (k = 0; k < 4; k++) {
                    nx = i + dir[k][0];
                    ny = j + dir[k][1];
                    if (nx < 0 || nx >= h || ny < 0 || ny >= w)
                        continue;
                    if (mat[nx][ny] < minn) {
                        tonum = 0;
                        minn = mat[nx][ny];
                    }
                    if (mat[nx][ny] == minn)
                        to[tonum++] = nx * w + ny;
                }
                if (tonum > 0) {
                    dset.setFriend(to[0], i * w + j);
                }
            }
        memset(conn, '*', sizeof(conn));
        count = 0;
        printf("Case #%d:\n", t);
        for (i = 0; i < h; i++) {
            for (j = 0; j < w; j++) {
                id = dset.find(i * w + j);
                if (conn[id] == '*') {
                    conn[id] = 'a' + count;
                    count++;
                }
                putchar(conn[id]);
                putchar(' ');
            }
            putchar('\n');
        }
    }

    return 0;
}

