#include <cstdio>
#include <cstring>
using namespace std;

const int maxn = 100;
char map[maxn][maxn];
int m, n;

FILE *fin = fopen("input.txt", "r");
FILE *fout = fopen("output.txt", "w");

void init()
{
    fscanf(fin, "%d%d", &m, &n);
    for (int i = 0; i < m; ++i) {
        fscanf(fin, "%s", map[i]);
    }
}

bool check(int x, int y )
{
    return (map[x][y] == '#' && (x + 1 < m && map[x + 1][y] == '#') && (y + 1 < n && map[x][y + 1] == '#') && (x + 1 < m && y + 1 < n && map[x + 1][y + 1] == '#'));
}

void fill(int x, int y)
{
    map[x][y] = '/';
    map[x + 1][y] = '\\';
    map[x][y + 1] = '\\';
    map[x + 1][y + 1] = '/';
}

bool run()
{
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (map[i][j] == '#') {
                if (check(i, j)) {
                    fill(i, j);
                }
                else {
                    return false;
                }
            }
        }
    }
    for (int i = 0; i < m; ++i) {
        fprintf(fout, "%s\n", map[i]);
    }
    return true;
}

int main(void)
{
    int t;
    fscanf(fin, "%d", &t);
    for (int i = 1; i <= t; ++i) {
        fprintf(fout, "Case #%d:\n", i);
        init();
        if (!run()) {
            fprintf(fout, "Impossible\n");
        }
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
