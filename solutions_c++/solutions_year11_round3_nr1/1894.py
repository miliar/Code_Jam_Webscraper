#include <iostream>
#include <string>
#include <vector>

using namespace std;

const string RED[] = { "/\\", "\\/" };

int n, m;
char f[51][51];

bool good(int x, int y) {
    return (x >= 0 && x < n && y >= 0 && y < m);
}

bool solve() {
    for (int x = 0; x < n; ++x)
        for (int y = 0; y < m; ++y)
            if (f[x][y] == '#') {
                for (int dx = 0; dx < 2; ++dx)
                    for (int dy = 0; dy < 2; ++dy) {
                        if (!good(x + dx, y + dy))
                            return false;
                        if (f[x + dx][y + dy] != '#')
                            return false;
                        f[x + dx][y + dy] = RED[dx][dy];
                    }
            }
    return true;
}

int main() {
    int T;
    cin >> T;
    for (int test_id = 1; test_id <= T; ++test_id) {
        scanf("%d%d\n", &n, &m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j)
                scanf("%c", &f[i][j]);
            scanf("\n");
        }

        printf("Case #%d:\n", test_id);
        if (solve()) {
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < m; ++j)
                    printf("%c", f[i][j]);
                printf("\n");
            }
        } else {
            printf("Impossible\n");
        }
    }
    return 0;
}
