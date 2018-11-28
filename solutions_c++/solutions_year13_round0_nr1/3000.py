#include <iostream>

enum GameState {
	xwin, owin, draw, incomplete
};

GameState computeState(const char *board) {
	auto rowCheck = [&board](char ch) {
		for (int i = 0; i < 4; i++) {
			bool won = true;
			for (int j = 0; j < 4; j++) {
				char cur = board[i*4 + j];
				won = won && (cur == ch || cur == 'T');
			}
			if (won) return true;
		}

		return false;
	};

	auto colCheck = [&board](char ch) {
		for (int j = 0; j < 4; j++) {
			bool won = true;
			for (int i = 0; i < 4; i++) {
				char cur = board[i*4 + j];
				won = won && (cur == ch || cur == 'T');
			}
			if (won) return true;
		}

		return false;
	};

	auto diagCheck = [&board](char ch) {
		bool won = true;
		for (int i = 0; i < 4; i++) {
			char cur = board[i*4 + i];
			won = won && (cur == ch || cur == 'T');
		}

		if (won) return true;

		won = true;
		for (int i = 0; i < 4; i++) {
			char cur = board[i * 4 + (3 - i)];
			won = won && (cur == ch || cur == 'T');
		}

		return won;
	};

	auto isIncomplete = [&board] () {
		for (int i = 0; i < 16; i++) {
			if (board[i] == '.') {
				return true;
			}
		}
		return false;
	};

	if (rowCheck('X') || colCheck('X') || diagCheck('X')) {
		return xwin;
	} else if (rowCheck('O') || colCheck('O') || diagCheck('O')) {
		return owin;
	} else if (isIncomplete()) {
		return incomplete;
	} else {
		return draw;
	}
	
}

std::string getMessage(const GameState &state) {
	switch (state) {
		case xwin: return "X won";
		case owin: return "O won";
		case draw: return "Draw";
		case incomplete: return "Game has not completed";
	}
}


int main(void) {
	std::string line;
	std::getline(std::cin, line);

	int ncases = std::stoi(line);
	char *board = new char[16];
	for (int i = 0; i < ncases; i++) {

		char ch;
		int k = 0;
		for (size_t l = 0; l < 4; l++) {
			std::getline(std::cin, line);
			for(char ch : line) board[k++] = ch;
		}

		GameState state = computeState(board);
		std::cout << "Case #" << (i+1) << ": " << getMessage(state) << std::endl;

		std::getline(std::cin, line);
	}

	delete board;
	return 0;
}

