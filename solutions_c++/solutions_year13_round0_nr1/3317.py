#include <iostream>
#include <functional>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

bool check(int a) {
    return a < 4 && a >= 0;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    string tmp;
    scanf("%d\n", &t);

    for (int h = 1; h <= t; h++) {
        string map[4];
        bool full = true, winner[2] = {false, false};

        for (int i = 0; i < 4; i++) 
            getline(cin, map[i]);

        getline(cin, tmp);

        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (map[i][j] == '.')
                    full = false;
                
        int dx[4] = {0, 1, 1, -1},
            dy[4] = {1, 0, 1, -1};

        for (int i = 0; i < 4; i++) {
            bool win = true;
            for (int j = 0; j < 4; j++)
                if (map[i][j] != 'X' && map[i][j] != 'T') {
                    win = false;
                    break;
                }

            if (win) winner[0] = true;

            win = true;
            for (int j = 0; j < 4; j++)
                if (map[i][j] != 'O' && map[i][j] != 'T') {
                    win = false;
                    break;
                }

            if (win) winner[1] = true;
        }

        for (int j = 0; j < 4; j++) {            
            bool win = true;
            for (int i = 0; i < 4; i++)
                if (map[i][j] != 'X' && map[i][j] != 'T') {
                    win = false;
                    break;
                }

            if (win) winner[0] = true;

            win = true;
            for (int i = 0; i < 4; i++)
                if (map[i][j] != 'O' && map[i][j] != 'T') {
                    win = false;
                    break;
                }

            if (win) winner[1] = true;
        }

        bool win = true;
        for (int i = 0; i < 4; i++)
            if (map[i][i] != 'X' && map[i][i] != 'T') {
                win = false;
                break;
            }

        if (win) winner[0] = true;

        win = true;
        for (int i = 0; i < 4; i++)
            if (map[i][i] != 'O' && map[i][i] != 'T') {
                win = false;
                break;
            }

        if (win) winner[1] = true;

        win = true;
        for (int i = 0; i < 4; i++)
            if (map[3 - i][i] != 'X' && map[3 - i][i] != 'T') {
                win = false;
                break;
            }

        if (win) winner[0] = true;

        win = true;
        for (int i = 0; i < 4; i++)
            if (map[3 - i][i] != 'O' && map[3 - i][i] != 'T') {
                win = false;
                break;
            }

        if (win) winner[1] = true;

        cout << "Case #" << h << ": " ;
        if (winner[0])
            cout << "X won" << endl;
        else if (winner[1])
            cout << "O won" << endl;
        else if (full)
            cout << "Draw" << endl;
        else 
            cout << "Game has not completed" << endl;

    }
}

    
