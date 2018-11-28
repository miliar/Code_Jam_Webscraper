#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <limits>
#include <utility>
#include <cmath>
#include <string>

using namespace std;

string tictactoe()
{
    vector<string> board(4);
    string dummy;
    getline(cin, dummy);
    for (int i = 0; i < 4; ++i)
        getline(cin, board[i]);
    
//    for (int r = 0; r < 4; ++r)
//        cout << board[r] << endl;
    
    int x = 0, o = 0, dot = 0;
    
    for (int r = 0; r < 4; ++r) {
        x = 0;
        o = 0;
        for (int c = 0; c < 4; ++c) {
            if (board[r][c] == '.')
                dot++;
            else if (board[r][c] == 'X')
                x++;
            else if (board[r][c] == 'O')
                o++;
            else if (board[r][c] == 'T') {
                x++;
                o++;
            }
        }
        if (x == 4)
            return "X won";
        else if (o == 4)
            return "O won";
    }

    for (int c = 0; c < 4; ++c) {
        x = 0;
        o = 0;
        for (int r = 0; r < 4; ++r) {
            if (board[r][c] == 'X')
                x++;
            else if (board[r][c] == 'O')
                o++;
            else if (board[r][c] == 'T') {
                x++;
                o++;
            }
        }
        if (x == 4)
            return "X won";
        else if (o == 4)
            return "O won";
    }

    x = 0;
    o = 0;
    for (int r = 0; r < 4; ++r) {
        if (board[r][r] == 'X')
            x++;
        else if (board[r][r] == 'O')
            o++;
        else if (board[r][r] == 'T') {
            x++;
            o++;
        }
    }
    if (x == 4)
        return "X won";
    else if (o == 4)
        return "O won";
    
    x = 0;
    o = 0;
    for (int r = 0; r < 4; ++r) {
        if (board[r][3 - r] == 'X')
            x++;
        else if (board[r][3 - r] == 'O')
            o++;
        else if (board[r][3 - r] == 'T') {
            x++;
            o++;
        }
    }
    if (x == 4)
        return "X won";
    else if (o == 4)
        return "O won";
    
    if (dot > 0)
        return "Game has not completed";
    return "Draw";
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;

    for (int t = 0; t < T; ++t) {
        string output = tictactoe();

        cout << "Case #" << t + 1 << ": " << output << endl;
    }

    return 0;
}
