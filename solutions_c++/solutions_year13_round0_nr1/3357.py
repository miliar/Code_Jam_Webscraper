#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

void readInput(const char *fileName, vector<string> &v) {
	ifstream in_file;
    int nCases;
    vector<vector<char> > board;
    char c;


	in_file.open(fileName, ifstream::in);
	if (in_file.fail()) cout << "**Opening file error**" << endl;
	else {
		in_file >> nCases;
		board.resize(4);
		board[0].resize(4);
		board[1].resize(4);
		board[2].resize(4);
		board[3].resize(4);
		for (int i = 0; i < nCases; i++) {
		    bool possibleDraw = true;
		    for (int j = 0; j < 4; j++) {
                for (int k = 0; k < 4; k++) {
                    in_file >> c;
                    if (c == '.') possibleDraw = false;
                    board[j][k] = c;
                }
		    }
            in_file.ignore(100, '\n');

            int j = 0;
            bool finish = false;
            char winner = ' ';
            while (j < 4 and not finish) {
                //rows
                if (board[j][0] != '.' and board[j][1] != '.' and board[j][2] != '.' and board[j][3] != '.') {
                    if (board[j][0] != 'T') {
                        if ((board[j][0] == board[j][1] or board[j][1] == 'T') and (board[j][0] == board[j][2] or board[j][2] == 'T') and (board[j][0] == board[j][3] or board[j][3] == 'T')) {
                            finish = true;
                            winner = board[j][0];
                        }
                    }
                    else {
                        if ((board[j][1] == board[j][0] or board[j][0] == 'T') and (board[j][1] == board[j][2] or board[j][2] == 'T') and (board[j][1] == board[j][3] or board[j][3] == 'T')) {
                            finish = true;
                            winner = board[j][1];
                        }
                    }
                }
                //columns
                if (not finish and board[0][j] != '.' and board[1][j] != '.' and board[2][j] != '.' and board[3][j] != '.') {
                    if (board[0][j] != 'T') {
                        if ((board[0][j] == board[1][j] or board[1][j] == 'T') and (board[0][j] == board[2][j] or board[2][j] == 'T') and (board[0][j] == board[3][j] or board[3][j] == 'T')) {
                            finish = true;
                            winner = board[0][j];
                        }
                    }
                    else {
                        if ((board[1][j] == board[0][j] or board[0][j] == 'T') and (board[1][j] == board[2][j] or board[2][j] == 'T') and (board[1][j] == board[3][j] or board[3][j] == 'T')) {
                            finish = true;
                            winner = board[1][j];
                        }
                    }
                }
                j++;
            }
            //diagonals
            if (not finish and board[0][0] != '.' and board[1][1] != '.' and board[2][2] != '.' and board[3][3] != '.') {
                if (board[0][0] != 'T') {
                    if ((board[0][0] == board[1][1] or board[1][1] == 'T') and (board[0][0] == board[2][2] or board[2][2] == 'T') and (board[0][0] == board[3][3] or board[3][3] == 'T')) {
                        finish = true;
                        winner = board[0][0];
                    }
                }
                else {
                    if ((board[1][1] == board[0][0] or board[0][0] == 'T') and (board[1][1] == board[2][2] or board[2][2] == 'T') and (board[1][1] == board[3][3] or board[3][3] == 'T')) {
                        finish = true;
                        winner = board[1][1];
                    }
                }
            }
            if (not finish and board[0][3] != '.' and board[1][2] != '.' and board[2][1] != '.' and board[3][0] != '.') {
                if (board[0][3] != 'T') {
                    if ((board[0][3] == board[1][2] or board[1][2] == 'T') and (board[0][3] == board[2][1] or board[2][1] == 'T') and (board[0][3] == board[3][0] or board[3][0] == 'T')) {
                        finish = true;
                        winner = board[0][3];
                    }
                }
                else {
                    if ((board[1][2] == board[0][3] or board[0][3] == 'T') and (board[1][2] == board[2][1] or board[2][1] == 'T') and (board[1][2] == board[3][0] or board[3][0] == 'T')) {
                        finish = true;
                        winner = board[1][2];
                    }
                }
            }


            if (winner == 'X') v.push_back("X won");
            else if (winner == 'O') v.push_back("O won");
            else {
                if (possibleDraw) v.push_back("Draw");
                else v.push_back("Game has not completed");
            }

		}
		in_file.close();
	}
}

void writeOutput(const char *fileName, vector<string> &v) {
	ofstream out_file;

	out_file.open(fileName, ofstream::out);
	if (out_file.fail()) cout << "**Opening file error**" << endl;
	else {
        for (int i = 0; i < v.size(); i++) out_file << "Case #" << i+1 << ": " << v[i] << endl;
		out_file.close();
	}
}

int main()
{
    vector<string> results;

    readInput("A-large.in", results);
    writeOutput("A-large.out", results);
    return 0;
}
