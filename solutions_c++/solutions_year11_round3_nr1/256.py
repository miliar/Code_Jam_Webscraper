#include <iostream>
#include <cstdio>
#include <cstring>

#define MAX 110
#define IN_MAP(x, y) ((x) >= 0 && (x) < n && (y) >= 0 && (y) < m)

using namespace std;

const int dx[] = {0, 0, 1, 1};
const int dy[] = {0, 1, 0, 1};
const char red[] = {"/\\\\/"};

char mat[MAX][MAX];
int n, m;

bool cover(const int x, const int y) {
    int i, tx, ty;

    for (i = 0; i < 4; i++) {
        tx = x + dx[i];
        ty = y + dy[i];
        if (IN_MAP(tx, ty) && mat[tx][ty] == '#') {
            mat[tx][ty] = red[i];
        } else {
            return false;
        }
    }

    return true;
}

bool solve() {
    int i, j;

    for (i = 0; i < n; i++) {
        for (j = 0; j < m; j++) {
            if (mat[i][j] == '#') {
                if (!cover(i, j)) return false;
            }
        }
    }

    return true;
}

int main() {
    int t, cnt = 1, i;

    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; i++) scanf("%s", mat[i]);
        printf("Case #%d:\n", cnt++);
        if (!solve()) {
            printf("Impossible\n");
        } else {
            for (i = 0; i < n; i++) {
                printf("%s\n", mat[i]);
            }
        }
    }

    return 0;
}
