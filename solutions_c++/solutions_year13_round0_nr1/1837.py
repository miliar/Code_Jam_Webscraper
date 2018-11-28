#include <iostream>

using namespace std;

enum Result {
     Draw, NC, XW, OW
};

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int N;
    scanf("%d", &N);
    for (int caseNumber = 0; caseNumber < N; caseNumber++) {
        string s[4];
        for (int i = 0; i < 4; i++) {
            cin >> s[i];
            while (s[i].empty())
                cin >> s[i];
        }
        Result r = Draw;
        int tx = -1, ty = -1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++) {
                if (s[i][j] == '.')
                    r = NC;
                if (s[i][j] == 'T') {
                    tx = i;
                    ty = j;
                }
            }

        // T = X
        if (tx >= 0 && ty >= 0) {
            s[tx][ty] = 'X';
        }
        // Row, Column
        for (int i = 0; i < 4; i++) {
            char ok1 = s[i][0], ok2 = s[0][i];
            for (int j = 1; j < 4; j++) {
                if (s[i][j] != ok1)
                    ok1 = '.';
                if (s[j][i] != ok2)
                    ok2 = '.';
            }
            if (ok1 == 'X' || ok2 == 'X')
                r = XW;
            if (ok1 == 'O' || ok2 == 'O')
                r = OW;
        }
        // Diagnol
        char ok1 = s[0][0], ok2 = s[0][3];
        for (int i = 1; i < 4; i++) {
            if (s[i][i] != ok1)
                ok1 = '.';
            if (s[i][3 - i] != ok2)
                ok2 = '.';
        }
        if (ok1 == 'X' || ok2 == 'X')
            r = XW;
        if (ok1 == 'O' || ok2 == 'O')
            r = OW;

        // T = O
        if (tx >= 0 && ty >= 0) {
            s[tx][ty] = 'O';
        }
        // Row, Column
        for (int i = 0; i < 4; i++) {
            char ok1 = s[i][0], ok2 = s[0][i];
            for (int j = 1; j < 4; j++) {
                if (s[i][j] != ok1)
                    ok1 = '.';
                if (s[j][i] != ok2)
                    ok2 = '.';
            }
            if (ok1 == 'X' || ok2 == 'X')
                r = XW;
            if (ok1 == 'O' || ok2 == 'O')
                r = OW;
        }
        // Diagnol
        ok1 = s[0][0];
        ok2 = s[0][3];
        for (int i = 1; i < 4; i++) {
            if (s[i][i] != ok1)
                ok1 = '.';
            if (s[i][3 - i] != ok2)
                ok2 = '.';
        }
        if (ok1 == 'X' || ok2 == 'X')
            r = XW;
        if (ok1 == 'O' || ok2 == 'O')
            r = OW;

        switch (r) {
        case Draw:
            printf("Case #%d: Draw\n", caseNumber + 1);
            break;
        case NC:
            printf("Case #%d: Game has not completed\n", caseNumber + 1);
            break;
        case XW:
            printf("Case #%d: X won\n", caseNumber + 1);
            break;
        case OW:
            printf("Case #%d: O won\n", caseNumber + 1);
            break;
        }
    }
}

