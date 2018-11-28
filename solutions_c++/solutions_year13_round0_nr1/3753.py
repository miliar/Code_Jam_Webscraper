#include <iostream>
#include <fstream>
#include <cstdlib>

const size_t kBoardSize = 4;
enum Cell {
    X,
    O,
    T,
    E
};

void
usage()
{
    std::cout << "Please specify input and output files\n";
}

bool
checkWinConditions(size_t _count, bool _foundT)
{
    bool isWin;
    isWin = ((kBoardSize == _count) || (kBoardSize - 1 == _count && true == _foundT));
    return (isWin);
}

bool
checkHorizontal(const Cell _board[kBoardSize][kBoardSize], size_t& _index)
{
    bool foundWinner = false;
    
    for (size_t i = 0; i < kBoardSize && false == foundWinner; ++i) {
        bool   foundT = false;
        size_t countX = 0;
        size_t countO = 0;
        for (size_t j = 0; j < kBoardSize; ++j) {
            Cell cell = _board[i][j];
            switch (cell) {
                case X: ++countX; break;
                case O: ++countO; break;
                case T: foundT = true; break;
            }
        }
        if (checkWinConditions(countX, foundT)) {
            _index = size_t(X);
            foundWinner = true;
        } else if (checkWinConditions(countO, foundT)) {
            _index = size_t(O);
            foundWinner = true;
        }
    }
    return (foundWinner);
}

bool
checkDiagonal(const Cell _board[kBoardSize][kBoardSize], size_t& _index)
{
    size_t countXdiag1 = 0; // for main diagonal
    size_t countXdiag2 = 0;
    size_t countOdiag1 = 0;  // for main diagonal
    size_t countOdiag2 = 0;
    bool   foundTdiag1 = false;
    bool   foundTdiag2 = false;
    bool   foundWinner = false;
    
    for (size_t i = 0; i < kBoardSize; ++i) {
        Cell cell = _board[i][i];
        switch (cell) {
            case X: ++countXdiag1; break;
            case O: ++countOdiag1; break;
            case T: foundTdiag1 = true; break;
        }
        cell = _board[i][kBoardSize - i - 1];
        switch (cell) {
            case X: ++countXdiag2; break;
            case O: ++countOdiag2; break;
            case T: foundTdiag2 = true; break;
        }
    }
    if (checkWinConditions(countXdiag1, foundTdiag1) || checkWinConditions(countXdiag2, foundTdiag2)) {
        _index = size_t(X);
        foundWinner = true;
    } else if (checkWinConditions(countOdiag1, foundTdiag1) || checkWinConditions(countOdiag2, foundTdiag2)) {
        _index = size_t(O);
        foundWinner = true;
    }
    return (foundWinner);
}

bool
checkVertical(const Cell _board[kBoardSize][kBoardSize], size_t& _index)
{
    bool   foundWinner = false;
    size_t countEmpty  = 0;
    
    for (size_t j = 0; j < kBoardSize && false == foundWinner; ++j) {
        bool   foundT = false;
        size_t countX = 0;
        size_t countO = 0;
        for (size_t i = 0; i < kBoardSize; ++i) {
            Cell cell = _board[i][j];
            switch (cell) {
                case X: ++countX; break;
                case O: ++countO; break;
                case T: foundT = true; break;
                case E: ++countEmpty; break;
            }
        }
        if (checkWinConditions(countX, foundT)) {
            _index = size_t(X);
            foundWinner = true;
        } else if (checkWinConditions(countO, foundT)) {
            _index = size_t(O);
            foundWinner = true;
        }
    }
    if (false == foundWinner && 0 == countEmpty) {
        _index = size_t(E);
        foundWinner = true;
    }
    return (foundWinner);
}

const char*
analyzeBoard(const Cell _board[kBoardSize][kBoardSize])
{
    const char *gameResult[]= {
        "X won",
        "O won",
        "Game has not completed",
        "Draw"
    };
    
    size_t index;
    if (checkHorizontal(_board, index)) {
        return (gameResult[index]);
    }
    if (checkDiagonal(_board, index)) {
        return (gameResult[index]);
    }
    // call checkVertical last, coz checkVertical count also empty cells
    if (checkVertical(_board, index)) {
        return (gameResult[index]);
    }
    // game not completed
    return (gameResult[2]);
}

int
main(int argc, char** argv)
{
    int retValue = EXIT_SUCCESS;
    if (3 > argc) {
        usage();
        retValue = EXIT_FAILURE;
    } else {
        std::ifstream in(argv[1]);
        std::ofstream out(argv[2]);
        if (in.fail()) {
            retValue = EXIT_FAILURE;
        } else {
            size_t numTests = 0;
            in >> numTests;
            for (size_t i = 0; i < numTests; ++i) {
                /// ******************************
                /// read test case[i]
                /// ******************************
                Cell board[kBoardSize][kBoardSize];
                for (size_t j = 0; j < kBoardSize; ++j) {
                    for (size_t k = 0; k < kBoardSize; ++k) {
                        char c;
                        in >> c;
                        Cell cell = E;
                        switch (c) {
                            case 'X': cell = X; break;
                            case 'O': cell = O; break;
                            case 'T': cell = T; break;
                        }
                        board[j][k] = cell;
                    }
                }
                
                /// ******************************
                /// process test case[i]
                /// ******************************
                const char* gameResult = analyzeBoard(board);
                
                /// ******************************
                /// write result
                /// ******************************
                out << "Case #" << (i+1) << ": " << gameResult << "\n";
            }
        }
        out.close();
        in.close();
    }
    return (retValue);
}