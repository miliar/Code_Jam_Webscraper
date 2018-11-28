#include <cstdio>
#include <iostream>

using namespace std;

char game[4][5];
bool possibleDraw;

bool checkWin(char tmp) {
    bool win;
    for (int i=0;i<4;++i) {
        win = true;
        for (int j=0;j<4;++j) {
            if (game[i][j] == '.')
                possibleDraw = true;
            if (game[i][j] != tmp && game[i][j] != 'T')
                win = false;
        }
        if (win == true) {
            return true;
        }
        else
            win = false;
    }
    for (int i=0;i<4;++i) {
        win = true;
        for (int j=0;j<4;++j) {
            if (game[j][i] != tmp && game[j][i] != 'T')
                win = false;
        }
        if (win == true) {
            return true;
        }
        else
            win = false;
    }
    win = true;
    for (int i=0;i<4;++i) {
        if (game[i][i] != tmp && game[i][i] != 'T')
            win = false;
    }
    if (win == true)
        return true;
    win = true;
    for (int i=0;i<4;++i) {
        if (game[i][3-i] != tmp && game[i][3-i] != 'T')
            win = false;
    }
    if (win == true)
        return true;
    else
        return false;
}

int main() {
    int T;
    scanf("%d",&T);
    for (int caseNumber = 1;caseNumber<=T;++caseNumber) {
        possibleDraw = false;
        for (int i=0;i<4;++i)
            scanf("%s",game[i]);
        if (checkWin('X') == true)
            printf("Case #%d: X won\n",caseNumber);
        else if (checkWin('O') == true)
            printf("Case #%d: O won\n",caseNumber);
        else if (possibleDraw == true)
            printf("Case #%d: Game has not completed\n",caseNumber);
        else
            printf("Case #%d: Draw\n",caseNumber);
        /*for (int i=0;i<4;++i) {
            for (int j=0;j<4;++j)
                cout << game[i][j];
            cout << endl;
        }
        cout << endl;*/
    }
    return 0;
}
