#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

enum GameStatus {
    X_WON,
    O_WON,
    DRAW,
    GAME_HAS_NOT_COMPLETED,
    OTHER
};

class Game {
    private:
    string field[4];

    public:
    Game() {
        for (int i = 0; i < 4; i++)
            cin >> field[i];
    }

    void transpone() {
        for (int i = 0; i < 4; i++)
            for (int j = i; j < 4; j++)
                swap(field[i][j], field[j][i]);
    }

    GameStatus getRowsStatus() {
        for (int i = 0; i < 4; i++) {
            if (field[0][i] == 'X' or field[0][i] == 'O') {
                bool flag = true;
                for (int j = 1; j < 4; j++)
                    flag &= (field[0][i] == field[j][i] or field[j][i] == 'T');
                if (flag) {
                    if (field[0][i] == 'X')
                        return X_WON;
                    else
                        return O_WON;
                }
            }
            if (field[0][i] == 'T') {
                if (field[1][i] == field[2][i] == field[3][i] and field[1][i] != '.') {
                    if (field[1][i] == 'X')
                        return X_WON;
                    else
                        return O_WON;
                }
            }
        }
        return OTHER;
    }

    GameStatus getColumnsStatus() {
        transpone();
        GameStatus temp = getRowsStatus();
        transpone();
        return temp;
    }

    GameStatus getLeftDiagStatus() {
        if (field[0][0] == 'T') {
            if (field[1][1] == field[2][2] == field[3][3]) {
                if (field[1][1] == 'X')
                    return X_WON;
                else
                    return O_WON;
            }
        } else if (field[0][0] == '.')
            return OTHER;
        else {
            bool flag = true;
            for (int j = 1; j < 4; j++)
                flag &= (field[0][0] == field[j][j] or field[j][j] == 'T');
            if (flag) {
                if (field[0][0] == 'X')
                    return X_WON;
                else
                    return O_WON;
            }
        }
        return OTHER;
    }

    void print() {
        for (int i = 0; i < 4; i++)
            cout << field[i] << endl;
        cout << endl;
    }

    GameStatus getRightDiagStatus() {
        if (field[3][0] == 'T') {
            if (field[2][1] == field[1][2] and field[1][2] == field[0][3] and field[2][1] != '.') {
                if (field[2][1] == 'X')
                    return X_WON;
                else
                    return O_WON;
            }
        } else if (field[3][0] == '.')
            return OTHER;
        else {
            bool flag = true;
            for (int j = 1; j < 4; j++)
                flag &= (field[3][0] == field[3 - j][j] or field[3 - j][j] == 'T');
            if (flag) {
                if (field[3][0] == 'X')
                    return X_WON;
                else
                    return O_WON;
            }
        }
        return OTHER;
    }

    GameStatus getGameStatus() {
        GameStatus temp = getRowsStatus();
        if (temp == OTHER) {
            temp = getColumnsStatus();
            if (temp == OTHER) {
                temp = getLeftDiagStatus();
                if (temp == OTHER) {
                    temp = getRightDiagStatus();
                    if (temp == OTHER) {
                        for (int i = 0; i < 4; i++)
                            for (int j = 0; j < 4; j++)
                                if (field[i][j] == '.')
                                    return GAME_HAS_NOT_COMPLETED;
                        return DRAW;
                    } else
                        return temp;
                } else
                    return temp;
            } else
                return temp;
        } else
            return temp;
    }

    string decodeAnswer() {
        GameStatus temp = getGameStatus();
        string ans;
        switch (temp) {
            case X_WON:                 ans = "X won";  break;
            case O_WON:                 ans = "O won";  break;
            case DRAW:                  ans = "Draw";   break;
            case GAME_HAS_NOT_COMPLETED:ans = "Game has not completed"; break;
        }
        return ans;
    }
};

string tostring(int i) {
    stringstream ss;
    ss << i;
    return ss.str();
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    cin >> T;
    Game current;
    cout << "Case #1: " + current.decodeAnswer() << endl;

    for (int i = 0; i < T - 1; i++) {
        current = Game();
        string ans = "Case #";
        ans += tostring(i + 2);
        ans += ": ";
        cout << ans + current.decodeAnswer() << endl;
    }


    return 0;
}
