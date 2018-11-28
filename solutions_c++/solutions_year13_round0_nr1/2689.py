#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
using namespace std;
int T, posi, posj;
char str[4][4];

bool check(char ch) {
    if (posi != -1 && posj != -1) {
        str[posi][posj] = ch;
    }
    bool flag = true;
    for (int i = 0; i < 4; i++) {
        flag = true;
        for (int j = 0; j < 4; j++) {
            if (str[i][j] != ch) {
                flag = false;
                break;
            }
        }
        if (flag) return true;
        flag = true;
        for (int j = 0; j < 4; j++) {
            if (str[j][i] != ch) {
                flag = false;
                break;
            }
        }
        if (flag) return true;
    }
    flag = true;
    for (int i = 0; i < 4; i++) {
        if (str[i][i] != ch) {
            flag = false;
            break;
        }
    }
    if (flag)   return true;
    flag = true;
    for (int i = 0; i < 4; i++) {
        if (str[i][3 - i] != ch) {
            flag = false;
            break;
        }
    }
    if (flag)   return true;
    return false;;
}


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("test.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        int tot = 0;
        posi = posj = -1;
        for (int i = 0; i < 4; i++) {
            scanf("%s", str[i]);
            for (int j = 0; j < 4; j++) {
                if (str[i][j] == '.') tot++;
                if (str[i][j] == 'T') posi = i, posj = j;
            }
        }
        if (check('X')) {
            printf("X won\n");
        } else if (check('O')) {
            printf("O won\n");
        } else if (tot == 0) {
            printf("Draw\n");
        } else {
            printf("Game has not completed\n");
        }

    }

    return 0;
}
