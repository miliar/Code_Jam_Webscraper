#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

typedef std::vector<std::string> board_t;

void printBoard( const board_t& board )
{

    for (int i = 0; i < board.size(); i++)
    {
        std::cout << board[i] << std::endl;
    }
}

bool testWin( char player, const board_t& board )
{
    std::string winSet;
    winSet += player;
    winSet += "T";

    if (
        winSet.find(board[0][0]) != std::string::npos &&
        winSet.find(board[1][1]) != std::string::npos &&
        winSet.find(board[2][2]) != std::string::npos &&
        winSet.find(board[3][3]) != std::string::npos )
    {
        //std::cout << "Found 1" << std::endl;
        return true;
    }

    if (
        winSet.find(board[0][3]) != std::string::npos &&
        winSet.find(board[1][2]) != std::string::npos &&
        winSet.find(board[2][1]) != std::string::npos &&
        winSet.find(board[3][0]) != std::string::npos )
    {
        //std::cout << "Found 2" << std::endl;
        return true;
    }

    for (int i = 0; i < board.size(); i++)
    {
        if (
        winSet.find(board[0][i]) != std::string::npos &&
        winSet.find(board[1][i]) != std::string::npos &&
        winSet.find(board[2][i]) != std::string::npos &&
        winSet.find(board[3][i]) != std::string::npos )
        {
            //std::cout << "Found 3" << std::endl;
            return true;
        }
    }

    for (int i = 0; i < board.size(); i++)
    {
        if (
        winSet.find(board[i][0]) != std::string::npos &&
        winSet.find(board[i][1]) != std::string::npos &&
        winSet.find(board[i][2]) != std::string::npos &&
        winSet.find(board[i][3]) != std::string::npos )
        {
            //std::cout << "Found 4" << std::endl;
            return true;
        }
    }

    return false;
}

bool notComplete( const board_t& board )
{
    for (int i = 0; i < board.size(); i++)
    {
        if (board[i].find('.') != std::string::npos)
        {
            return true;
        }
    }
}

int main ( void )
{
    std::ifstream file;

    file.open("tic-large.in");

    int numTestCases = 0;

    file >> numTestCases;
    //std::cout << "numTestCases " << numTestCases << std::endl;

    for(int i = 1; i <= numTestCases; i++)
    {
        board_t board;

        for (int j = 0; j < 4; j++)
        {
            std::string row;
            file >> row;
            board.push_back(row);
        }

        std::cout << "Case #" << i << ": ";
        if (testWin('X', board))
        {
            std::cout << "X won";
        }
        else if (testWin('O', board))
        {
            std::cout << "O won";
        }
        else if (notComplete(board))
        {
            std::cout << "Game has not completed";
        }
        else
        {
            std::cout << "Draw";
        }

        std::cout << std::endl;
        //printBoard(board);
    }

    return 0;
}

