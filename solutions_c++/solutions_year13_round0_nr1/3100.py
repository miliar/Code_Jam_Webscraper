#include <algorithm>
#include <cstring>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

template <class T>
T split(string str, char delim) {
	T t;
	string token;
	stringstream ss(str);
	while (getline(ss, token, delim))
		t.push_back(stoi(token));
	return t;
}

int main(int argc, char **argv) {
	// Setup input and output files
	if (argc != 2) {
		cout << "Input file!" << endl;
		return 1;
	}
	string filename(argv[1]);
	ifstream is(filename);
	ofstream os(filename.replace(filename.end()-2, filename.end(), "out"));

	string buf;

	// Structure to hold a line of four squares
	class line {
		public:
			int x;
			int o;
			int t;
			bool ongoing;
			line() : x(0), o(0), t(0), ongoing(false){} 
			void clear() {x=0; o=0; t=0; }
			char win(ofstream &os) {
				if (x == 4 || (x == 3 && t == 1)) {
					os << "X won" << endl;
					cout << "X won" << endl;
					return 'x';
				} else if (o == 4 || (o == 3 && t == 1)) {
					os << "O won" << endl;
					cout << "O won" << endl;
					return 'o';
				}
				return (char)0;
			}
			void check(char c) {
				switch (c) {
					case 'O':
						o++;
						break;
					case 'X':
						x++;
						break;
					case 'T':
						t++;
						break;
					case '.':
						ongoing = true;
						break;
				}
			}
	};

	// Loop over test cases
	getline(is, buf);
	int numTests = stoi(buf);
	for (int n=1; n<=numTests; n++) {
		os << "Case #" << n << ": ";
		cout << "Case #" << n << ": ";

		// Populate board
		vector<vector<char> > board;
		for (int r=0; r<4; r++) {
			getline(is, buf);
			vector<char> row;
			for (int c=0; c<4; c++)
				row.push_back(buf[c]);
			board.push_back(row);
		}
		getline(is, buf);

		line four;
		char state = 'd';
		// Loop over rows
		for (int r=0; r<4; r++) {
			four.clear();
			for (int c=0; c<4; c++) {
				four.check(board[r][c]);
			}
			if (state = four.win(os))
				break;
		}
		if (state == 'x' || state == 'o') continue;
		for (int c=0; c<4; c++) {
			four.clear();
			for (int r=0; r<4; r++) {
				four.check(board[r][c]);
			}
			if (state = four.win(os))
				break;
		}
		if (state == 'x' || state == 'o') continue;
		four.clear();
		for (int r=0, c=0; r<4; r++, c++) {
			four.check(board[r][c]);
		}
		if (state = four.win(os))
		continue;
		four.clear();
		for (int r=0, c=3; r<4; r++, c--) {
			four.check(board[r][c]);
		}
		if (state = four.win(os))
		continue;
		if (four.ongoing) {
			os << "Game has not completed" << endl;
			cout << "Game has not completed" << endl;
		} else {
			os << "Draw" << endl;
			cout << "Draw" << endl;
		}

	}

	// wrap it up
	is.close();
	os.close();
	return 0;
}

// USEFULL STUFF
// for (XXX::iterator it=XXX.begin(); it!=XXX.end(); it++) {
