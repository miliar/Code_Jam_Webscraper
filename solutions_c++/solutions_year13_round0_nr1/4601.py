#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <fstream>

using namespace std;

string eval_board(const vector< vector<char> >& board) {
	int o_h = 0, x_h = 0;
	int o_v = 0, x_v = 0;
	int o_dl = 0, x_dl = 0;
	int o_dr = 0, x_dr = 0;
	bool completed = true;
	for(int i = 0; i < 4; ++i) {
		if(board[i][i] == 'O') {
			++o_dl;
		}else if(board[i][i] == 'X') {
			++x_dl;
		}else if(board[i][i] == 'T') {
			++o_dl;
			++x_dl;
		}
		if(board[i][3-i] == 'O') {
			++o_dr;
		}else if(board[i][3-i] == 'X') {
			++x_dr;
		}else if(board[i][3-i] == 'T') {
			++o_dr;
			++x_dr;
		}
		o_h = o_v = x_h = x_v = 0;
		for(int j = 0; j < 4; ++j) {
			if(board[i][j] == 'O') {
				++o_h;
			}else if(board[i][j] == 'X') {
				++x_h;
			}else if(board[i][j] == 'T') {
				++o_h;
				++x_h;
			}else if(completed) {
				completed = false;
			}

			if(board[j][i] == 'O') {
				++o_v;
			}else if(board[j][i] == 'X') {
				++x_v;
			}else if(board[j][i] == 'T') {
				++o_v;
				++x_v;
			}
		}
		if(o_h == 4 || o_v == 4) return "O won";
		else if(x_h == 4 || x_v == 4) return "X won";
	}
	if(o_dl == 4 || o_dr == 4) return "O won";
	else if(x_dl == 4 || x_dr == 4) return "X won";

	if(!completed) return "Game has not completed";
	return "Draw";
}

int main() {
	ifstream fin ("tttt.in");
	ofstream fout ("tttt.out");
	
	int n;
	fin >> n;

	vector<vector<vector<char> > > board(n, vector<vector<char> >(4, vector<char>(4)));
	for(int i = 0; i < n; ++i) {
		for(int j = 0; j < 4; ++j) {
			string line;
			fin >> line;
			board[i][j][0] = line[0];
			board[i][j][1] = line[1];
			board[i][j][2] = line[2];
			board[i][j][3] = line[3];
		}
	}

	for(int i = 0; i < n; ++i) fout << "Case #" << (i+1) << ": " << eval_board(board[i]) << endl;

	return 0;
}