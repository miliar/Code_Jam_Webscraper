#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>

using namespace std;
int T;
int dx[] = {0, -1, 0, 1, 1, -1, 1, -1};
int dy[] = {-1, 0, 1, 0, 1, -1, -1, 1};

char board[5][5];
void input() {
    getchar();
    for (int i = 0; i < 4; ++ i)
        cin >> board[i];
}

bool game_end() {
    getchar();
    for (int row = 0; row < 4; ++ row)
        for (int col = 0; col < 4; ++ col)
            if (board[row][col] == '.')
                return false;
    return true;
}

void solve(int cn) {
    for (int row = 0; row < 4; ++ row)
        for (int col = 0; col < 4; ++ col) {
            char c = board[row][col];
            if (c != 'X' && c != 'O') continue;
            for (int d = 0; d < 8; ++ d) {
                bool good = true;
                for (int t = 0; t < 4; ++ t) {
                    int nrow = row + dx[d] * t;
                    int ncol = col + dy[d] * t;
                    if (nrow >= 4 || ncol >= 4 || nrow < 0 || ncol < 0
                        || (board[nrow][ncol] != board[row][col] && board[nrow][ncol] != 'T')) {
                        good = false;
                    }
                }
                if (good) {
                    cout << "Case #" << cn << ": " << board[row][col] << " won" << endl;
                    return ;
                }
            }
        }
    cout << "Case #" << cn << ": " << (game_end() ? "Draw" : "Game has not completed") << endl;
}

void print() {
    for (int i = 0; i < 4; ++ i)
        cout << board[i] << endl;
}
int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A.out", "w", stdout);
    cin >> T;
    for (int cn = 1; cn <= T; ++ cn) {
        input();
//        print();
        solve(cn);
    }
    return 0;
}
