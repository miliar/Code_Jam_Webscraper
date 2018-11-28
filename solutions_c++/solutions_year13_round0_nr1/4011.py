#include <cstdio>
#include <string>

using namespace std;

string getstate(char board[5][5])
{
	int row, col;
	// Check for X win
	for (row = 0; row < 4; row++) {
		int count = 0;
		for (col = 0; col < 4; col++) {
			if (board[row][col] == 'X' || board[row][col] == 'T')
				count++;
			else
				break;
		}
		if (count == 4)
			return "X won";
	}
	for (col = 0; col < 4; col++) {
		int count = 0;
		for (row = 0; row < 4; row++) {
			if (board[row][col] == 'X' || board[row][col] == 'T')
				count++;
			else
				break;
		}
		if (count == 4)
			return "X won";
	}
	int count = 0;
	for (row = 0, col = 0; row < 4; row++, col++) {
		if (board[row][col] == 'X' || board[row][col] == 'T')
			count++;
	}
	if (count == 4)
		return "X won";
	count = 0;
	for (row = 0, col = 3; row < 4; row++, col--) {
		if (board[row][col] == 'X' || board[row][col] == 'T')
			count++;
	}
	if (count == 4)
		return "X won";

	// Check for Y win
	for (row = 0; row < 4; row++) {
		int count = 0;
		for (col = 0; col < 4; col++) {
			if (board[row][col] == 'O' || board[row][col] == 'T')
				count++;
			else
				break;
		}
		if (count == 4)
			return "O won";
	}
	for (col = 0; col < 4; col++) {
		int count = 0;
		for (row = 0; row < 4; row++) {
			if (board[row][col] == 'O' || board[row][col] == 'T')
				count++;
			else
				break;
		}
		if (count == 4)
			return "O won";
	}
	count = 0;
	for (row = 0, col = 0; row < 4; row++, col++) {
		if (board[row][col] == 'O' || board[row][col] == 'T')
			count++;
	}
	if (count == 4)
		return "O won";
	count = 0;
	for (row = 0, col = 3; row < 4; row++, col--) {
		if (board[row][col] == 'O' || board[row][col] == 'T')
			count++;
	}
	if (count == 4)
		return "O won";

	for (int row = 0; row < 4; row++)
		for (int col = 0; col < 4; col++)
			if (board[row][col] == '.')
				return "Game has not completed";
	return "Draw";
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("tttout.txt", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		char board[5][5];
		for (int i = 0; i < 4; i++)
			scanf("%s", &board[i]);

		printf("Case #%d: %s\n", t+1, getstate(board).c_str());
	}

	return 0;
}