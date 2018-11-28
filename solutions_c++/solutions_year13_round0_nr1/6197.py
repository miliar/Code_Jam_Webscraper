#include <iostream>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <vector>
#include <string>
#include <cassert>

using namespace std;

ifstream *input;
string getLine() {
    string line;
    if (input)
        getline(*input, line);
    else
        getline(std::cin, line);
    return line;
}

#define S 4

int main (int argc, char * argv[]) {
    int T;

    string s, line;
    if (argc > 1) {
        input = new ifstream(argv[1], std::ios_base::in);
        if (!input->good()) {
            return -1;
        }
    }

    line = getLine();
    if (line.length() == 0 || line == "\n") {
        return 0;
    }
    {
        stringstream ss(line);
        ss >> T;
        if (T == 0) {
            return 0;
        }
    }
    
    int *result = new int[T];
    for (int i = 0; i < T; i++) {

        std::vector<int> rows_num_X(S, 0);
        std::vector<int> cols_num_X(S, 0);
        std::vector<int> rows_num_O(S, 0);
        std::vector<int> cols_num_O(S, 0);

        int diag1_num_O = 0;
        int diag1_num_X = 0;
        int diag2_num_O = 0;
        int diag2_num_X = 0;

        //possible results
        std::vector<int> rows_pos_num_X(S, 0);
        std::vector<int> cols_pos_num_X(S, 0);
        std::vector<int> rows_pos_num_O(S, 0);
        std::vector<int> cols_pos_num_O(S, 0);

        int diag1_pos_num_O = 0;
        int diag1_pos_num_X = 0;
        int diag2_pos_num_O = 0;
        int diag2_pos_num_X = 0;

        for (int n = 0; n < S; n++) {
            line = getLine();
            assert(line.size() == S);
            for (int m = 0; m < S; m++) {
                if (line[m] == 'T') {
                    rows_num_X[n]++;
                    cols_num_X[m]++;
                    rows_num_O[n]++;
                    cols_num_O[m]++;
                    rows_pos_num_X[n]++;
                    cols_pos_num_X[m]++;
                    rows_pos_num_O[n]++;
                    cols_pos_num_O[m]++;
                    if (m == n) {
                        diag1_num_O++;
                        diag1_num_X++;
                        diag1_pos_num_O++;
                        diag1_pos_num_X++;
                    } else if ((S - 1 - n) == m) {
                        diag2_num_O++;
                        diag2_num_X++;
                        diag2_pos_num_O++;
                        diag2_pos_num_X++;
                    }
                } else if (line[m] == 'O') {
                    rows_num_O[n]++;
                    cols_num_O[m]++;
                    rows_pos_num_O[n]++;
                    cols_pos_num_O[m]++;
                    if (m == n) {
                        diag1_num_O++;
                        diag1_pos_num_O++;
                    } else if ((S - 1 - n) == m) {
                        diag2_num_O++;
                        diag2_pos_num_O++;
                    }
                } else if (line[m] == 'X') {
                    rows_num_X[n]++;
                    cols_num_X[m]++;
                    rows_pos_num_X[n]++;
                    cols_pos_num_X[m]++;
                    if (m == n) {
                        diag1_num_X++;
                        diag1_pos_num_X++;
                    } else if ((S - 1 - n) == m) {
                        diag2_num_X++;
                        diag2_pos_num_X++;
                    }
                } else {
                    rows_pos_num_X[n]++;
                    cols_pos_num_X[m]++;
                    rows_pos_num_O[n]++;
                    cols_pos_num_O[m]++;
                    if (m == n) {
                        diag1_pos_num_O++;
                        diag1_pos_num_X++;
                    } else if ((S - 1 - n) == m) {
                        diag2_pos_num_O++;
                        diag2_pos_num_X++;
                    }
                }
            }
        }
        line = getLine();

        bool winX = false;
        bool winO = false;
        //possible wins
        bool posWinX = false;
        bool posWinO = false;
        for (int n = 0; n < S; n++) {
            if (rows_num_X[n] == S || cols_num_X[n] == S || diag1_num_X == S || diag2_num_X == S)
                winX = true;
            if (rows_num_O[n] == S || cols_num_O[n] == S || diag1_num_O == S || diag2_num_O == S)
                winO = true;
            if (winO && winX)
                break;
            if (rows_pos_num_X[n] == S || cols_pos_num_X[n] == S || diag1_pos_num_X == S || diag2_pos_num_X == S)
                posWinX = true;
            if (rows_pos_num_O[n] == S || cols_pos_num_O[n] == S || diag1_pos_num_O == S || diag2_pos_num_O == S)
                posWinO = true;
        }

/*
result:
0 =   "X won" (the game is over, and X won)
1 =   "O won" (the game is over, and O won)
2 =   "Draw" (the game is over, and it ended in a draw)
3 =   "Game has not completed" (the game is not over yet)
*/
        if (winX && winO)
            result[i] = 2;
        else if (winX)
            result[i] = 0;
        else if (winO)
            result[i] = 1;
        else if (posWinX || posWinO) { // either X or O can win, outcome of the game does not matter
            result[i] = 3;
        } else {
            result[i] = 2; //nobody can win
        }
    }

    if (input) {
        input->close();
        delete input;
    }
    for (int i = 0; i < T; i++) {
        if (result[i] == 0)
            cout << "Case #" << i + 1 << ": X won" << endl;
        else if (result[i] == 1)
            cout << "Case #" << i + 1 << ": O won" << endl;
        else if (result[i] == 2)
            cout << "Case #" << i + 1 << ": Draw" << endl;
        else
            cout << "Case #" << i + 1 << ": Game has not completed" << endl;
    }
    delete [] result;
}
