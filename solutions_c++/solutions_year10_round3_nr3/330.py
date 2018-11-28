#include <iostream>
#include <string>

#define MAXLINES 1000

using std::cin;
using std::cout;
using std::endl;
using std::string;

// Number of test cases
int t = 0, num = 1;
// Dimensions of the bark
int m = 0, n = 0;

string bits (char ch)
{
	switch (ch) {
		case '0': return "0000";
		case '1': return "0001";
		case '2': return "0010";
		case '3': return "0011";
		case '4': return "0100";
		case '5': return "0101";
		case '6': return "0110";
		case '7': return "0111";
		case '8': return "1000";
		case '9': return "1001";
		case 'A': return "1010";
		case 'B': return "1011";
		case 'C': return "1100";
		case 'D': return "1101";
		case 'E': return "1110";
		case 'F': return "1111";
		default: return "0000";
	}
}

string board[MAXLINES];

int chess[1000];

void zerar()
{
	for (int i = 0; i < 1000; i++) {
		chess[i] = 0;
	}
}

bool isboard(int x, int y, int tam)
{
	for (int i = x; i < (x+tam); i++)
		for (int j = y; j < (y+tam); j++) {
			if (board[i][j] != '0' && board[i][j] != '1') return false;
			if (
				(i-1 >= x && board[i][j] == board[i-1][j]) ||
				(j-1 >= y && board[i][j] == board[i][j-1]) ||
				(i+1 < (x+tam) && board[i][j] == board[i+1][j]) ||
				(j+1 < (y+tam) && board[i][j] == board[i][j+1])
			)
				return false;
		}

	return true;
}

void markboard(int x, int y, int tam)
{
	for (int i = x; i < (x+tam); i++)
		for (int j = y; j < (y+tam); j++)
			board[i][j] = 'X';
}

int numchess (int tam)
{
	int r = 0;
	for (int i = 0; i <= (m-tam); i++)
		for (int j = 0; j <= (n-tam); j++)
			if (isboard(i, j, tam)) {
				markboard(i, j, tam);
				r++;
			}

	return r;
}

int main()
{
	cin >> t;

	while (num <= t) {
		cin >> m >> n;

		for (int i = 0; i < m; i ++) {
			string line = "";
			for (int j = 0; j < (n/4); j++) {
				char ch = ' ';
				cin >> ch;
				line += bits(ch);
			}
			board[i] = "" + line;
		}
		// After this proccess the matrix BOARD has the description of the bark
		zerar();

		// i => tamanho do tabuleiro
		int res = 0;
		for (int i = m; i > 0; i--) {
			chess[i] = numchess(i);
			if (chess[i] != 0)
				res++;
		}

/*
		for (int i = 0; i < m; i ++) {
			for (int j = 0; j < board[i].length(); j++)
				cout << board[i][j];
			cout << endl;
		}
*/

		cout << "Case #" << num << ": " << res << endl;
		for (int i = m; i > 0; i--) {
			if (chess[i] != 0)
				cout << i << " " << chess[i] << endl;
		}

		num++;
	}

	return 0;
}
