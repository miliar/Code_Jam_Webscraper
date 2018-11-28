#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <array>
#include <string>
#include <memory>

template<class T>
struct FileStream {
	T stream;
	FileStream(const std::string& filename) : stream(filename.c_str()) {
	}

	~FileStream() {
		stream.close();
	}
};



enum class Symbol {
	X = 1, O = -1, T = 5, Nothing = 0
};

enum class GameState {
	XWon, OWon, Draw, NotFinished, Unknown
};



const int field_size = 4;
typedef std::array<Symbol, field_size> FieldLine;
typedef std::array<FieldLine, field_size> Field;

const FieldLine& getRow(const Field& field, int row) {
	static FieldLine result;
	for (int i = 0; i < field_size; ++i) {
		result[i] = field[i][row];
	}
	return result;
}

const std::string& convertResult(GameState gameState) {
	static std::string result;
	switch (gameState) {
	case GameState::XWon:
		result = "X won";
		break;
	case GameState::OWon:
		result = "O won";
		break;
	case GameState::Draw:
		result = "Draw";
		break;
	case GameState::NotFinished:
		result = "Game has not completed";
		break;
	}
	return result;
}

GameState lineState(const FieldLine& current_field_line, int& nothing_count) {
	auto begin = current_field_line.begin();
	auto end = current_field_line.end();
	int X_count = std::count(begin, end, Symbol::X);
	int O_count = std::count(begin, end, Symbol::O);
	if (end != std::find(begin, end, Symbol::T)) {
		if (X_count == field_size - 1) {
			return GameState::XWon;
		}
		if (O_count == field_size - 1) {
			return GameState::OWon;
		}
	}
	if (X_count == field_size) {
		return GameState::XWon;
	}
	if (O_count == field_size) {
		return GameState::OWon;
	}
	nothing_count += std::count(begin, end, Symbol::Nothing);
	return GameState::Unknown;
}

GameState evaluateState(const Field& field) {
	int nothing_count = 0;
	GameState res = GameState::Unknown;
	for (int line = 0; line < field_size; ++line) {
		const FieldLine& current_field_line = field[line];
		res = lineState(current_field_line, nothing_count);
		if (res != GameState::Unknown) {
			return res;
		}
	}

	for (int row = 0; row < field_size; ++row) {
		const FieldLine& current_field_row = getRow(field, row);
		res = lineState(current_field_row, nothing_count);
		if (res != GameState::Unknown) {
			return res;
		}
	}

	FieldLine maindiag;
	FieldLine seconddiag;
	for (int i = 0; i < field_size; ++i) {
		maindiag[i] = field[i][i];
		seconddiag[i] = field[i][field_size - i - 1];
	}

	res = lineState(maindiag, nothing_count);
	if (res != GameState::Unknown) {
		return res;
	}

	res = lineState(seconddiag, nothing_count);
	if (res != GameState::Unknown) {
		return res;
	}

	res = nothing_count ? GameState::NotFinished : GameState::Draw;
	return res;
}

void QualificationRound2013A(const std::string& filename) {
	
	FileStream<std::ifstream> input(filename);
	FileStream<std::ofstream> output(filename + ".out");
	std::string current_line("");
	std::getline(input.stream, current_line);
	const int cases = atoi(current_line.c_str());
	Field field;
	for (int current_case = 0; current_case < cases; ++current_case) {
		for (int i = 0; i < field_size; ++i) {
			std::getline(input.stream, current_line);
			for (int j = 0; j < field_size; ++j) {
				char current_char = current_line[j];
				field[i][j] = current_char == 'X' ? Symbol::X : current_char == 'O' ? Symbol::O : current_char == 'T' ? Symbol::T : Symbol::Nothing;
			}
		}
		output.stream << "Case #" << current_case + 1 << ": " << convertResult(evaluateState(field)) << std::endl;
		std::getline(input.stream, current_line);
	}
}

void main(int argc, char* argv[]) {
	std::string filename("A-large.in");
	QualificationRound2013A(filename);
}