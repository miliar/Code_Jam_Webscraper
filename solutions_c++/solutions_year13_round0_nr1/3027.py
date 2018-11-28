#include <iostream>
#include <map>
using namespace std;

void doRound(int r);

map<char, char> characters;
map<char, string> outcomes;
const char T = 3; // Draw
const char X = 2; // X won
const char O = 1; // O won
const char E = 0; // Not over yet.

int main()
{
	int numrounds;
	cin >> numrounds;

	ios_base::sync_with_stdio(false);
	
	characters['T'] = T;
	characters['X'] = X;
	characters['O'] = O;
	characters['.'] = E;
	outcomes[T] = "Draw";
	outcomes[X] = "X won";
	outcomes[O] = "O won";
	outcomes[E] = "Game has not completed";
	
	for (int i = 1; i <= numrounds; ++i)
		doRound(i);
}

char outcome(char *board)
{	
	char r;
	
#define CHECK(a, b, c, d)\
	if ((r = board[a] & board[b] & board[c] & board[d])) return r
	
	// Check to see if the rows contain any winning configs.
	CHECK(0, 1, 2, 3);
	CHECK(4, 5, 6, 7);
	CHECK(8, 9, 10, 11);
	CHECK(12, 13, 14, 15);
	
	// Check columns;
	CHECK(0, 4, 8, 12);
	CHECK(1, 5, 9, 13);
	CHECK(2, 6, 10, 14);
	CHECK(3, 7, 11, 15);
	
	// Check Diag1.
	CHECK(0, 5, 10, 15);
	
	// Check Diag2.
	CHECK(3, 6, 9, 12);
	
	// Nobody has won yet.
	for (int i = 0; i < 16; ++i)
		if (board[i] == E)
			return E;
	return T;
}

void doRound(int r)
{
	cout << "Case #" << r << ": ";
	
	char board[16];
	char *ptr = &board[0];
	
	string line;
	for (int i = 0; i < 4; ++i)
	{
		cin >> line;
		for (int k = 0; k < 4; ++k)
			*ptr++ = characters[line.at(k)];
	}
	
	cout << outcomes[outcome(board)];
	
	cout << '\n';//endl;
}