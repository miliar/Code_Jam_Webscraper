#include <iostream>
#include <fstream>

#define BOARD_SIZE 4
#define BUFFER_SIZE 256

typedef enum
{
	PLAYER_X,
	PLAYER_O,
	DRAW,
	NOT_FINISHED
} Status;

void build_board_row(char* row, char* buffer, Status* status);
void check_col_and_diag(char board[][BOARD_SIZE], Status* status);
void print_output(int index, Status status);

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		std::cout << "Usage: Tic-Tac-Toe-Tomek.exe <input_file>" << std::endl;
		return -1;
	}

	char board[BOARD_SIZE][BOARD_SIZE];

	std::ifstream input(argv[1], std::ios::in);
	char buffer[BUFFER_SIZE];
	int index_limit = -1;
	input >> index_limit;
	for (int index = 1; index <= index_limit; ++index)
	{
		// Discard empty lines
		input.getline(buffer, BUFFER_SIZE);
		Status status = DRAW;

		for (int i = 0; i < BOARD_SIZE; ++i)
		{
			input.getline(buffer, BUFFER_SIZE);
			build_board_row(board[i], buffer, &status);
		}

		if (status == DRAW || status == NOT_FINISHED)
		{
			check_col_and_diag(board, &status);
		}

		print_output(index, status);
	}

	return 0;
}

void build_board_row(char* row, char* buffer, Status* status)
{
	bool row_found = true;
	char token = buffer[0] != 'T' ? buffer[0] : buffer[1];

	for (int i = 0; i < BOARD_SIZE; ++i)
	{
		row[i] = buffer[i];
		if (*status == DRAW && row[i] == '.')
		{
			*status = NOT_FINISHED;
		}
		
		if (i > 0)
		{
			row_found = row_found && (row[i] == token || row[i] == 'T');
		}
	}
	
	if (row_found)
	{
		if (row[0] == 'X' || row[1] == 'X')
			*status = PLAYER_X;
		else if (row[0] == 'O' || row[1] == 'O')
			*status = PLAYER_O;
	}
}

void check_col_and_diag(char board[][BOARD_SIZE], Status* status)
{
	int i = -1;
	int j = -1;

	// Check cols
	bool col_found = false;
	for (j = 0; j < BOARD_SIZE && !col_found; ++j)
	{
		col_found = true;
		char token = board[0][j] != 'T' ? board[0][j] : board[0][j+1];

		for (i = 1; i < BOARD_SIZE && col_found; ++i)
		{
			col_found = col_found && (board[i][j] == token || board[i][j] == 'T');
		}
	}

	if (col_found)
	{
		if (board[0][j-1] == 'X' || board[1][j-1] == 'X')
			*status = PLAYER_X;
		else if (board[0][j-1] == 'O' || board[1][j-1] == 'O')
			*status = PLAYER_O;

		return;
	}

	// Check diag one
	bool diag_found = true;
	char token = board[0][0] != 'T' ? board[0][0] : board[1][1];
	for (i = 1, j = 1; i < BOARD_SIZE && diag_found; ++i, ++j)
	{
		diag_found = diag_found && (board[i][j] == token || board[i][j] == 'T');
	}

	if (diag_found)
	{
		if (board[0][0] == 'X' || board[1][1] == 'X')
			*status = PLAYER_X;
		else if (board[0][0] == 'O' || board[1][1] == 'O')
			*status = PLAYER_O;
		return;
	}

	// Check diag two
	diag_found = true;
	token = board[BOARD_SIZE - 1][0] != 'T' ? board[BOARD_SIZE - 1][0] : board[BOARD_SIZE - 2][1];
	for (i = BOARD_SIZE - 2, j = 1; i >= 0 && diag_found; --i, ++j)
	{
		diag_found = diag_found && (board[i][j] == token || board[i][j] == 'T');
	}

	if (diag_found)
	{
		if (board[BOARD_SIZE - 1][0] == 'X' || board[BOARD_SIZE - 2][1] == 'X')
			*status = PLAYER_X;
		else if(board[BOARD_SIZE - 1][0] == 'O' || board[BOARD_SIZE - 2][1] == 'O')
			*status = PLAYER_O;
		return;
	}
}

void print_output(int index, Status status)
{
	std::cout << "Case #" << index << ": ";
	switch(status)
	{
		case PLAYER_X:
			std::cout << "X won";
			break;
		case PLAYER_O:
			std::cout << "O won";
			break;
		case DRAW:
			std::cout << "Draw";
			break;
		case NOT_FINISHED:
			std::cout << "Game has not completed";
			break;
		default:
			std::cout << "### Wrong status ###";
	}
	std::cout << std::endl;
}
