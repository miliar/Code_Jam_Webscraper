#include <iostream>
#include <cstdlib>

const unsigned short N = 4;
const unsigned short M = 4;
const char EMPTY = '.';
const char BOTH = 'T';
const char X = 'X';
const char O = 'O';

char board[N][M];

/**
 * Returns empty if no player has won with this column
 * otherwise returns the player character
 */
char checkColumn(const short& column) {
	char firstPlayerMove(' ');

	for (short i(0); i < N; i++) {
		switch (board[i][column]) {
		case EMPTY:
			return EMPTY;

		case BOTH:
			break;

		case X:
			if (firstPlayerMove == O)
				return EMPTY;
			else
				firstPlayerMove = X;

			break;

		case O:
			if (firstPlayerMove == X)
				return EMPTY;
			else
				firstPlayerMove = O;

			break;

		default:
			std::cout << "Found an invalid character" << std::endl;
		}
	}

	return firstPlayerMove;
}

/**
 * Returns empty if no player has won with this line
 * otherwise returns the player character
 */
char checkLine(const short& line) {
	char firstPlayerMove(' ');

	for (short i(0); i < M; i++) {
		switch (board[line][i]) {
		case EMPTY:
			return EMPTY;

		case BOTH:
			break;

		case X:
			if (firstPlayerMove == O)
				return EMPTY;
			else
				firstPlayerMove = X;

			break;

		case O:
			if (firstPlayerMove == X)
				return EMPTY;
			else
				firstPlayerMove = O;

			break;

		default:
			std::cout << "Found an invalid character" << std::endl;
		}
	}

	return firstPlayerMove;
}

/**
 * @param left_to_right indicates wether the function checks the left-to-right diagonal
 * or right-to-left diagonal
 * Returns empty if no player has own with the diagonals
 * otherwise returns the player character
 */
 char checkDiagonal(const bool& left_to_right) {
 	char firstPlayerMove(' ');
 	char pos;

	for (short i(0); i < M; i++) {
		pos = left_to_right ? board[i][i] : board[i][M - i - 1];
		switch (pos) {
		case EMPTY:
			return EMPTY;

		case BOTH:
			break;

		case X:
			if (firstPlayerMove == O)
				return EMPTY;
			else
				firstPlayerMove = X;

			break;

		case O:
			if (firstPlayerMove == X)
				return EMPTY;
			else
				firstPlayerMove = O;

			break;

		default:
			std::cout << "Found an invalid character" << std::endl;
		}
	}

	return firstPlayerMove;
}

void printBoard() {
	for (int i(0); i < N; i++) {
		for (int j(0); j < M; j++)
			std::cout << board[i][j];
		std::cout << std::endl;
	}
}

int main() {
	short num_test;
	std::cin >> num_test;

	for (short test(0); test < num_test; test++) {
		bool not_over(false);

		for (short i(0); i < N; i++) {
			for (short j(0); j < M; j++) {
				std::cin >> board[i][j];

				if (board[i][j] == EMPTY)
					not_over = true;
			}
		}

		// Debug
		// printBoard();

		// Contains wether player* has won the game
		bool playerX(false);
		bool playerO(false);

		for (short i(0); i < N; i++)
			switch (checkLine(i)) {
			case EMPTY:
				break;

			case X:
				playerX = true;
				break;

			case O:
				playerO = true;
				break;

			default:
				std::cout << "Found an invalid character" << std::endl;
			}


		for (short j(0); j < M; j++)
			switch (checkColumn(j)) {
			case EMPTY:
				break;

			case X:
				playerX = true;
				break;

			case O:
				playerO = true;
				break;

			default:
				std::cout << "Found an invalid character" << std::endl;
			}

		bool left_to_right(false);

		do {
			switch (checkDiagonal(left_to_right)) {
			case EMPTY:
				break;

			case X:
				playerX = true;
				break;

			case O:
				playerO = true;
				break;

			default:
				std::cout << "Found an invalid character" << std::endl;
			}

			left_to_right = !left_to_right;
		} while (left_to_right != false);

		std::cout << "Case #" << (test + 1) << ": ";

		if ((playerX && playerO) || (!playerX && !playerO && !not_over))
			std::cout << "Draw" << std::endl;
		else if (playerX)
			std::cout << "X won" << std::endl;
		else if (playerO)
			std::cout << "O won" << std::endl;
		else
			std::cout << "Game has not completed" << std::endl;
	}
}
