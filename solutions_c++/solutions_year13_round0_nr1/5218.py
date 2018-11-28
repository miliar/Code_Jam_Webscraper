#include <string>
#include <iostream>
#include <stdio.h>
#include <fstream>
#include <unistd.h>
using namespace std;

char sta[4][4];

int judge(){  // 0: draw, 1: x win, 2: o win, 3: not completed
    for (int i = 0; i < 4; i++){
        int xcnt = 0, ocnt = 0;
        for (int j = 0; j < 4; j++){
            if (sta[i][j] == 'X' || sta[i][j] == 'T')
                xcnt++;
            if (sta[i][j] == 'O' || sta[i][j] == 'T')
                ocnt++;
        }
        if (xcnt == 4)
            return 1;
        if (ocnt == 4)
            return 2;
    }

    for (int j = 0; j < 4; j++){
        int xcnt = 0, ocnt = 0;
        for (int i = 0; i < 4; i++){
            if (sta[i][j] == 'X' || sta[i][j] == 'T')
                xcnt++;
            if (sta[i][j] == 'O' || sta[i][j] == 'T')
                ocnt++;
        }
        if (xcnt == 4)
            return 1;
        if (ocnt == 4)
            return 2;
    }

    int xcnt = 0, ocnt = 0;
    for (int i = 0; i < 4; i++){
        if (sta[i][i] == 'X' || sta[i][i] == 'T')
            xcnt++;
        if (sta[i][i] == 'O' || sta[i][i] == 'T')
            ocnt++;
    }
    if (xcnt == 4)
        return 1;
    if (ocnt == 4)
        return 2;

    xcnt = 0, ocnt = 0;
    for (int i = 0; i < 4; i++){
        if (sta[i][3-i] == 'X' || sta[i][3-i] == 'T')
            xcnt++;
        if (sta[i][3-i] == 'O' || sta[i][3-i] == 'T')
            ocnt++;
    }
    if (xcnt == 4)
        return 1;
    if (ocnt == 4)
        return 2;

    bool full = true;
    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++)
            if (sta[i][j] == '.'){
                full = false;
                break;
            }
        if (!full)
            break;
    }

    if (full)
        return 0;
    return 3;
}

int main(){
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int cc = 1; cc <= t; cc++){
        for (int i = 0; i < 4; i++){
            for (int j = 0; j < 4; j++)
                cin >> sta[i][j];
            //getchar();
        }

        switch (judge()){
            case 0:
                printf("Case #%d: Draw\n", cc);
                break;
            case 1:
                printf("Case #%d: X won\n", cc);
                break;
            case 2:
                printf("Case #%d: O won\n", cc);
                break;
            case 3:
                printf("Case #%d: Game has not completed\n", cc);
                break;
        }
    }

    return 0;
}
