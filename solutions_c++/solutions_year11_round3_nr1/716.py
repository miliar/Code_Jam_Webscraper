#include <cstdio>

using namespace std;

int rows, cols;
char grid[64][64];

bool go() {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (grid[i][j] == '#') {
                if (i + 1 >= rows || j + 1 >= cols || grid[i + 1][j] != '#' || grid[i][j + 1] != '#' || grid[i + 1][j + 1] != '#') return false;
                grid[i][j] = '/';
                grid[i][j + 1] = '\\';
                grid[i + 1][j] = '\\';
                grid[i + 1][j + 1] = '/';
            }
        }
    }

    return true;
}

int main() {
    int kases;

    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%d%d", &rows, &cols);
        for (int i = 0; i < rows; ++i) scanf("%s", grid[i]);

        printf("Case #%d:\n", kase);
        if (go()) {
            for (int i = 0; i < rows; ++i) printf("%s\n", grid[i]);
        } else {
            printf("Impossible\n");
        }
    }

    return 0;
}
