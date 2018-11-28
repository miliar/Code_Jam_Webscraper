#include <iostream>
#include <algorithm>

template <typename T>
struct Board {
    size_t width;
    size_t height;
    T* board;

    Board(size_t w, size_t h) :
        width(w),
        height(h),
        board(new T[w*h])
    { }

    Board(Board const& other) :
        width(other.width),
        height(other.height),
        board(new T[width*height])
    {
        std::copy_n(other.board, width*height, this->board);
    }

    ~Board() {
        delete[] board;
    }

    T* operator [] (size_t row)
    {
        return board + (row*width);
    }
    
    T const* operator [] (size_t row) const
    {
        return board + (row*width);
    }

    size_t numCells() const
    {
        return width * height;
    }

};

enum CellState {
    X = 'X',
    O = 'O',
    Empty = '.',
    WildCard = 'T'
};



template <typename T>
std::istream& operator>>(std::istream& is, Board<T>& b)
{
    for (size_t i = 0; i < b.numCells(); ++i)
    {
        char state;
        is >> state;
        b.board[i] = static_cast<enum CellState>(state);
    }

    return is;
}

template <typename T>
std::ostream& operator<<(std::ostream& os, Board<T>& b)
{
    for (size_t i = 0; i < b.height; ++i)
    {
        for (size_t j = 0; j < b.width; ++j)
        {
            os << static_cast<char>(b[i][j]);
        }
        os << std::endl;
    }

    return os;
}

struct BoardState
{
    bool xWon;
    bool oWon;
    bool hasEmptyCells;

    BoardState() :
        xWon(false),
        oWon(false),
        hasEmptyCells(false)
    { }

    std::string toString()
    {
        if (xWon && oWon)
        {
            return "Draw";
        } 
        else if (xWon)
        {
            return "X won";
        } 
        else if (oWon)
        {
            return "O won";
        } 
        else if (!hasEmptyCells)
        {
            return "Draw";
        }

        return "Game has not completed";
    }
};

bool rowOccupied(Board<CellState> const& b, CellState player, size_t row)
{
    for (size_t i = 0; i < b.width; ++i)
    {
        CellState s = b[row][i];
        if (s != WildCard && s != player)
        {
            return false;
        }
    }

    return true;
}

bool colOccupied(Board<CellState> const& b, CellState player, size_t col)
{
    for (size_t i = 0; i < b.height; ++i)
    {
        CellState s = b[i][col];
        if (s != WildCard && s != player)
        {
            return false;
        }
    }

    return true;
}

bool diagOccupied(Board<CellState> const& b, CellState player, bool increasingDiag)
{
    size_t rowInc = 1;
    size_t row = 0;

    if( !increasingDiag )
    {
        row = b.height - 1;
        rowInc = -1;
    }
    
    for (size_t col = 0; col < b.width; ++col)
    {
        CellState s = b[row][col];
        if (s != WildCard && s != player)
        {
            return false;
        }

        row += rowInc;
    }

    return true;
}

bool didPlayerWin(Board<CellState> const& b, CellState player)
{
    for (size_t row = 0; row < b.height; ++row)
    {
        if ( rowOccupied(b, player, row) )
        {
            return true;
        }
    }

    for (size_t col = 0; col < b.width; ++col)
    {
        if ( colOccupied(b, player, col) )
        {
            return true;
        }
    }

    if ( diagOccupied(b, player, false) )
    {
        return true;
    }
    
    if ( diagOccupied(b, player, true) )
    {
        return true;
    }

    return false;
}

BoardState analyze(Board<CellState> const& b)
{
    BoardState state;

    // see if there are any empty cells
    for (size_t i = 0; i < b.numCells(); ++i)
    {
        if (b.board[i] == Empty)
        {
            state.hasEmptyCells = true;
            break;
        }
    }

    // Player X
    state.xWon = didPlayerWin(b, X);
    state.oWon = didPlayerWin(b, O);

    return state;
}

int main(int argc, char const *argv[])
{
    (void) argc;
    (void) argv;

    // io efficiency
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    size_t numExamples;
    std::cin >> numExamples;

    for (size_t example = 0; example < numExamples; ++example)
    {
        Board<CellState> b(4, 4);

        std::cin >> b;

        //std::cout << b;
        std::cout << "Case #" << (example+1) << ": " << analyze(b).toString();
        std::cout << std::endl;
    }

    return 0;
}
