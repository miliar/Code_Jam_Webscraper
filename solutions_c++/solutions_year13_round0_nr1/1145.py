// Problem A. Tic-Tac-Toe-Tomek

#include <cassert>
#include <iostream>
using namespace std;

const unsigned N = 4;

static bool isXOorT(char board, char c)
{
	return board == c || board == 'T';
}

static bool winRow(char board[N][N], char c, unsigned i)
{
	return isXOorT(board[i][0], c)
		&& isXOorT(board[i][1], c)
		&& isXOorT(board[i][2], c)
		&& isXOorT(board[i][3], c);
}

static bool winColumn(char board[N][N], char c, unsigned j)
{
	return isXOorT(board[0][j], c)
		&& isXOorT(board[1][j], c)
		&& isXOorT(board[2][j], c)
		&& isXOorT(board[3][j], c);
}

static bool winDiagonal0(char board[N][N], char c)
{
	return isXOorT(board[0][0], c)
		&& isXOorT(board[1][1], c)
		&& isXOorT(board[2][2], c)
		&& isXOorT(board[3][3], c);
}

static bool winDiagonal1(char board[N][N], char c)
{
	return isXOorT(board[0][3], c)
		&& isXOorT(board[1][2], c)
		&& isXOorT(board[2][1], c)
		&& isXOorT(board[3][0], c);
}

static bool winner(char board[N][N], char c)
{
	for (unsigned i = 0; i < N; ++i) {
		if (winRow(board, c, i) || winColumn(board, c, i))
			return true;
	}
	return winDiagonal0(board, c) || winDiagonal1(board, c);
}

static bool complete(char board[N][N])
{
	for (unsigned i = 0; i < N; ++i) {
		for (unsigned j = 0; j < N; ++j)
			if (board[i][j] == '.')
				return false;
	}
	return true;
}

static const char* testcase()
{
	assert(cin);
	char board[N][N];
	for (unsigned i = 0; i < N; ++i) {
		for (unsigned j = 0; j < N; ++j)
			cin >> board[i][j];
	}
	assert(cin);

#if 0
	for (unsigned i = 0; i < N; ++i) {
		for (unsigned j = 0; j < N; ++j)
			cout << board[i][j];
		cout << '\n';
	}
	cout << '\n';
#endif

	if (winner(board, 'X'))
		return "X won";
	else if (winner(board, 'O'))
		return "O won";
	else if (complete(board))
		return "Draw";
	else
		return "Game has not completed";
}

int main()
{
	unsigned n;
	cin >> n;
	assert(cin);
	for (unsigned i = 0; i < n; ++i)
		cout << "Case #" << i+1 << ": " << testcase() << '\n';
}
