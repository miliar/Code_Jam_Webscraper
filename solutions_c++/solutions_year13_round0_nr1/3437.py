#include <cstdio>
using namespace std;

char field[4][4];

bool check_dir(char ch, bool dir)
{
    for (int i = 0; i < 4; ++i) {
        bool win = true;
        for (int j = 0; j < 4; ++j) {
            int c = dir ? field[i][j] : field[j][i];
            if (c == '.' || (c != 'T' && c != ch))
                win = false;
        }
        if (win) return true;
    }
    return false;
}

bool check_diag(char ch, bool dir)
{
    for (int i = 0; i < 4; ++i) {
        char c = dir ? field[i][i] : field[i][3 - i];
        if (c != 'T' && c != ch) return false;
    }
    return true;
}

bool check(char ch)
{
    return check_dir(ch, false) || check_dir(ch, true) || check_diag(ch, false) || check_diag(ch, true);
}

int main()
{
    int T; scanf("%d", &T);
    for (int testcase = 1; testcase <= T; ++testcase) {
        printf("Case #%d: ", testcase);

        int count = 0;
        for (int y = 0; y < 4; ++y) {
            for (int x = 0; x < 4; ++x) {
                scanf(" %c", &field[y][x]);
                if (field[y][x] != '.') ++count;
            }
        }

        if (check('X'))
            puts("X won");
        else if (check('O'))
            puts("O won");
        else if (count == 16)
            puts("Draw");
        else
            puts("Game has not completed");
    }
}
