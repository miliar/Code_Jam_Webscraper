#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

bool isNotOver(char** board)
{
    return (board[0][0] == '.' ||
            board[0][1] == '.' ||
            board[0][2] == '.' ||
            board[0][3] == '.' ||
            board[1][0] == '.' ||
            board[1][1] == '.' ||
            board[1][2] == '.' ||
            board[1][3] == '.' ||
            board[2][0] == '.' ||
            board[2][1] == '.' ||
            board[2][2] == '.' ||
            board[2][3] == '.' ||
            board[3][0] == '.' ||
            board[3][1] == '.' ||
            board[3][2] == '.' ||
            board[3][3] == '.');
}

bool won(char** board, char player)
{
    // Check horizontal lines
    for (int i = 0; i < 4; i++)
    {
        if (
                (board[i][0] == player || board[i][0] == 'T')
           &&   (board[i][1] == player || board[i][1] == 'T')
           &&   (board[i][2] == player || board[i][2] == 'T')
           &&   (board[i][3] == player || board[i][3] == 'T')
           )
        {
            return true;
        }
    }

    // Check vertical lines
    for (int i = 0; i < 4; i++)
    {
        if (
                (board[0][i] == player || board[0][i] == 'T')
           &&   (board[1][i] == player || board[1][i] == 'T')
           &&   (board[2][i] == player || board[2][i] == 'T')
           &&   (board[3][i] == player || board[3][i] == 'T')
           )
        {
            return true;
        }
    }

    // Check axis
    if (
            (board[0][0] == player || board[0][0] == 'T')
       &&   (board[1][1] == player || board[1][1] == 'T')
       &&   (board[2][2] == player || board[2][2] == 'T')
       &&   (board[3][3] == player || board[3][3] == 'T')
       )
    {
        return true;
    }
    if (
            (board[0][3] == player || board[0][3] == 'T')
       &&   (board[1][2] == player || board[1][2] == 'T')
       &&   (board[2][1] == player || board[2][1] == 'T')
       &&   (board[3][0] == player || board[3][0] == 'T')
       )
    {
        return true;
    }

    return false;
}


int main(int argc, char** argv)
{
    // Create board
    char** board = (char**)malloc(sizeof(char*)*4);
    board[0] = (char*)malloc(sizeof(char)*4);
    board[1] = (char*)malloc(sizeof(char)*4);
    board[2] = (char*)malloc(sizeof(char)*4);
    board[3] = (char*)malloc(sizeof(char)*4);

    int tests;
    cin >> tests;
    string blank;
    getline(cin, blank);

    for (int t = 1; t <= tests; t++)
    {

        // Load board
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                //cin >> board[i][j];
                scanf("%c", &board[i][j]);
            }
            getline(cin, blank);
        }
        getline(cin, blank);

        string result;

        // Discover result
        if (won(board, 'X'))
        {
            result = "X won";
        }
        else if (won(board, 'O'))
        {
            result = "O won";
        }
        else if (isNotOver(board))
        {
            result = "Game has not completed";
        }
        else
        {
            result = "Draw";
        }

        // Return result
        cout << "Case #" << t << ": " << result << "\n";
    }
}

