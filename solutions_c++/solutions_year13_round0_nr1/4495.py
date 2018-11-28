#define BUFFER_SIZE 1000
#define BOARD_SIZE 4

#include <fstream>
#include <iostream>

bool checkRow(int row, char board[BOARD_SIZE][BOARD_SIZE], char player)
{
    for (int column = 0; column < BOARD_SIZE; ++column)
        if (board[row][column] != player && board[row][column] != 'T') return false;
    return true;
}

bool checkColumn(int column, char board[BOARD_SIZE][BOARD_SIZE], char player)
{
    for (int row = 0; row < BOARD_SIZE; ++row)
        if (board[row][column] != player && board[row][column] != 'T') return false;
    return true;
}

bool checkDiag1(char board[BOARD_SIZE][BOARD_SIZE], char player)
{
    for (int i = 0; i < BOARD_SIZE; ++i)
        if (board[i][i] != player && board[i][i] != 'T') return false;
    return true;
}

bool checkDiag2(char board[BOARD_SIZE][BOARD_SIZE], char player)
{
    for (int i = 0; i < BOARD_SIZE; ++i)
        if (board[i][BOARD_SIZE - i - 1] != player && board[i][BOARD_SIZE - i - 1] != 'T') return false;
    return true;
}

int solveProblemA(char board[BOARD_SIZE][BOARD_SIZE])
{
    for (int i = 0; i < BOARD_SIZE; ++i)
    {
        if (checkRow(i, board, 'X') || checkColumn(i, board, 'X')) return 0;
        if (checkRow(i, board, 'O') || checkColumn(i, board, 'O')) return 1;
    }

    if (checkDiag1(board, 'X') || checkDiag2(board, 'X')) return 0;
    if (checkDiag1(board, 'O') || checkDiag2(board, 'O')) return 1;

    for (int i = 0; i < BOARD_SIZE; ++i)
        for (int j = 0; j < BOARD_SIZE; ++j)
            if (board[i][j] == '.') return 4;

    return 3;
}

void problemA(std::ifstream& fin)
{
    char buffer[BUFFER_SIZE];
    std::ofstream fout("C:\\CodeJam\\problemA.out");

    fin.getline(buffer, BUFFER_SIZE);
    int t = atoi(buffer);

    char board[BOARD_SIZE][BOARD_SIZE];

    for (int i = 1; i <= t; ++i)
    {
        for (int j = 0; j < BOARD_SIZE; ++j)
        {
            fin.getline(buffer, BUFFER_SIZE);
            for (int k = 0; k < BOARD_SIZE; ++k)
                board[j][k] = buffer[k];
        }

        fout << "Case #" << i << ": ";

        switch (solveProblemA(board))
        {
            case 0 : fout << "X won";                   break;
            case 1 : fout << "O won";                   break;
            case 3 : fout << "Draw";                    break;
            default: fout << "Game has not completed";  break;
        }

        fout << std::endl;
        fin.getline(buffer, BUFFER_SIZE);
    }

    fout.close();
}

int main(int argc, char* argv[])
{
    std::ifstream fin("C:\\CodeJam\\A-small-attempt0.in");
    if (fin.is_open())
    {
        problemA(fin);
        fin.close();
    }

    return 0;
}
