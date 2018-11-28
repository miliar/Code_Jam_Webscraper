#include <cstdio>
#include <cstdlib>

char plansza[51][51];

bool check(int r, int c) {
    for (int y = 0; y < r; ++y) {
        for (int x = 0; x < c; ++x) {
            if (plansza[y][x] == '#') {
                if (x < c - 1 && plansza[y][x + 1] == '#' && y < r - 1 && plansza[y + 1][x] == '#' && plansza[y + 1][x + 1] == '#') {
                    plansza[y][x] = '/';
                    plansza[y][x + 1] = '\\';
                    plansza[y + 1][x] = '\\';
                    plansza[y + 1][x + 1] = '/';
                } else {
                    return false;
                }
            }
        }
    }
    return true;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        int r, c;
        scanf("%d%d", &r, &c);

        for (int j = 0; j < r; ++j) {
            scanf("%s", &plansza[j]);
        }
        if (check(r, c) == false) {
            printf("Case #%d:\nImpossible\n", i);
        } else {
            printf("Case #%d:\n", i);
            for (int y = 0; y < r; ++y) {
                printf("%s\n", plansza[y]);
            }
        }



    }
    return 0;
}