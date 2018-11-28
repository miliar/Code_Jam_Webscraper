#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <iomanip>

using namespace std;

typedef string ret_t;

class Solver {
public:
    char checkline(string line) {
	bool X = true;
	bool O = true;
	for (int i = 0; i < 4; ++i) {
	    if (line[i] == '.')
		return '.';
	    else if (line[i] == 'X')
		O = false;
	    else if (line[i] == 'O')
		X = false;
	}
	if (X) return 'X';
	else if (O) return 'O';
	else return '.';
    }
    ret_t solve(vector<string> board) {
	for (int i = 0; i < 10; ++i) {
	    string line;
	    if (i < 4)
		line = board[i];
	    else if (i < 8) {
		for (int j = 0; j < 4; ++j) line.push_back(board[j][i-4]);
	    }
	    else if (i == 8) {
		for (int j = 0; j < 4; ++j) line.push_back(board[j][j]);
	    }
	    else {
		for (int j = 0; j < 4; ++j) line.push_back(board[j][3-j]);
	    }

	    char r = checkline(line);
	    if (r == 'X')
		return "X won";
	    else if (r == 'O')
		return "O won";
	}

	bool full = true;
	for (int i = 0; i < 4; ++i)
	    for (int j = 0; j < 4; ++j)
		if (board[i][j] == '.')
		    full = false;
	if (full)
	    return "Draw";

	return "Game has not completed";
    }
};

int main(int argc, char ** argv) {
    string s;
    int N;
    getline(cin, s);
    {
        stringstream A(s);
        A >> N;
    }
    for (int no = 1; no <= N; ++no) {
        cerr << "Case " << no << " / " << N << endl;
        Solver solver;
        // *** get input ***
        vector<string> b;
        for (int i = 0; i < 4; ++i) {
	    getline(cin, s);
            b.push_back(s);
        }
	getline(cin, s);
        ret_t ret = solver.solve(b);

        // *** give output ***
        cout << "Case #" << no << ": " << ret << endl; // one line
        //cout << "Case #" << no << ":\n" << ret; // multi-line
        //cout << "Case #" << no << ": " << fixed << setprecision(7) << ret << endl; // float
    }
    return 0;
}
