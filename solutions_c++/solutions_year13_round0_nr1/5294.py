#include <iostream>
#define BOARD_SIZE 4

using namespace std;

bool checkBoard(char board[BOARD_SIZE][BOARD_SIZE], char p1)
{
    int i,j;

    //horizontal
    for(i=0; i < BOARD_SIZE; ++i)
    {
        for(j=0; j < BOARD_SIZE; ++j)
        {
           if(!(board[i][j] == p1 || board[i][j] == 'T'))
               break;
        }
        if(j == BOARD_SIZE)
        {
            return true;
        }
    } 

    //vertical
    for(i=0; i < BOARD_SIZE; ++i)
    {
        for(j=0; j < BOARD_SIZE; ++j)
        {
            if(!(board[j][i] == p1 || board[j][i] == 'T'))
                break;
        }
        if(j == BOARD_SIZE)
        {
            return true;
        }
    }

    //diagonals
    for(i=0; i < BOARD_SIZE; ++i)
    {
       if(!(board[i][i] == p1 || board[i][i] == 'T' ))
           break;
    }
    if(i == BOARD_SIZE)
    {
        return true;
    }

    for(i=0, j=3; i < BOARD_SIZE; ++i, --j)
    {
       if(!(board[i][j] == p1 || board[i][j] == 'T' ))
           break;
    }
    if(i == BOARD_SIZE)
    {
        return true;
    }

    return false;
}

bool gameGoesOn(char board[BOARD_SIZE][BOARD_SIZE])
{
    for(int i=0; i < BOARD_SIZE; ++i)
        for(int j=0; j < BOARD_SIZE; ++j)
            if(board[i][j] == '.')
                return true;
    return false;
}

int main(void)
{
    int T;
    char board[BOARD_SIZE][BOARD_SIZE];

    cin >> T;

    for(int i=1; i <=T; ++i)
    {
        for(int j=0; j < BOARD_SIZE; ++j)
        {
            for(int k=0; k < BOARD_SIZE; ++k)
            {
                cin >> board[j][k];
            }
            cin.ignore(255,'\n');
        }
        if(i < T)
        {
            cin.ignore(255,'\n');
        }
        cout << "Case #" << i << ": ";
        if(checkBoard(board, 'X'))
            cout << "X won" << endl;
        else if(checkBoard(board, 'O'))
            cout << "O won" << endl;
        else if(gameGoesOn(board))
            cout << "Game has not completed" << endl;
        else
            cout << "Draw" << endl;

    }

    return 0;
}
