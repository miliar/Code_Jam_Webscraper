#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <array>

static const size_t BOARD_SIZE = 4;
static const char JOKER = 'T';
static const char O = 'O';
static const char X = 'X';
static const char EMPTY = '.';

typedef std::array<std::array<char, BOARD_SIZE>, BOARD_SIZE> Board;

std::vector<Board> readBoards(std::istream& in)
{
    size_t n;
    in >> n;
    std::vector<Board> b;
    b.resize(n);
    char c;
    for (size_t k = 0; k < n; ++k) {
        for (size_t i = 0; i < BOARD_SIZE; ++i) {
            for (size_t j = 0; j < BOARD_SIZE; ++j) {
                in >> c;
                b[k][i][j] = c;
            }
        }
    }
    return b;
}

bool checkRow(const Board& b, size_t row, char s)
{
    size_t counter = 0;
    for (size_t i = 0; i < BOARD_SIZE; ++i)
        if (b[row][i] == s || b[row][i] == JOKER)
            ++counter;
    return counter == BOARD_SIZE;
}

bool checkColumn(const Board& b, size_t col, char s)
{
    size_t counter = 0;
    for (size_t i = 0; i < BOARD_SIZE; ++i)
        if (b[i][col] == s || b[i][col] == JOKER)
            ++counter;
    return counter == BOARD_SIZE;
}

bool checkDiag(const Board& b, char s)
{
    size_t counter = 0;
    for (size_t i = 0; i < BOARD_SIZE; ++i)
        if (b[i][i] == s || b[i][i] == JOKER)
            ++counter;
    return counter == BOARD_SIZE;
}

bool checkCoDiag(const Board& b, char s)
{
    size_t counter = 0;
    for (size_t i = 0; i < BOARD_SIZE; ++i)
        if (b[i][BOARD_SIZE - 1 - i] == s || b[i][BOARD_SIZE - 1 - i] == JOKER)
            ++counter;
    return counter == BOARD_SIZE;
} 

bool check(const Board& b, char s)
{
    if (checkDiag(b, s))
        return true;
    if (checkCoDiag(b, s))
        return true;
    for (size_t i = 0; i < BOARD_SIZE; ++i) {
        if (checkRow(b, i, s))
            return true;
        if (checkColumn(b, i, s))
            return true;
    }
    return false;
}

bool complete(const Board& b)
{
    for (size_t i = 0; i < BOARD_SIZE; ++i)
        for (size_t j = 0; j < BOARD_SIZE; ++j)
            if (b[i][j] == EMPTY)
                return false;
    return true;
}

std::string state(const Board& b)
{
    if (check(b, X))
        return "X won";
    else if (check(b, O))
        return "O won";
    else if (complete(b))
        return "Draw";
    else
        return "Game has not completed"; 
}

void print(const Board& b, std::ostream& out)
{
    for (size_t i = 0; i < BOARD_SIZE; ++i) {
        for (size_t j = 0; j < BOARD_SIZE; ++j) {
            out << b[i][j];
        }
        out << std::endl;
    }
}

int main()
{
    auto bs = readBoards(std::cin);
    for (size_t i = 0; i < bs.size(); ++i) {
        std::cout << "Case #" << (i + 1) << ": " << state(bs[i]) << std::endl;
    }
    return 0;
}

