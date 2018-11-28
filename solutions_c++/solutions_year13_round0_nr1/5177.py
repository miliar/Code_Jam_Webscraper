#include <cstdio>

#define EQU(x, i, j) (map[i][j] == (x) || map[i][j] == 'T')

bool check(char x, char map[4][5]) {
    int i, j;
    bool flag;
    for (i = 0; i < 4; i++) {
        flag = true;
        for (j = 0; j < 4; j++) {
            if(!EQU(x, i, j)){
                flag = false;
                break;
            }
        }
        if (flag) return true;

        flag = true;
        for (j = 0; j < 4; j++) {
            if(!EQU(x, j, i)){
                flag = false;
                break;
            }
        }
        if (flag) return true;
    }

    flag = true;
    for (i = 0; i < 4; i++) {
        if (!EQU(x, i, i)){
            flag = false;
            break;
        }
    }
    if (flag) return true;

    flag = true;
    for (i = 0; i < 4; i++) {
        if (!EQU(x, i, 3 - i)){
            flag = false;
            break;
        }
    }
    return flag;
}

bool finished(char map[4][5]) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++)
            if(map[i][j] == '.')return false;
    }
    return true;
}

void process(int c, char map[4][5]) {
    if (check('X', map))
        printf("Case #%d: X won\n", c);
    else if (check('O', map))
        printf("Case #%d: O won\n", c);
    else if (finished(map))
        printf("Case #%d: Draw\n", c);
    else
        printf("Case #%d: Game has not completed\n", c);
}

int main() {
    int n;
    char map[4][5] = {0};

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 4; j++) {
            scanf("%s", map[j]);
        }

        process(i + 1, map);
    }

    return 0;
}
