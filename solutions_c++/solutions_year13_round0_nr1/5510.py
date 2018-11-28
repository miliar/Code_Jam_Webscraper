#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <sstream>

// Usage:
// cat input.txt | ./main > output.txt
// ./main input.txt > output.txt
// ./main input.txt output.txt

void processAllCases(std::istream &is, std::ostream &os);
void processCase(const int iteration, std::istream &is, std::ostream &os);

int main(int argc, char *argv[]) {
    std::ostream* os;
    std::istream* is;
    std::ofstream fout;
    std::ifstream fin;
    switch(argc) {
        case 1:
            os = &std::cout;
            is = &std::cin;
            break;
        case 2:
            fin.open(argv[1]);
            is = &fin;
            os = &std::cout;
            break;
        case 3:
            fin.open(argv[1]);
            is = &fin;
            fout.open(argv[2]);
            os = &fout;
            break;
        default:
            std::cout
                << "Usage:" << std::endl
                << "cat input.txt | ./main > output.txt" << std::endl
                << "./main input.txt > output.txt" << std::endl
                << "./main input.txt output.txt" << std::endl;
            return 1;
    }
    processAllCases(*is, *os);
    return 0;
}

// process all cases
void processAllCases(std::istream &is, std::ostream &os)
{
    int totalCases;
    is >> totalCases;
    for(int caseNumber = 1; caseNumber <= totalCases; ++caseNumber)
    {
        processCase(caseNumber, is, os);
    }
}

std::string getResult(const std::vector<std::vector<char> > &board);

// process individual case, caseNumber = 1..totalCases
void processCase(const int caseNumber, std::istream &is, std::ostream &os)
{
    std::vector<std::vector<char> > board;
    for(int i = 0; i < 4; ++i)
    {
        std::string line;
        is >> line;
        std::vector<char> row;
        for(int j = 0; j < 4; ++j)
        {
            row.push_back(line[j]);
        }
        board.push_back(row);
    }

    os << "Case #" << caseNumber << ": " << getResult(board) << std::endl;
}

char getCurrentPlayer(char a, char b)
{
    char currentPlayer;
    if(a != 'T')
    {
        currentPlayer = a;
    }
    else
    {
        currentPlayer = b;
    }
    return currentPlayer;
}

// possbile outcomes are "X won", "O won", "Draw", "Game has not completed"
std::string getResult(const std::vector<std::vector<char> > & board)
{
    char winnerChar;
    bool winner = false;
    bool anyDots = false;
    for(int i = 0; i < 4; ++i)
    {
        bool rowWinner = true;
        char currentPlayer = getCurrentPlayer(board[i][0], board[i][1]);
        if (currentPlayer == '.')
        {
            anyDots = true;
            rowWinner = false;
            continue;
        }
        for(int j = 0; j < 4; ++j)
        {
            if (board[i][j] == '.')
            {
                anyDots = true;
                rowWinner = false;
                break;
            }
            if(currentPlayer != board[i][j] && board[i][j] != 'T')
            {
                rowWinner = false;
                break;
            }
        }

        if(rowWinner)
        {
            winnerChar = currentPlayer;
            winner = true;
            break;
        }

    }

    for(int i = 0; i < 4; ++i)
    {
        bool columnWinner = true;
        char currentPlayer = getCurrentPlayer(board[0][i], board[1][i]);
        if (currentPlayer == '.')
        {
            columnWinner = false;
            anyDots = true;
            continue;
        }
        for(int j = 0; j < 4; ++j)
        {
            if (board[j][i] == '.')
            {
                anyDots = true;
                columnWinner = false;
                break;
            }
            if(currentPlayer != board[j][i] && board[j][i] != 'T')
            {
                columnWinner = false;
                break;
            }
        }

        if(columnWinner)
        {
            winnerChar = currentPlayer;
            winner = true;
            break;
        }

    }

    bool diagonalWinner = true;
    char currentPlayer = getCurrentPlayer(board[0][0], board[1][1]);
    if (currentPlayer == '.')
    {

        diagonalWinner = false;
        anyDots = true;
    }
    for(int i = 0; i < 4; ++i)
    {
        int j = i;
        if (board[i][j] == '.')
        {

            diagonalWinner = false;
            anyDots = true;
            break;
        }
        if(currentPlayer != board[i][j] && board[i][j] != 'T')
        {
            diagonalWinner = false;
            break;
        }


    }
    if(diagonalWinner)
    {
        winnerChar = currentPlayer;
        winner = true;
    }

    diagonalWinner = true;
    currentPlayer = getCurrentPlayer(board[3][0], board[2][1]);
    if (currentPlayer == '.')
    {

        diagonalWinner = false;
        anyDots = true;
    }
    for(int i = 0; i < 4; ++i)
    {
        int j = 3 - i;
        if (board[i][j] == '.')
        {
            diagonalWinner = false;
            anyDots = true;
            break;
        }
        if(currentPlayer != board[i][j] && board[i][j] != 'T')
        {
            diagonalWinner = false;
            break;
        }

    }
    if(diagonalWinner)
    {
        winnerChar = currentPlayer;
        winner = true;
    }


    if(winner)
    {
        std::stringstream ss;
        ss << winnerChar << " won";
        return ss.str();
    }
    else
    {
        if(anyDots)
        {
            return "Game has not completed";
        }
        else
        {
            return "Draw";
        }
    }
    return "Error";
}
