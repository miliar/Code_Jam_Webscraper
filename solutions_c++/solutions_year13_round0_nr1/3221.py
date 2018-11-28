#include <iostream>
#include <stdio.h>
using namespace std;

bool isWin(char c, char mat[][5]) {
    int c1 = 0, c2 = 0;
    for (int i=0; i<4; ++i) {
        int cnt = 0, cnt2 = 0;
        for (int j=0; j<4; ++j) {
            if (mat[i][j] == c || mat[i][j] == 'T')
                ++ cnt;
            if (mat[j][i] == c || mat[j][i] == 'T')
                ++ cnt2;
        }
        if (cnt == 4 || cnt2 == 4)
            return true;

        if (mat[i][i] == c || mat[i][i] == 'T')
            ++ c1;
        if (mat[i][3-i] == c || mat[i][3-i] == 'T')
            ++ c2;
    }

    if (c1 == 4 || c2 == 4)
        return true;
    else
        return false;
}

bool isFinish(char mat[][5]) {
    for (int i=0; i<4; ++i)
        for (int j=0; j<4; ++j)
            if (mat[i][j] == '.')
                return false;
    return true;
}

int main () {
    freopen("out.txt", "w", stdout);
    int t;
    char mat[4][5];
    scanf("%d", &t);
    for (int cs=1; cs<=t; ++cs) {
        for (int i=0; i<4; ++i)
            scanf("%s", &mat[i]);

        bool x = isWin('X', mat);
        bool o = isWin('O', mat);

        printf("Case #%d: ", cs);

        if (x || o) {
            if (x)
                printf("X");
            else
                printf("O");

            printf(" won\n");
        } else if (isFinish(mat))
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
    return 0;
}
