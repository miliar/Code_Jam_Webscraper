#include <cstdio>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

static char NeutralSymbol   = 'T';
static char P1Symbol        = 'X';
static char P2Symbol        = 'O';
static char EmptySymbol     = '.';

enum State
{
    P1Won,
    P2Won,
    Draw,
    NotCompleted
};

bool checkCases(const char _board[16], unsigned _start, unsigned _end, unsigned _step, char _playerSymbol)
{
    for(unsigned i = _start; i < _end; i += _step)
    {
        if(_board[i] != NeutralSymbol && _board[i] != _playerSymbol)
            return false;
    }

    return true;
}

bool checkRow(const char _board[16], unsigned _index, char _playerSymbol)
{
    const unsigned startIndex = _index * 4;
    const unsigned endIndex = startIndex + 4;

    return checkCases(_board, startIndex, endIndex, 1, _playerSymbol);
}

bool checkColumn(const char _board[16], unsigned _index, char _playerSymbol)
{
    const unsigned startIndex = _index;
    const unsigned endIndex = startIndex + 16;

    return checkCases(_board, startIndex, endIndex, 4, _playerSymbol);
}

bool checkPlayerWin(const char _board[16], char _playerSymbol)
{
    for(unsigned i = 0; i < 4; ++i)
    {
        if(checkRow(_board, i, _playerSymbol))
            return true;

        if(checkColumn(_board, i, _playerSymbol))
            return true;
    }

    if(checkCases(_board, 0, 20, 5, _playerSymbol))
        return true;

    if(checkCases(_board, 3, 15, 3, _playerSymbol))
        return true;

    return false;
}

bool checkEmptyCase(const char _board[16])
{
    for(unsigned i = 0; i < 16; ++i)
    {
        if(_board[i] == EmptySymbol)
            return true;
    }

    return false;
}

State checkBoard(const char _board[16])
{
    if(checkPlayerWin(_board, P1Symbol))
        return P1Won;

    if(checkPlayerWin(_board, P2Symbol))
        return P2Won;

    if(checkEmptyCase(_board))
        return NotCompleted;

    return Draw;
}

void parseBoard(istream &_input, string &_board)
{
    _board = "";
    string buffer;

    for(unsigned i = 0; i < 4; ++i)
    {
        getline(_input, buffer);

        _board += buffer.substr(0, 4);
    }

    getline(_input, buffer);
}

void parseInput(vector<string> &_boards, const char *_fileName)
{
    fstream input(_fileName, fstream::in);

    string buffer;
    getline(input, buffer);

    const unsigned length = atoi(buffer.c_str());

    _boards.reserve(length);
    for(unsigned i = 0; i < length; ++i)
    {
        string board;
        parseBoard(input, board);

        _boards.push_back(board);
    }

    input.close();
}

static char *ResultStrings[] =
{
    "X won",
    "O won",
    "Draw",
    "Game has not completed"
};

void displayResult(FILE *_outFile, unsigned _caseIndex, State _result)
{
    fprintf(_outFile, "Case #%d: %s\n", _caseIndex + 1, ResultStrings[_result]);
}

void computeOutput(const vector<string> &_boards)
{
    FILE *output = fopen("output", "w");

    const unsigned length = _boards.size();
    for(unsigned i = 0; i < length; ++i)
    {
        displayResult(output, i, checkBoard(_boards[i].c_str()));
    }

    fclose(output);
}

int main(int argc, char *argv[])
{
    if(argc != 2)
        return -1;

    vector<string> boards;
    parseInput(boards, argv[1]);
    computeOutput(boards);

    return 0;
}