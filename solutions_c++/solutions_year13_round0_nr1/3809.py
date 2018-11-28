#include <stdio.h>
#include <string.h>
#include <iostream>
using namespace std;

const int MAX = 5;
char mp[MAX][MAX];

bool check_win(char ch) {
    int j, tcnt;
    for (int i = 0; i < 4; ++i) {
        if (mp[i][0] == ch || mp[i][0] == 'T') {
            tcnt = 0;
            for (j = 0; j < 4; ++j) {
                if (mp[i][j] != ch && mp[i][j] != 'T')
                    break;
                if (mp[i][j] == 'T') {
                    tcnt++;
                    if (tcnt > 1)
                        break;
                }
            }
            if (j == 4)
                return true;
        }
    }
    for (int i = 0; i < 4; ++i) {
        if (mp[0][i] == ch || mp[0][i] == 'T') {
            tcnt = 0;
            for (j = 0; j < 4; ++j) {
                if (mp[j][i] != ch && mp[j][i] != 'T')
                    break;
                if (mp[j][i] == 'T') {
                    tcnt++;
                    if (tcnt > 1)
                        break;
                }
            }
            if (j == 4)
                return true;
        }
    }
    tcnt = 0;
    for (j = 0; j < 4; ++j) {
        if (mp[j][j] != ch && mp[j][j] != 'T')
            break;
        if (mp[j][j] == 'T') {
            tcnt++;
            if (tcnt > 1)
                break;
        }
    }
    if (j == 4)
        return true;
    tcnt = 0;
    for (j = 0; j < 4; ++j) {
        if (mp[j][3 - j] != ch && mp[j][3 - j] != 'T')
            break;
        if (mp[j][3 - j] == 'T') {
            tcnt++;
            if (tcnt > 1)
                break;
        }
    }
    if (j == 4)
        return true;
    return false;
}

bool check_draw()
{
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (mp[i][j] == '.')
                return false;
    return true;
}

//return: 1 x won, 2 o won, 3 draw, 4 not completed
char* work()
{
    char* str = new char[32];
    if (check_win('X')) {
        strcpy(str, "X won");
    }
    else if (check_win('O')) {
        strcpy(str, "O won");
    }
    else if (check_draw()) {
        strcpy(str, "Draw");
    }
    else {
        strcpy(str, "Game has not completed");
    }
}

int main()
{
    freopen("al.in", "r", stdin);
   freopen("al.out", "w", stdout);
    
    int cas;
    scanf("%d", &cas);
    for (int icase = 1; icase <= cas; ++icase) {
        for (int i = 0; i < 4; ++i)
            scanf("%s", &mp[i]);

        printf("Case #%d: %s\n", icase, work());
    }

}
