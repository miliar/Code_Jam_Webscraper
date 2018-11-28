#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <iterator>
#include <cassert>

const unsigned BOARD_SIZE = 4;

enum class Square
{
	X,
	O,
	T,
	EMPTY
};

enum class GameResult
{
	X_WON,
	O_WON,
	DRAW,
	INCOMPLETE
};


struct Position
{
	unsigned x, y;
	Position(unsigned x, unsigned y) : x(x), y(y) {} // Prevent partial initialization
};

std::vector<Square> parseRow(const std::string &row)
{
	std::vector<Square> retval;
	std::transform(row.begin(), row.end(), back_inserter(retval),
		[] (const char c) -> Square
		{
			switch (c)
			{
			case 'X':
				return Square::X;
			case 'O':
				return Square::O;
			case 'T':
				return Square::T;
			case '.':
				return Square::EMPTY;
			default:
				assert(0 && "Invalid input");
			}
		}
	);
	return retval;
}

class Board
{
	std::vector<std::vector<Square>> m_matrix;

public:
	Board(const std::vector<std::string> &rows) :
		m_matrix()
	{
		std::transform(rows.begin(), rows.end(), back_inserter(m_matrix), parseRow);

		// Ensure
		const unsigned height = m_matrix.size();
		assert(height == BOARD_SIZE);
		for (const auto &row : m_matrix)
			assert(row.size() == height);
	}

	unsigned getHeight() const
	{
		return m_matrix.size();
	}

	unsigned getWidth() const
	{
		if (!getHeight())
			return 0;

		return m_matrix[0].size();
	}

	Square getSquare(const Position &position) const
	{
		return m_matrix[position.y][position.x];
	}
};

bool withinBoard(const Board &board, const Position &position)
{
	return position.x < board.getWidth() && position.y < board.getHeight();
}

GameResult getLineWinner(const Board &board, const Position &startPosition, std::function<Position(Position)> stepNext)
{
	Square player = Square::T;
	for (auto position = startPosition; withinBoard(board, position); position = stepNext(position))
	{
		const Square currentSquare = board.getSquare(position);
		if (currentSquare == Square::EMPTY)
			return GameResult::INCOMPLETE;

		if (currentSquare == Square::T)
			continue;

		if (player == Square::T)
		{
			player = currentSquare;
			continue;
		}

		if (player != currentSquare)
		{
			for (; withinBoard(board, position); position = stepNext(position))
			{
				if (currentSquare == Square::EMPTY)
					return GameResult::INCOMPLETE;
			}

			return GameResult::DRAW;
		}
	}

	switch (player)
	{
	case Square::X:
		return GameResult::X_WON;
	case Square::O:
		return GameResult::O_WON;
	default:
		assert(0 && "Unpossible");
	}
}

GameResult testGame(const Board &board)
{
	bool foundIncomplete = false;

	for (unsigned column = 0; column< board.getWidth(); ++column)
	{
		const auto result = getLineWinner(board, {column, 0}, [] (Position p) -> Position { return {p.x, p.y+1}; });
		switch (result)
		{
		case GameResult::INCOMPLETE:
			foundIncomplete = true;
		case GameResult::DRAW:
			break;
		default:
			return result;
		}
	}

	for (unsigned row = 0; row < board.getHeight(); ++row)
	{
		const auto result = getLineWinner(board, {0, row}, [] (Position p) -> Position { return {p.x+1, p.y}; });
		switch (result)
		{
		case GameResult::INCOMPLETE:
			foundIncomplete = true;
		case GameResult::DRAW:
			break;
		default:
			return result;
		}
	}

	const auto topLeftResult = getLineWinner(board, {0, 0}, [] (Position p) -> Position { return {p.x+1, p.y+1}; });
	switch (topLeftResult)
	{
	case GameResult::INCOMPLETE:
		foundIncomplete = true;
	case GameResult::DRAW:
		break;
	default:
		return topLeftResult;
	}

	const auto topRightResult = getLineWinner(board, {board.getWidth()-1, 0}, [] (Position p) -> Position { return {p.x-1, p.y+1}; });
	switch (topRightResult)
	{
	case GameResult::INCOMPLETE:
		foundIncomplete = true;
	case GameResult::DRAW:
		break;
	default:
		return topRightResult;
	}

	if (foundIncomplete)
		return GameResult::INCOMPLETE;

	return GameResult::DRAW;
}

void test(const unsigned id)
{
	std::vector<std::string> rawBoard(BOARD_SIZE);
	for (auto &row : rawBoard)
		std::getline(std::cin, row);
	Board board(rawBoard);

	std::cout << "Case #" << id << ": ";
	switch (testGame(board))
	{
	case GameResult::X_WON:
		std::cout << "X won" << std::endl;
		break;
	case GameResult::O_WON:
		std::cout << "O won" << std::endl;
		break;
	case GameResult::DRAW:
		std::cout << "Draw" << std::endl;
		break;
	case GameResult::INCOMPLETE:
		std::cout << "Game has not completed" << std::endl;
		break;
	}
}

int main()
{
	std::string line;
	std::getline(std::cin, line);
	std::istringstream sout(line);
	unsigned testCount;
	sout >> testCount;

	for (unsigned i = 0; i < testCount; ++i)
	{
		test(i+1);
		std::string emptyLine;
		getline(std::cin, emptyLine);
	}

	return 0;
}
