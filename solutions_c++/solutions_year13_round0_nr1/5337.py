#include <string>
#include <vector>
#include <iostream>

using std::string;
using std::vector;

bool won(const char& c, const vector<string>& board) {
    for (int i = 0; i < 4; i++) {
        bool yes = true;
        for (int j = 0; j < 4; j++)
            if (board[i][j] != 'T' && board[i][j] != c)
                yes = false;

        if (yes) return true;
    }

    for (int j = 0; j < 4; j++) {
        bool yes = true;
        for (int i = 0; i < 4; i++)
            if (board[i][j] != 'T' && board[i][j] != c)
                yes = false;

        if (yes) return true;
    }

    bool yes = true;
    for (int i = 0; i < 4; i++)
        if (board[i][i] != 'T' && board[i][i] != c)
            yes = false;

    if (yes) return true;

    yes = true;
    for (int i = 0; i < 4; i++)
        if (board[i][3-i] != 'T' && board[i][3-i] != c)
            yes = false;

    return yes;
}

bool draw(const vector<string>& board) {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (board[i][j] == '.')
                return false;

    return true;
}

int main() {
    int ntests;
    std::cin >> ntests;
    vector<vector<string> > input(ntests, vector<string>(4));
    for (int test = 0; test < ntests; test++) {
        for (int i = 0; i < 4; i++)
            std::cin >> input[test][i];
    }

    vector<string> output(ntests);

    #pragma omp parallel for schedule(dynamic)
    for (int test = 0; test < ntests; test++) {
        if (won('X', input[test]))
            output[test] = "X won";
        else if (won('O', input[test]))
            output[test] = "O won";
        else if (draw(input[test]))
            output[test] = "Draw";
        else output[test] = "Game has not completed";
    }

    for (int test = 0; test < ntests; test++)
        std::cout << "Case #" << test+1 << ": " << output[test] << '\n';

    return 0;
}

