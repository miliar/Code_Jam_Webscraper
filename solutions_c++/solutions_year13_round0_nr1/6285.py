#include <iostream>
#include <string>
#include <vector>
#include <cassert>

using namespace std;

string status(vector<string>& board) 
{
	// count the number of X, O and T in each column, row and two diags
	int Xrows[4] = {0};
	int Orows[4] = {0};
	int Trows[4] = {0};
	int Xcols[4] = {0};
	int Ocols[4] = {0};
	int Tcols[4] = {0};
	int XDL = 0;
	int XDR = 0;
	int ODL = 0;
	int ODR = 0;
	int TDL = 0;
	int TDR = 0;
	bool bEmptyCell = false;
	for(int r = 0; r < 4; r++) {
		for(int c = 0; c < 4; c++) {
			if(board[r][c] == '.') {
				bEmptyCell = true;
			} else if(board[r][c] == 'X') {
				Xrows[r]++;
				Xcols[c]++;
				if(r == c) {
					XDL++;
				}
				if(r + c == 3) {
					XDR++;
				}
			} else if(board[r][c] == 'O') {
				Orows[r]++;
				Ocols[c]++;
				if(r == c) {
					ODL++;
				}
				if(r + c == 3) {
					ODR++;
				}
			} else if(board[r][c] == 'T') {
				Trows[r]++;
				Tcols[c]++;
				if(r == c) {
					TDL++;
				}
				if(r + c == 3) {
					TDR++;
				}
			}
		}
	}
	bool Xwon = (XDL == 4) || (XDR == 4) || (XDL == 3 && TDL == 1) || (XDR == 3 && TDR == 1);
	bool Owon = (ODL == 4) || (ODR == 4) || (ODL == 3 && TDL == 1) || (ODR == 3 && TDR == 1);
	for(int i = 0; i < 4 /*&& (!Xwon) && (!Owon)*/; i++) {
		Xwon = Xwon || (Xrows[i] == 4) || (Xrows[i] == 3 && Trows[i] == 1) || (Xcols[i] == 4) || (Xcols[i] == 3 && Tcols[i] == 1);
		Owon = Owon || (Orows[i] == 4) || (Orows[i] == 3 && Trows[i] == 1) || (Ocols[i] == 4) || (Ocols[i] == 3 && Tcols[i] == 1);
	}
	assert(!(Xwon && Owon));
	if(Xwon) return "X won";
	if(Owon) return "O won";
	if(bEmptyCell)
		return "Game has not completed";
	return "Draw";
}

int main(int argc, char ** argv) 
{
	int T;
	vector<string> board;

	cin >> T;

	for(int tcase = 1; tcase <= T; tcase++) {
		string s;
		board.clear();
		for(int i = 0; i < 4; i++) {
			cin >> s;
			board.push_back(s);
		}

		cout << "Case #" << tcase << ": "  << status(board) << endl;
	}
	return 0;
}