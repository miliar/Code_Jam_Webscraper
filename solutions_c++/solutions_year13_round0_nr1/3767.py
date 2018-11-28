#include <cstdio>

int tests;
char t[4][5];
char cnt[256];
char winner;

bool gameWon()
{
    for (int x=0; x<4; ++x) {
        cnt['O'] = cnt['X'] = cnt['T'] = 0;
        for (int y=0; y<4; ++y) ++cnt[t[x][y]];
        if (cnt['X'] == 4 || (cnt['X'] == 3 && cnt['T'])) return winner = 'X';
        if (cnt['O'] == 4 || (cnt['O'] == 3 && cnt['T'])) return winner = 'O';
    }
    for (int x=0; x<4; ++x) {
        cnt['O'] = cnt['X'] = cnt['T'] = 0;
        for (int y=0; y<4; ++y) ++cnt[t[y][x]];
        if (cnt['X'] == 4 || (cnt['X'] == 3 && cnt['T'])) return winner = 'X';
        if (cnt['O'] == 4 || (cnt['O'] == 3 && cnt['T'])) return winner = 'O';
    }
    cnt['O'] = cnt['X'] = cnt['T'] = 0;
    for (int i=0; i<4; ++i) ++cnt[t[i][i]];
    if (cnt['X'] == 4 || (cnt['X'] == 3 && cnt['T'])) return winner = 'X';
    if (cnt['O'] == 4 || (cnt['O'] == 3 && cnt['T'])) return winner = 'O';
    cnt['O'] = cnt['X'] = cnt['T'] = 0;
    for (int i=0; i<4; ++i) ++cnt[t[i][3-i]];
    if (cnt['X'] == 4 || (cnt['X'] == 3 && cnt['T'])) return winner = 'X';
    if (cnt['O'] == 4 || (cnt['O'] == 3 && cnt['T'])) return winner = 'O';
    return false;
}

int main()
{
    scanf("%d", &tests);
    for(int tst=1; tst<=tests; ++tst) {
        scanf("%s%s%s%s", t[0], t[1], t[2], t[3]);
        cnt['.'] = 0;
        printf("Case #%d: ", tst);
        if (gameWon()) printf("%c won\n", winner);
        else if (cnt['.']) printf("Game has not completed\n");
        else printf("Draw\n");
    }
}
