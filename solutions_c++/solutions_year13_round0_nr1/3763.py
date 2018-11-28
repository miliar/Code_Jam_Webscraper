#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstring>
#include <vector>

using namespace std;

typedef vector<string> StrVec;
typedef vector<string> Board;

void printBoard(ostream &out, Board &bd) {
    for (int i = 0; i < bd.size(); ++i) {
        out << bd[i] << endl;
    }
}

bool isFullBoard(const Board &bd) {
    int m = bd.size();
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < m; ++j) {
            if ( bd[i][j] == '.' ) {;
                return false;
            }
        }
    }
    return true;
}

inline bool isOkayChar(char a, char b) {
    if ( (a == 'T') || (a == b) ) {
        return true;
    }
    return false;
}
bool checkPlayerWon(const Board &bd, char player) {
    int m = bd.size();
    // each row
    for (int i = 0; i < m; ++i) {
        bool rowOkay = true;
        for (int j = 0; j < m; ++j) {
            if ( !isOkayChar(bd[i][j], player) ) {
                rowOkay = false;
                break;
            }
        }

        if (rowOkay) {
            return true;
        }
    }

    // each column
    for (int j = 0; j < m; ++j) {
        bool colOkay = true;
        for (int i = 0; i < m; ++i) {
            if ( !isOkayChar(bd[i][j], player) ) {
                colOkay = false;
            }
        }

        if (colOkay) {
            return true;
        }
    }

    // check main diagional
    bool mainDiagOkay = true;
    for (int i = 0; i < m; ++i) {
        if ( !isOkayChar(bd[i][i], player) ) {
            mainDiagOkay = false;
            break;
        }
    }
    if (mainDiagOkay) {
        return true;
    }

    // check reverse diagional
    bool revDiagOkay = true;
    for (int i = 0; i < m; ++i) {
        if ( !isOkayChar(bd[i][m - 1 - i], player) ) {
            revDiagOkay = false;
            break;
        }
    }

    if (revDiagOkay) {
        return true;
    }

    return false;
}

string checkStatus(const Board &bd) {
    if ( checkPlayerWon(bd, 'X') ) {
        return "X won";
    } else if ( checkPlayerWon(bd, 'O') )  {
        return "O won";
    } else { // nobody won
        return ( isFullBoard(bd) ? "Draw" : "Game has not completed" );
    };
}

int main(int argc, char *argv[]) {
    // ifstream inFile("tiny.in");
    // ifstream inFile("A-small-attempt0.in");
    // ofstream outFile("A-small-attempt0.out");
    ifstream inFile("A-large.in");
    ofstream outFile("A-large.out");
    istream &in = inFile;
    ostream &out = outFile;
    // ostream &out = cout;

    string line;
    getline(in, line);
    int T = atoi(line.c_str());

    for (int i = 0; i < T; ++i) {
        Board bd;
        for (int j = 0; j < 4; j++) {
            getline(in, line);
            bd.push_back(line);
        }
        getline(in, line);
        // printBoard(out, bd);
        out << "Case #" << i+1 << ": " << checkStatus(bd) << endl;
        //
    }
    return 0;
}
