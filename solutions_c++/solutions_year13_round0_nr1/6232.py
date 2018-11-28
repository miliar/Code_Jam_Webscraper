#include <iostream>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;

static inline bool isWin(const vector<string>& board, char player)
{
    // horiz
    for(int i = 0; i < 4; ++i)
    {
        bool isAllPlayer = true;
        for(int j = 0; j < 4; ++j)
        {
            if(board[i][j] != player && board[i][j] != 'T')
            {
                isAllPlayer = false;
                break;
            }
        }
        if (isAllPlayer)
            return true;
    }

    for(int i = 0; i < 4; ++i)
    {
        bool isAllPlayer = true;
        for(int j = 0; j < 4; ++j)
        {
            if(board[j][i] != player && board[j][i] != 'T')
            {
                isAllPlayer = false;
                break;
            }
        }
        if (isAllPlayer)
            return true;
    }

    if((board[0][0] == player || board[0][0] == 'T') &&
       (board[1][1] == player || board[1][1] == 'T') &&
       (board[2][2] == player || board[2][2] == 'T') &&
       (board[3][3] == player || board[3][3] == 'T') )
        return true;

    if((board[0][3] == player || board[0][3] == 'T') &&
       (board[1][2] == player || board[1][2] == 'T') &&
       (board[2][1] == player || board[2][1] == 'T') &&
       (board[3][0] == player || board[3][0] == 'T') )
        return true;

    return false;
}

static inline bool isFull(const vector<string>& board)
{
    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            if(board[i][j] == '.')
                return false;
        }
    }
    return true;
}

int main(void)
{
    int T;
    cin >> T;
    for(int game = 1; game <= T; ++game)
    {
        printf("Case #%d: ", game);
        vector<string> brd;
        for(int row = 0; row < 4; ++row)
        {
            string onerow;
            cin >> onerow;
            brd.push_back(onerow);
        }

        if(isWin(brd, 'O'))
            printf("O won\n");
        else if(isWin(brd, 'X'))
            printf("X won\n");
        else if(isFull(brd))
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
    return 0;
}

