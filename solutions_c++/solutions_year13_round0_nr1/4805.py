//  Google Code Jam - Qualification Round
//  Problem A
//  Submission by Zemblan (nainan.kovoor@gmail.com)
//


#include <vector>
#include <iostream>

using namespace std;


enum { BoardSize = 4 };


typedef char Point;

enum LineStatus
{   Indeterminate
,   TakenByX
,   TakenByO
};

enum BoardStatus
{   Incomplete
,   Drawn
,   WonByX
,   WonByO
};


BoardStatus boardStatusFromLineStatus(const LineStatus& lineStatus)
{
    switch (lineStatus) {
    case Indeterminate:
        return Incomplete;
        break;
    case TakenByX:
        return WonByX;
        break;
    case TakenByO:
        return WonByO;
        break;
    }
}


struct Line
{
    // Construction
    Line()
    :   m_vecOfPoints(BoardSize, '.')
    {
    }
    // Access
    Point& operator[](int i) { return m_vecOfPoints[i]; }
    const Point& operator[](int i) const { return m_vecOfPoints[i]; }

private:
    // Implementation
    vector<Point> m_vecOfPoints;
};


struct Board
{
    // Construction
    Board()
    :   m_vecOfRows(BoardSize)
    {};
    // Access
    Line& operator[](int i) { return m_vecOfRows[i]; }
    const Line& operator[](int i) const { return m_vecOfRows[i]; }
    // Attributes
    Line  rowLine(int row) const { return m_vecOfRows[row]; }
    Line  colLine(int col) const
    {
        Line line;
        for (int row = 0; row != BoardSize; ++row) {
            line[row] = m_vecOfRows[row][col];
        }
        return line;
    }
    Line  lftDiagLine() const
    {
        Line line;
        for (int rc = 0; rc != BoardSize; ++rc) {
            line[rc] = m_vecOfRows[rc][rc];
        }
        return line;
    }
    Line  rgtDiagLine() const
    {
        Line line;
        for (int rc = 0; rc != BoardSize; ++rc) {
            line[rc] = m_vecOfRows[rc][BoardSize - 1 - rc];
        }
        return line;
    }
    bool isCovered() const
    {
        for (int row = 0; row != BoardSize; ++row) {
            for (int col = 0; col != BoardSize; ++col) {
                if (m_vecOfRows[row][col] == '.') {
                    return false;
                }
            }
        }

        return true;
    }

private:
    // Implementation
    vector<Line> m_vecOfRows;
};


LineStatus lineStatus(const Line& line)
{
    int numX (0), numO (0), numT (0);

    for (int i = 0; i != BoardSize; ++i) {
        switch (line[i]) {
        case 'X':
            ++numX;
            break;
        case 'O':
            ++numO;
            break;
        case 'T':
            ++numT;
            break;
        default:
            break;
        }
    }

    return
        ((numX + numT) == BoardSize) ? TakenByX
    :   ((numO + numT) == BoardSize) ? TakenByO
    :   Indeterminate;
}

BoardStatus boardStatus(const Board& board)
{
    // Look for win via row
    for (int row = 0; row != BoardSize; ++row) {
        LineStatus rowStatus = lineStatus(board.rowLine(row));
        if (rowStatus != Indeterminate) {
            return boardStatusFromLineStatus(rowStatus);
        }
    }
    // Look for win via col
    for (int col = 0; col != BoardSize; ++col) {
        LineStatus colStatus = lineStatus(board.colLine(col));
        if (colStatus != Indeterminate) {
            return boardStatusFromLineStatus(colStatus);
        }
    }
    // Look for win via lft diagonal
    {
        LineStatus lftDiagStatus = lineStatus(board.lftDiagLine());
        if (lftDiagStatus != Indeterminate) {
            return boardStatusFromLineStatus(lftDiagStatus);
        }
    }
    // Look for win via rgt diagonal
    {
        LineStatus rgtDiagStatus = lineStatus(board.rgtDiagLine());
        if (rgtDiagStatus != Indeterminate) {
            return boardStatusFromLineStatus(rgtDiagStatus);
        }
    }
    // Neither player won - determine whether drawn or incomplete
    return board.isCovered() ? Drawn : Incomplete;
}


void processTestCase(int caseNum)
{
    // Initialise board from input 
    Board board;
    for (int row = 0; row != BoardSize; ++row) {
        for (int col = 0; col != BoardSize; ++col) {
            cin >> board[row][col];
        }
    }

    // Determine and output board status
    cout << "Case #" << caseNum << ": ";
    switch (boardStatus(board)) {
    case Incomplete:
        cout << "Game has not completed";
        break;
    case Drawn:
        cout << "Draw";
        break;
    case WonByX:
        cout << "X won";
        break;
    case WonByO:
        cout << "O won";
        break;
    }
    cout << endl;
}


int main()
{
    int NTestCases;
    cin >> NTestCases;

    for (int t = 0; t != NTestCases; ++t) {
        processTestCase(t + 1);
    }

    return 0;
}
