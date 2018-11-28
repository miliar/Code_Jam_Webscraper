#include <iostream>
#include <fstream>
#include <string>
using namespace std;


/** ******************
 *  TIC TAC TOE TOMEK
 ** ******************/

/*
 * "X won" (the game is over, and X won)
 * "O won" (the game is over, and O won)
 * "Draw" (the game is over, and it ended in a draw)
 * "Game has not completed" (the game is not over yet)
 */

string solveTicTacToeTomek(ifstream& file) {
    bool completed = true;

    char board[4][4];
    // lines 0-3 are rows
    // lines 4-7 are cols
    // line 8 is downwards diagonal
    // line 9 is upwards diagonal
    string testLine[10];

    // fill the board
    for (int i=0; i!=4; i++) {
        file >> board[i];

        testLine[i] = board[i];

        char temp;
        for (int k=0; k!=4; k++) {
            temp = board[i][k];
            testLine[4+k].push_back(temp); // cols
        }

        // diagonals
        temp = board[i][i]; testLine[8].push_back(temp);
        temp = board[i][3-i]; testLine[9].push_back(temp);
    }

    // At this point there is no '.' in the board

    // Test
    for (int i=0; i!=10; i++) {
        if (testLine[i].find('.') != string::npos) {
            // '.' found noone wins this line
            completed = false;
            continue;
        }
        if (testLine[i].find('X') == string::npos) {
            // no X found so O wins
            return "O won ";
        } else if (testLine[i].find('O') == string::npos) {
            // no O found so X wins
            return "X won ";
        }
    }

    if (completed) {
        return "Draw";
    } else {
        return "Game has not completed";
    }
}


/** ******************
 *  MAIN PROGRAM
 ** ******************/

int main()
{
    string line;
    ifstream myFile;
    myFile.open("test.txt");
    if (myFile.is_open()) {
        // N Test Cases
        int T;
        myFile >> T;
        for (int caseN  = 0; caseN != T; caseN++) {
            cout << "Case #" << caseN+1 << ": ";
            cout << solveTicTacToeTomek(myFile) << endl;
        }
    } else {
        cout << "Unable to read file." << endl;
    }
    myFile.close();
    return 0;
}
