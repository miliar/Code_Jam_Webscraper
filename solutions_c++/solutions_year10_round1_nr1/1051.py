#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
#include <stdio.h>

typedef std::vector< std::vector<char> > Board;

void chomp()
{
	while('\n' != getchar()) ;
}

void printBoard(const Board& board)
{
    int n = board.size();
    for(int i=0; i!= n; ++i)
    {
	for(int j=0; j != n; ++j)
	    std::cout << board[i][j];
	std::cout << std::endl;
    }
}

Board readInput(int n)
{
    Board board(n);
    for(int i=0; i!=n; ++i)
    {
	board[i].reserve(n);
	for(int j = 0; j != n; ++j)
	{
	    char c = getchar();
	    board[i].push_back(c);
	}
	chomp();
    }
    //std::cout << "Input: " <<std::endl;
    //printBoard(board);
    return board;
}

Board rotateBoard(const Board& in)
{
    int n = in.size();
    Board out(n);
    for(int i=0; i!= n; ++i)
    {
	out[i].reserve(n);
	for(int j=0; j != n; ++j)
	{
	    out[i].push_back(in[n-j-1][i]);
	}
    }
    //std::cout << "Rotated: " << std::endl;
    //printBoard(out);
    return out;
}



void gravitate(Board& board)
{
    int n = board.size();
    for(int i=0; i!=n; ++i)
    {
	int curIdx = n-1;
	for(int j=n-1; j>=0; --j)
	{
	    if(board[i][j] != '.')
	    {
		board[i][curIdx] = board[i][j];
		curIdx--;
	    }
	}
	while(curIdx>=0)
	    board[i][curIdx--] = '.';

    }
    //std::cout << "Gravitated" << std::endl;
    //printBoard(board);
}

enum Result {Neither, Red, Blue, Both};

bool checkWinner(const Board& board, char player, int k)
{
    int n = board.size();
    Board rowCounts(n, std::vector<char>(n, 0));
    Board colCounts(n, std::vector<char>(n, 0));
    Board leftDiagCounts(n, std::vector<char>(n, 0));
    Board rightDiagCounts(n, std::vector<char>(n, 0));

    for(int i=0; i!=n; ++i)
    {
	for(int j =0; j!=n; ++j)
	{
	    if(board[i][j] == player)
	    {
		if(i != 0)
		    colCounts[i][j] = colCounts[i-1][j]+1;
		else
		    colCounts[i][j] = 1;
		if(j != 0)
		    rowCounts[i][j] = rowCounts[i][j-1]+1;
		else
		    rowCounts[i][j] = 1;
		if(i!=0 && j != 0)
		    leftDiagCounts[i][j] = leftDiagCounts[i-1][j-1]+1;
		else
		    leftDiagCounts[i][j] = 1;
		if(i!=0 && j != n-1)
		    rightDiagCounts[i][j] = rightDiagCounts[i-1][j+1]+1;
		else
		    rightDiagCounts[i][j] = 1;
	    }
	    if(colCounts[i][j] ==k || rowCounts[i][j] == k || leftDiagCounts[i][j] == k || rightDiagCounts[i][j] == k)
		return true;
	}
    }

    return false;
}

Result getResult(const Board& board, int k)
{
   bool redWins = checkWinner(board, 'R', k); 
   bool blueWins = checkWinner(board, 'B', k);
   return static_cast<Result>((redWins ? 1 : 0) | (blueWins ? 2 : 0));
}

void doCase(int caseNum)
{
    int n, k;
    std::cin >> n >> k;
    chomp();
    Board board = readInput(n);
    gravitate(board);
    board = rotateBoard(board);
    std::cout << "Case #" << caseNum << ": ";
    switch(Result r = getResult(board, k))
    {
	case Neither:
	    std::cout << "Neither";
	    break;
	case Red:
	    std::cout << "Red";
	    break;
	case Blue:
	    std::cout << "Blue";
	    break;
	case Both:
	    std::cout << "Both";
	    break;
	default:
	    std::cout << "bad result " << r;
    }
    std::cout << std::endl;
}

int main()
{
    int nTestCases;
    std::cin >> nTestCases;

    for(int i = 0; i != nTestCases; ++i)
	doCase(i+1);

    return 0;
}
