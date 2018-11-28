#include <cstdio>

char ttt[5][5];

int main()
{
    //freopen("A-small-attempt0.in", "r", stdin);
    //freopen("A.txt", "w", stdout);
    int n, nc, row, col;
    bool x, o, finish;
    char cur;
    scanf("%d", &n);
    for (nc=1;nc<=n;nc++) {
        for (row=0;row<4;row++) {
            scanf("%s", ttt[row]);
        }
        x = false;
        o = false;
        finish = true;
        for (row=0;row<4;row++) {
            if (ttt[row][0]=='.')
                continue;
            if (ttt[row][0]=='T')
                cur = ttt[row][1];
            else
                cur = ttt[row][0];
            //printf("%d %c\n", row, cur);
            for (col=1;col<4;col++) {
                if (ttt[row][col]!=cur && ttt[row][col]!='T')
                    break;
            }
            if (col==4) {
                if (cur=='X')
                    x = true;
                else
                    o = true;
                break;
            }
        }
        if (!x && !o) {
            for (col=0;col<4;col++) {
                if (ttt[0][col]=='.')
                    continue;
                if (ttt[0][col]=='T')
                    cur = ttt[1][col];
                else
                    cur = ttt[0][col];
                for (row=1;row<4;row++) {
                    if (ttt[row][col]!=cur && ttt[row][col]!='T')
                        break;
                }
                if (row==4) {
                    if (cur=='X')
                        x = true;
                    else
                        o = true;
                    break;
                }
            }
        }
        if (!x && !o) {
            if (ttt[0][0]!='.') {
                if (ttt[0][0]=='T')
                    cur = ttt[1][1];
                else
                    cur = ttt[0][0];
                for (row=1;row<4;row++) {
                    if (ttt[row][row]!=cur && ttt[row][row]!='T')
                        break;
                }
                if (row==4) {
                    if (cur=='X')
                        x = true;
                    else
                        o = true;
                }
            }
            if (ttt[0][3]!='.') {
                if (ttt[0][3]=='T')
                    cur = ttt[1][2];
                else
                    cur = ttt[0][3];
                for (row=1;row<4;row++) {
                    if (ttt[row][3-row]!=cur && ttt[3-row][row]!='T')
                        break;
                }
                if (row==4) {
                    if (cur=='X')
                        x = true;
                    else
                        o = true;
                }
            }
        }
        if (!x && !o) {
            for (row=0;row<4;row++) {
                for (col=0;col<4;col++) {
                    if (ttt[row][col]=='.')
                        break;
                }
                if (col!=4)
                    break;
            }
            if (row!=4)
                finish = false;
        }/*
        if (x) {
            printf("x true\n");
        } else {
            printf("x false\n");
        }
        if (o) {
            printf("o true\n");
        } else {
            printf("o false\n");
        }
        if (finish) {
            printf("f true\n");
        } else {
            printf("f false\n");
        }*/
        printf("Case #%d: ", nc);
        if (x) {
            printf("X won\n");
        } else if (o) {
            printf("O won\n");
        } else if (finish) {
            printf("Draw\n");
        } else {
            printf("Game has not completed\n");
        }
    }
}
