#include <iostream>
#include <utility>
using namespace std;

const int eage = 4;
const string msg[] = {
    "X won",
    "O won",
    "Game has not completed",
    "Draw",
};

void print_result(const int i, const string& s) {
    cout << "Case #" << i << ": " << s << endl;
}

bool check_straight_line(const int x, const int y, const string m[], const char c) {
    int i = 0;
    for(i = 0; i < eage; ++i) {
        if(m[y][i] == 'T') continue;
        if(m[y][i] == '.' || m[y][i] != c) break;
    }
    if(i == eage) return true;

    for(i = 0; i < eage; ++i) {
        if(m[i][x] == 'T') continue;
        if(m[i][x] == '.' || m[i][x] != c) break;
    }
    if(i == eage) return true;

    return false;
}

bool check_diagonal_line(const string m[], const char c) {
    int i = 0, j = 0;
    for(i = 0, j = 0; i < eage; ++i, ++j) {
        if(m[j][i] == 'T') continue;
        if(m[j][i] == '.' || m[j][i] != c) break;
    }
    if(i == eage) return true;

    for(i = 0, j = 3; i < eage; ++i, --j) {
        if(m[j][i] == 'T') continue;
        if(m[j][i] == '.' || m[j][i] != c) break;
    }
    if(i == eage) return true;

    return false;
}

int main(void) {
    int t;
    cin >> t;
    for(int n = 1; n <= t; ++n) {
        string board[eage];
        for(int i = 0; i < eage; ++i) {
            cin >> board[i];
        }

        if(check_diagonal_line(board, 'X')) {
            print_result(n, msg[0]);
            continue;
        } else if(check_diagonal_line(board, 'O')) {
            print_result(n, msg[1]);
            continue;
        }

        bool won = false;
        for(int i = 0; !won && i < eage; ++i) {
            if(check_straight_line(i, 0, board, 'X')) {
                won = true;
                print_result(n, msg[0]);
            } else if(check_straight_line(i, 0, board, 'O')) {
                won = true;
                print_result(n, msg[1]);
            }
        }
        for(int i = 1; !won && i < eage; ++i) {
            if(check_straight_line(0, i, board, 'X')) {
                won = true;
                print_result(n, msg[0]);
            } else if(check_straight_line(0, i, board, 'O')) {
                won = true;
                print_result(n, msg[1]);
            }
        }
        if(won) continue;

        bool finished = true;
        for(int i = 0; finished && i < eage; ++i) {
            for(int j = 0; finished && j < eage; ++j) {
                if(board[i][j] == '.') {
                    finished = false;
                }
            }
        }

        if(finished) {
            print_result(n, msg[3]);
        } else {
            print_result(n, msg[2]);
        }
    }
    return 0;
}
