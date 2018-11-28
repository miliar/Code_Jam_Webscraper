#include <iostream>
#include <string>
#include <fstream>
using namespace std;

class TicTacToeTomek
{
public:
	enum Outcome {
		OC_XWON,
		OC_OWON,
		OC_DRAW,
		OC_INCOMPLETE,
		OC_ERROR
	};

	TicTacToeTomek(string s);
	Outcome ProcessBoard();

	static const int Rows = 4;
	static const int Cols = 4;

protected:
	enum Piece {
		PIECE_X = 0,
		PIECE_O,
		PIECE_T,
		PIECE_EMPTY
	};
	bool IsEqualPiece(const char &c1, const char &c2);
	static bool IsValidChar(char c) {
		return ((c == 'X') || (c == 'O') || (c == 'T') || (c == '.'));
	}
	Outcome ProcessGroup (char c1, char c2, char c3, char c4);


	static const char BADBOARD = '-';
	char Board[Rows][Cols];
};

TicTacToeTomek::TicTacToeTomek(string s) {
	// Ensure that only valid characters are presented
	int r = 0, c = 0;
	for (size_t i = 0; (i < s.size()) && IsValidChar(s[i]); ++i) {
		if (r >= Rows) {
			Board[0][0] = BADBOARD;
			break;		// Too many characters
		}
		Board[r][c++] = s[i];
		if (c == Cols) {
			c = 0;
			++r;	// Move to the next row
		}
	}

	if (r != Rows)
	{
		// We didn't get enough pieces
		Board[0][0] = BADBOARD;
	}
}

bool TicTacToeTomek::IsEqualPiece(const char &c1, const char &c2)
{
	return ((c1 == c2) ||
			((c1 == 'T') && (c2 != '.')) ||
			((c1 != '.') && (c2 == 'T')));
}

TicTacToeTomek::Outcome TicTacToeTomek::ProcessBoard() {
	if (Board[0][0] == BADBOARD) return OC_ERROR;

	Outcome result = OC_DRAW;
	for (int i = 0;	(result == OC_DRAW) && (i < Rows); ++i) {
		result = ProcessGroup(Board[i][0], Board[i][1], Board[i][2], Board[i][3]);
	}

	for (int i = 0; ((result == OC_DRAW) && (i < Cols)); ++i) {
		result = ProcessGroup(Board[0][i], Board[1][i], Board[2][i], Board[3][i]);
	}

	// Check the Diagonals
	if (result == OC_DRAW) {
		result = ProcessGroup(Board[0][0], Board[1][1], Board[2][2], Board[3][3]);
	}
	if (result == OC_DRAW) {
		result = ProcessGroup(Board[0][3], Board[1][2], Board[2][1], Board[3][0]);
	}

	if (result == OC_DRAW) {
		// If we haven't found an answer yet, it's either a draw or incomplete
		for (unsigned int i = 0; i < Rows; ++i) {
			for (unsigned int j = 0; j < Rows; ++j) {
				if (Board[i][j] == '.') {
					result = OC_INCOMPLETE;
					break;
				}
			}
		}
	}

	return result;
}

TicTacToeTomek::Outcome TicTacToeTomek::ProcessGroup(char c1, char c2, char c3, char c4) {
	if (IsEqualPiece(c1, c2) && IsEqualPiece(c2, c3) && IsEqualPiece(c3, c4) && IsEqualPiece(c4, c1)) {
		char Piece = (c1 == 'T') ? c2 : c1;		// Assumes there is only one 'T' in the board; valid board is given as precondition
		switch (Piece) {
		case 'X':
			return OC_XWON;
		case 'O':
			return OC_OWON;
		case '.':
			return OC_DRAW;
		default:
			cerr << "Invalid Piece on Board\n";
			break;
		}
	}
	return OC_DRAW;
}

void main() {
	ifstream in("D:\\tttt2.txt");
	ofstream out("D:\\tttt2out.txt");
	int numBoards;
	in >> numBoards;
	for (int i = 1; i <= numBoards; ++i) {
		string sBoard = "";
		for (int j = 0; j < TicTacToeTomek::Rows; ++j) {
			string sTmp;
			in >> sTmp;
			sBoard += sTmp;
		}
		TicTacToeTomek tttt(sBoard);
		out << "Case #" << i << ": ";
		switch(tttt.ProcessBoard()) {
		case TicTacToeTomek::OC_XWON:
			out << "X won";
			break;
		case TicTacToeTomek::OC_OWON:
			out << "O won";
			break;
		case TicTacToeTomek::OC_DRAW:
			out << "Draw";
			break;
		case TicTacToeTomek::OC_INCOMPLETE:
			out << "Game has not completed";
			break;
		case TicTacToeTomek::OC_ERROR:
		default:
			out << "ERROR";
			break;
		}
		out << endl;
	}
	in.close();
	out.close();
}


