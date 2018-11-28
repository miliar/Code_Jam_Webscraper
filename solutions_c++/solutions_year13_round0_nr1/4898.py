#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <unordered_map>
#include <vector>
#include <set>
#include <unordered_set>

// =================== SOME USEFULL DEFINES ======================================
#define fi first
#define se second
#define FOR(i, n) for(int i = 0; i < (n); ++i)
#define sqr(x) ((x)*(x))
#define pow2(x) (1 << (x))
#define hmap unordered_map
#define hset unordered_set
#define ll long long
// ===============================================================================

using namespace std;

istream& ioIN(int argc, const char **argv);
ostream& ioOUT(int argc, const char **argv);

bool checkRows(char a[4][4], char player) {
	for (int i = 0; i < 4; ++i) {
		int j;
		for (j = 0; j < 4; j++)
			if (a[i][j] != player) break;

		if (j == 4)
			return true;
	}
	return false;
}

bool checkCols(char a[4][4], char player) {
	for (int i = 0; i < 4; ++i) {
		int j;
		for (j = 0; j < 4; j++)
			if (a[j][i] != player) break;

		if (j == 4)
			return true;
	}
	return false;
}

bool checkDiagonals(char a[4][4], char p) {
	return (((a[0][0] == p) && (a[1][1] == p) && (a[2][2] == p) && (a[3][3] == p))
		|| ((a[0][3] == p) && (a[1][2] == p) && (a[2][1] == p) && (a[3][0] == p)));
}

int main(int argc, const char **argv) {
	istream &in = ioIN(argc, argv);
	ostream &out = ioOUT(argc, argv);

	int T;

	in >> T; in.ignore();

	for (int t = 1; t <= T; ++t) {
		char c[4][4];
		pair<int, int> posT(-1, -1);
		int numEmpty = 0;

		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				in >> c[i][j];
				if (c[i][j] == '.') numEmpty++;
				if (c[i][j] == 'T') posT.first = i, posT.second = j;
			}
			in.ignore();
		}
		in.ignore();

		if (posT.first >= 0) c[posT.first][posT.second] = 'X';
		if (checkRows(c, 'X') || checkCols(c, 'X') || checkDiagonals(c, 'X')) {
			out << "Case #" << t << ": X won" << endl;
			continue;
		}

		if (posT.first >= 0) c[posT.first][posT.second] = 'O';
		if (checkRows(c, 'O') || checkCols(c, 'O') || checkDiagonals(c, 'O')) {
			out << "Case #" << t << ": O won" << endl;
			continue;
		}

		if (numEmpty == 0)
			out << "Case #" << t << ": Draw" << endl;
		else
			out << "Case #" << t << ": Game has not completed" << endl;
	}
	out.flush();

	return 0;
}

// ===============================================================================

istream& ioIN(int argc, const char **argv) {
	if (argc > 1)
		return *(new ifstream(argv[1]));
	return cin;
}

ostream& ioOUT(int argc, const char **argv) {
	if (argc > 2)
		return *(new ofstream(argv[2]));
	return cout;
}
