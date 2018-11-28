#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <sstream>
#define inf 1000000007
#define eps 1e-8
#define M 105
#define N 2505
#define For(i,a,b) for(int i=(a);i<(b);i++)
using namespace std;
char s[5][5];

int main() {
    int T;
    scanf("%d", &T);
    freopen("123.txt", "w", stdout);
    int cs = 0;
    while (T--) {
        cs++;
        int a = 0, b = 0, c = 0;

        For(i, 0, 4)
        For(j, 0, 4) {
            scanf(" %c", &s[i][j]);
            if (s[i][j] == '.')
                c++;
        }
        int ta, tb;

        For(i, 0, 4) {
            ta = 0, tb = 0;
            For(j, 0, 4)
            if (s[i][j] == 'X')
                ta++;
            else if (s[i][j] == 'O')
                tb++;
            else if (s[i][j] == 'T')
                ta++, tb++;
            a = max(ta, a);
            b = max(tb, b);
        }

        For(i, 0, 4) {
            ta = 0, tb = 0;
            For(j, 0, 4)
            if (s[j][i] == 'X')
                ta++;
            else if (s[j][i] == 'O')
                tb++;
            else if (s[j][i] == 'T')
                ta++, tb++;


            a = max(ta, a);
            b = max(tb, b);
        }
        ta = 0, tb = 0;
        For(i, 0, 4)
        if (s[i][i] == 'X')
            ta++;
        else if (s[i][i] == 'O')
            tb++;
        else if (s[i][i] == 'T')
            ta++, tb++;
        a = max(ta, a);
        b = max(tb, b);
        ta = 0, tb = 0;
        For(i, 0, 4)
        if (s[i][4 - i - 1] == 'X')
            ta++;
        else if (s[i][4 - 1 - i] == 'O')
            tb++;
        else if (s[i][4 - i - 1] == 'T')
            ta++, tb++;
        a = max(ta, a);
        b = max(tb, b);
        printf("Case #%d: ", cs);
        if (a == 4) {
            printf("X won");
        } else if (b == 4)
            printf("O won");
        else if (c == 0)
            printf("Draw");
        else printf("Game has not completed");
        printf("\n");

    }

    return 0;
}