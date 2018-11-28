#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)

bool calc(int rows, int cols, vector<string>& tab) {
    char g[100][100] = {};
    For(i, rows) {
        For(j, cols) {
            g[i][j] = tab[i][j];
        }
    }

    For(i, rows) {
        For(j, cols) {
            if (g[i][j] == '#') {
                if (j+1 == cols) return false;
                if (g[i][j+1] != '#') return false;

                if (i+1 == rows) return false;
                if (g[i+1][j] != '#') return false;

                g[i][j] = '/'; g[i][j+1] = '\\';
                g[i+1][j] = '\\'; g[i+1][j+1] = '/';
            }
        }
    }


    For(i, rows) {
        For(j, cols) {
            putchar(g[i][j]);
        }
        puts("");
    }
    return true;
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int rows, cols;
        scanf("%d %d", &rows, &cols);

        vector<string> g;
        char s[1000];
        For(i, rows) {
            scanf("%s", s);
            g.push_back(s);
        }

        printf("Case #%d:\n", cc+1);
        bool ret = calc(rows, cols, g);
        if (!ret)
            puts("Impossible");

    }
}
