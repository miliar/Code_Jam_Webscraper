#include <fstream>
#include <iostream>

const int numCharsPerLine = 4;
const int numLines = 4;

bool rowWin(char player, char board[][numCharsPerLine]){
    for (int lineIdx = 0; lineIdx < numLines; lineIdx++){
        bool foundOther = false;
        for (int charIdx = 0; charIdx < numCharsPerLine; charIdx++){
            if ((board[lineIdx][charIdx] != player) && board[lineIdx][charIdx] != 'T'){
                foundOther = true;
                break;
            }
        }
        if (foundOther == false){
            return true;
        }
    }
    return false;
}

bool columnWin(char player, char board[][numCharsPerLine]){
    for (int charIdx = 0; charIdx < numCharsPerLine; charIdx++){
        bool foundOther = false;
        for (int lineIdx = 0; lineIdx < numLines; lineIdx++){
            if ((board[lineIdx][charIdx] != player) && board[lineIdx][charIdx] != 'T'){
                foundOther = true;
                break;
            }
        }
        if (foundOther == false){
            return true;
        }
    }
    return false;
}

bool diagonalWin1(char player, char board[][numCharsPerLine]){
    bool foundOther = false;
    for (int charIdx = 0; charIdx < numCharsPerLine; charIdx++){
        if ((board[charIdx][charIdx] != player) && board[charIdx][charIdx] != 'T'){
            foundOther = true;
            break;
        }
    }
    return !foundOther;
}

bool diagonalWin2(char player, char board[][numCharsPerLine]){
    bool foundOther = false;
    for (int charIdx = 0; charIdx < numCharsPerLine; charIdx++){
        int charIdx2 = numCharsPerLine - charIdx - 1;
        if ((board[charIdx2][charIdx] != player) && board[charIdx2][charIdx] != 'T'){
            foundOther = true;
            break;
        }
    }
    return !foundOther;
}

bool isFinished(char board[][numCharsPerLine]){
    for (int lineIdx = 0; lineIdx < numLines; lineIdx++){
        for (int charIdx = 0; charIdx < numCharsPerLine; charIdx++){
            if (board[lineIdx][charIdx] == '.'){
                return false;
            }
        }
    }
    return true;
}

int main(int argc, char *argv[])
{
    //Game Tic-Tac-Toe-Tomek
    std::cout << "Starting solution of problem A..." << std::endl;

    //file names for input and output
    std::string filenameIn = "A-large.in";
    std::string filenameOut = "A-large.out";
    //std::string filenameIn = "A-small-practice.in";
    //std::string filenameOut = "A-small-practice.out";
    //std::string filenameIn = "A-small-attempt0.in";
    //std::string filenameOut = "A-small-attempt0.out";

    std::ofstream os(filenameOut.c_str());

    std::ifstream is(filenameIn.c_str());
    if (is.is_open()){
        int numTestCases = 0;
        is >> numTestCases;

        for (int nCase = 1; nCase <= numTestCases; nCase++){
            std::cout << "Processing case #" << nCase << std::endl;

            char board[numLines][numCharsPerLine];
            for (int lineIdx = 0; lineIdx < numLines; lineIdx++){
                for (int charIdx = 0; charIdx < numCharsPerLine; charIdx++){
                    char input = 0;
                    is >> input; //'X', 'O', 'T' or '.'
                    board[lineIdx][charIdx] = input;
                }
            }

            //output board
            for (int i = 0; i < numLines * numCharsPerLine; i++){
                std::cout << board[i / 4][i % 4] << " ";
                if ((i%numCharsPerLine) == (numCharsPerLine-1)){
                    std::cout << std::endl;
                }
            }


            //determine state of the game
            std::string result = "Game has not completed";
            if (rowWin('X', board) || columnWin('X', board) || diagonalWin1('X', board) || diagonalWin2('X', board)){
                //"X won"
                result = "X won";
            } else if (rowWin('O', board) || columnWin('O', board) || diagonalWin1('O', board) || diagonalWin2('O', board)){
                //"O won"
                result = "O won";
            } else if (isFinished(board)){
                //"Draw"
                result = "Draw";
            }

            //write result for test case into file
            os << "Case #" << nCase << ": " << result << std::endl;
            std::cout << "Case #" << nCase << ": " << result << std::endl;
        }

    }
    is.close();

    os.close();

    return 0;
}
