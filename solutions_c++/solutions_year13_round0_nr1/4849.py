#include <iostream>
#include <string>
#define for0(i, n) for( int i = 0; i < (n); i++)

using namespace std;


bool wins(char board[4][4], int i, int j)
{
	int ys[8] = { 1, 1, 0, -1, -1, -1, 0, 1};
	int xs[8] = { 0, 1, 1, 1, 0, -1, -1, -1};
	char winner = board[i][j];
	if (winner == '.' || winner == 'T') return false;

	bool found = false;
	for0(d, 8)
	{
		int curi = i;
		int curj = j;
		for0(s, 3)
		{
			curj += ys[d];
			curi += xs[d];

			if (curj < 0 || curi < 0 || curj >= 4 || curi >= 4) break;

			if (board[curi][curj] != winner && board[curi][curj] != 'T') break;

			if (s == 2) found = true;
		}
		if (found) break;

	}

	return found;
}

int main ()
{
	int T;
	cin >> T;
	for0(t, T)
	{
		char board[4][4] = {0};
		for0(i, 16)
			cin >> ws >> board[i%4][i/4];
		char winner = 'D';
		for0(i, 16)
		{
			if (board[i%4][i/4] == '.') winner = '.';
			if (wins(board, i%4, i/4) ) 
			{
					winner =  board[i%4][i/4];
					break;
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if (winner == 'D') cout << "Draw" << endl;
		else if (winner == '.') cout << "Game has not completed" << endl;
		else cout << winner << " won" << endl;
			
		
	}


}