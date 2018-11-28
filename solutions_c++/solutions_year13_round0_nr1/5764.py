#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int ac, char** av) {
    int T;
    cin >> T;
    char winner = '?';
    for (int cs=1; cs<=T; ++cs) {
        vector<string> b(4);
        for (int j=0; j<4; ++j) cin >> b[j];
        // check rows
        bool empties = false;
        for (int r=0; r<4; ++r) {
            if (b[r][0]=='.') empties = true;
            for (int c=1; c<4; ++c) {
                if (b[r][c]=='.') empties = true;
                if (b[r][c-1]!='T' && b[r][c]!='T' && b[r][c-1]!=b[r][c])
                    goto not_found_row;
            }
            winner = b[r][0] == 'T' ? b[r][1] : b[r][0];
            if (winner!='.') {
                cout << "Case #" << cs << ": " << winner << " won\n";
                goto next_board;
            }
          not_found_row:
            ;
        }

        // check columns
        for (int c=0; c<4; ++c) {
            for (int r=1; r<4; ++r) {
                if (b[r-1][c]!='T' && b[r][c]!='T' && b[r-1][c]!=b[r][c])
                    goto not_found_col;
            }
            winner = b[0][c] == 'T' ? b[1][c] : b[0][c];
            if (winner!='.') {
                cout << "Case #" << cs << ": " << winner << " won\n";
                goto next_board;
            }
          not_found_col:
            ;
        }

        // check diagonals
        for (int d=1; d<4; ++d) {
            if (b[d-1][d-1]!='T' && b[d][d]!='T' && b[d-1][d-1]!=b[d][d])
                goto not_found_diag;
        }
        winner = b[0][0] == 'T' ? b[1][1] : b[0][0];
        if (winner!='.') {
            cout << "Case #" << cs << ": " << winner << " won\n";
            goto next_board;
        }
      not_found_diag:
        for (int d=1; d<4; ++d) {
            if (b[d-1][4-d]!='T' && b[d][4-1-d]!='T' && b[d-1][4-d]!=b[d][4-1-d])
                goto not_found_antidiag;
        }
        winner = b[0][3] == 'T' ? b[1][2] : b[0][3];
        if (winner!='.') {
            cout << "Case #" << cs << ": " << winner << " won\n";
            goto next_board;
        }
      not_found_antidiag:
        if (empties) {
            cout << "Case #" << cs << ": Game has not completed\n";
        } else {
            cout << "Case #" << cs << ": Draw\n";
        }
      next_board:
        ;
    }
}
