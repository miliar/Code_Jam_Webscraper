#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

const int R = 5;
const int C = 5;

int T, cas;
char graph[R][C];
bool end;

bool judge(char);

int main() {
    scanf ("%d", &T);
    for (cas = 1; cas <= T; cas++) {
        end = true;
        while (gets(graph[0]))
            if (graph[0][0] != 0)
                break;
        for (int i = 1; i < 4; i++)
            gets(graph[i]);
        cout << "Case #" << cas << ": ";
        if (judge('O')) {
            cout << "O won" << endl;
            continue;
        }
        if (judge('X')) {
            cout << "X won" << endl;
            continue;
        }
        for (int i = 0; end && i < 4; i++)
            for (int j = 0; end && j < 4; j++)
                if (graph[i][j] == '.') 
                    end = false;
        if (end)
            cout << "Draw" << endl;
        else
            cout << "Game has not completed" << endl;
    }

    return 0;
}

bool judge (char symbol) {
    int cntS, cntT;
    for (int i = 0; i < 4; i++) {
        cntS = cntT = 0;
        for (int j = 0; j < 4; j++) {
            if (graph[i][j] == symbol)
                cntS++;
            if (graph[i][j] == 'T')
                cntT++;
        }
        if (cntS + cntT == 4 && cntT <= 1)
            return true;

        cntS = cntT = 0;
        for (int j = 0; j < 4; j++) {
            if (graph[j][i] == symbol)
                cntS++;
            if (graph[j][i] == 'T')
                cntT++;
        }
        if (cntS + cntT == 4 && cntT <= 1)
            return true;
    }
    cntS = cntT = 0;
    for (int i = 0; i < 4; i++) {
        if (graph[i][i] == symbol)
            cntS++;
        if (graph[i][i] == 'T')
            cntT++;
    }
    if (cntS + cntT == 4 && cntT <= 1)
        return true;

    cntS = cntT = 0;
    for (int i = 0; i < 4; i++) {
        if (graph[i][3 - i] == symbol)
            cntS++;
        if (graph[i][3 - i] == 'T')
            cntT++;
    }
    if (cntS + cntT == 4 && cntT <= 1)
        return true;

    return false;
}
