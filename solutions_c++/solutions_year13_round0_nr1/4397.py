#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main() {
    int N; cin >> N;
    for (int I = 1; I <= N; I++) {
        string res = "";
        vector<string> input;
        getline(cin, res);
        for (int i = 0; i < 4; i++) {
            getline(cin, res);
            input.push_back(res);
        }
        // check the rows, columns and diagonals
        bool foundx = false;
        bool foundo = false;
        int diag1x = 0;
        int diag1o = 0;
        int diag2x = 0;
        int diag2o = 0;
        bool complete = true;
        for (int i = 0; i < 4; i++) {
            // check the rows & columns
            int rowx = 0, rowo = 0, colx = 0, colo = 0;
            for (int j = 0; j < 4; j++) {
                if (input[i][j] == '.') complete = false;
                if (input[i][j] == 'X') rowx++;
                if (input[i][j] == 'O') rowo++;
                if (input[i][j] == 'T') {
                    rowx++;
                    rowo++;
                }
                if (input[j][i] == 'X') colx++;
                if (input[j][i] == 'O') colo++;
                if (input[j][i] == 'T') {
                    colx++;
                    colo++;
                }
            }         
            if (rowx == 4 || colx == 4) foundx = true;
            if (rowo == 4 || colo == 4) foundo = true;
            if (input[i][i] == 'X') diag1x++;
            if (input[i][i] == 'O') diag1o++;
            if (input[i][i] == 'T') {
                diag1x++;
                diag1o++;
            }
            if (input[i][3-i] == 'X') diag2x++;
            if (input[i][3-i] == 'O') diag2o++;
            if (input[i][3-i] == 'T') {
                diag2x++;
                diag2o++;
            }
        }
        if (diag1x == 4 || diag2x == 4) foundx = true;
        if (diag1o == 4 || diag2o == 4) foundo = true;
        string xwon = "X won";
        string owon = "O won";
        string draw = "Draw";
        string incomplete = "Game has not completed";
        if (foundx) res = xwon;
        else if (foundo) res = owon;
        else if (complete) res = draw;
        else res = incomplete;
            
        
        cout << "Case #" << I << ": " << res << endl;
    }
    return 0;
}
