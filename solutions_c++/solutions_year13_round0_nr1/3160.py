#include <iostream>
#include <stdio.h>
#include <string>
using namespace std;

void convertTtoC(string str[5], char c) {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (str[i][j] == 'T')
                str[i][j] = c;
    return;
}

int notCompleted(string str[5]) {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (str[i][j] == '.')
                return 1;
    return 0;
}

int checkWinner(string str[5], char c) {
    string temp[5];
    temp[0] = str[0];
    temp[1] = str[1];
    temp[2] = str[2];
    temp[3] = str[3];
    convertTtoC(temp, c);
    for (int i = 0; i < 4; i++) {
        if (temp[i][0] == c && temp[i][1] == c && temp[i][2] == c && temp[i][3] == c)
            return 1;
    }
    for (int i = 0; i < 4; i++)
        if (temp[0][i] == c && temp[1][i] == c && temp[2][i] == c && temp[3][i] == c)
            return 1;
    if (temp[0][0] == c && temp[1][1] == c && temp[2][2] == c && temp[3][3] == c)
        return 1;
    if (temp[0][3] == c && temp[1][2] == c && temp[2][1] == c && temp[3][0] == c)
        return 1;
    return 0;
}

string cases[5] = {"X won\n", "O won\n", "Draw\n", "Game has not completed\n"};

int main(void) {
    int t, winner;
    string str[5];

    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w+", stdout);

    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> str[0] >> str[1] >> str[2] >> str[3];

        winner = checkWinner(str, 'X');
        if (winner == 1)
            cout << "Case #" << i << ": " << cases[0];
        else {
            winner = checkWinner(str, 'O');
            if (winner == 1)
                cout << "Case #" << i << ": " << cases[1];
            else {
                if (notCompleted(str) == 1)
                    cout << "Case #" << i << ": " << cases[3];
                else
                    cout << "Case #" << i << ": " << cases[2];
            }
        }
    }
    return 0;
}