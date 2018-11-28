#include <iostream>
#include <fstream>

using namespace std;

void checkGrid(int & xcount, int & ocount, bool & gameCompleted, char grid[4][4], int a, int b) {
    if (grid[a][b] == 'O') ocount++;
    else if (grid[a][b] == 'X') xcount++;
    else if (grid[a][b] == 'T') {
        ocount++;
        xcount++;
    } else if (grid[a][b] == '.') gameCompleted = false;
}


bool checkWin(int xcount, int ocount, ofstream & out) {
    if (xcount == 4) {
        out << "X won" << endl;
        return true;
    } else if (ocount == 4) {
        out << "O won" << endl;
        return true;
    }

    return false;
}

void analyzeGrid(char grid[4][4], ofstream & out, int i) {
    out << "Case #" << i << ": ";
    bool gameCompleted = true;

    //rows
    for (int a = 0; a < 4; a++) {
        int xcount = 0, ocount = 0;

        for (int b = 0; b < 4; b++) {
            checkGrid(xcount, ocount, gameCompleted, grid, a, b);
        }
        if (checkWin(xcount, ocount, out)) return;
    }

    //columns
    for (int b = 0; b < 4; b++) {
        int xcount = 0, ocount = 0;

        for (int a = 0; a < 4; a++) {
            checkGrid(xcount, ocount, gameCompleted, grid, a, b);
        }
        if (checkWin(xcount, ocount, out)) return;
    }

    //diagonals
    for (int d = 0; d < 2; d++) {
        int xcount = 0, ocount = 0;

        for (int c = 0; c < 4; c++) {

            int a = c;
            int b;
            if (d == 0)
                b = c;
            else
                b = 3 - c;

            checkGrid(xcount, ocount, gameCompleted, grid, a, b);
        }

        if (checkWin(xcount, ocount, out)) return;
    }

    if (gameCompleted) {
        out << "Draw" << endl;
    } else {
        out << "Game has not completed" << endl;
    }
}

int main() {
    ifstream f;
    f.open("input");

    ofstream out;
    out.open("output");

    int numbTests;
    f >> numbTests;

    char grid[4][4];

    for (int i = 1; i <= numbTests; i++) {
        for (int j = 0; j < 4; j++) {
            string cur;
            f >> cur;
            for (int k = 0; k < 4; k++) {
                grid[j][k] = cur[k];
            }
        }

        analyzeGrid(grid, out, i);
    }


    f.close();
    out.close();
    return 0;
}


