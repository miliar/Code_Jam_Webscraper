#include <iostream>
#include <vector>

using namespace std;

enum game_results { X_WON, O_WON, DRAW, INCOMPLETE };
static const char *get_result_string(enum game_results res)
{
	switch (res) {
	case X_WON:
		return "X won";
	case O_WON:
		return "O won";
	case DRAW:
		return "Draw";
	case INCOMPLETE:
		return "Game has not completed";
	}
}

struct game_board {
	std::vector<std::string> rows; 
};

static enum game_results check_vector(const std::string& string)
{
	enum game_results res = DRAW;
	bool seen_player = false;
	for (int i = 0; i < string.length(); ++i) {
		switch (string[i]) {
		case '.':
			return INCOMPLETE;
		case 'X':
			if (!seen_player) {
				res = X_WON;
				seen_player = true;
			} else if (X_WON != res) {
				return DRAW;
			}
			break;
		case 'O':
			if (!seen_player) {
				res = O_WON;
				seen_player = true;
			} else if (O_WON != res) {
				return DRAW;
			}
			break;
		case 'T':
			break;
		}
	}
	return res;
}

static void get_next_board(istream& input, struct game_board* board)
{
	char c;
	std::string line;
	board->rows.resize(0);
	const int ROWS_IN_BOARD = 4;

	for (int x = 0; x < ROWS_IN_BOARD; ++x) {
		getline(input, line);
		board->rows.push_back(line);
	}
	getline(input, line);
}

// Transforms the rows into colums and diagnol runs to check
static void transform_rows(std::vector<std::string>& rows, std::vector<std::string>* cols)
{
	char run[5] = {0,};
	cols->resize(0);
	const int len = rows.size();

	// Grab the columns first
	for (int i = 0; i < len; ++i) {
		for (int j = 0; j < len; ++j) {
			run[j] = rows[j][i];
		}
		cols->push_back(run);
	}

	// Now the two diagnols
	for (int i = 0; i < len; ++i) {
		run[i] = rows[i][i];
	}
	cols->push_back(run);
	for (int i = 0; i < len; ++i) {
		run[i] = rows[i][3-i];
	}
	cols->push_back(run);
}

static enum game_results check_board(struct game_board& board)
{
	enum game_results res = DRAW;
	std::vector<std::string>::iterator it;
	std::vector<std::string> cols;

	// First check the rows for a winner.
	for (it = board.rows.begin(); it != board.rows.end(); ++it) {
		enum game_results run_result = check_vector(*it);
		// If we have a winner, don't bother checking any other lines.
		if ((X_WON == run_result) || (O_WON == run_result)) {
			return run_result;
		} else if (INCOMPLETE == run_result) {
			res = INCOMPLETE;
		}
	}

	// No winner, so let's check the colums and diagnols.
	transform_rows(board.rows, &cols);
	for (it = cols.begin(); it != cols.end(); ++it) {
		enum game_results run_result = check_vector(*it);
		// If we have a winner, don't bother checking any other lines.
		if ((X_WON == run_result) || (O_WON == run_result)) {
			return run_result;
		} else if (INCOMPLETE == run_result) {
			res = INCOMPLETE;
		}
	}

	return res;
}

int main(int argc, char *argv[])
{
	struct game_board board;
	unsigned int board_count;
	enum game_results res;
	cin.sync_with_stdio(false);
	cin >> board_count;
	cin.ignore(255, '\n');
	if (!board_count) {
		return 0;
	}
	for (int i = 0; i < board_count; ++i) {
		get_next_board(cin, &board);
		res = check_board(board);
		cout << "Case #" << i + 1 << ": " << get_result_string(res) << endl;
	}
}
