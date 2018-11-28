#include <cstdio>

int r, c;
char tab[123][123];

bool valid(int i, int j) {
    return i >= 0 && i < r && j >= 0 && j < c;
}

bool replace(int i, int j) {
    tab[i][j] = '/';
    if (valid(i, j+1) && tab[i][j+1] == '#') tab[i][j+1] = '\\'; else return false;
    if (valid(i+1, j) && tab[i+1][j] == '#') tab[i+1][j] = '\\'; else return false;
    if (valid(i+1, j+1) && tab[i+1][j+1] == '#') tab[i+1][j+1] = '/'; else return false;
    return true;
}

int main() {
    int nt, cases = 1;
    scanf(" %d", &nt);
    while (nt--) {
        scanf(" %d%d", &r, &c);
        for (int i = 0; i < r; i++)
            scanf(" %s", tab[i]);
        bool res = true;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                if (tab[i][j] == '#')
                    res = res && replace(i, j);
        printf("Case #%d:\n", cases++);
        if (!res)
            printf("Impossible\n");
        else
            for (int i = 0; i < r; i++)
                printf("%s\n", tab[i]);
    }

    return 0;
}
