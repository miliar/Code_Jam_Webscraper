#include<iostream>
using namespace std;
int main()
{
    int t;
    int board[4][4];
    char c;
    cin>>t;
    for (int k = 1; k <= t; k++)
    {
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {
                cin>>c;
                switch(c)
                {
                    case 'X':
                        board[i][j] = 1;
                        break;
                    case 'O':
                        board[i][j] = -1;
                        break;
                    case 'T':
                        board[i][j] = 0;
                        break;
                    case '.':
                        board[i][j] = -10;
                        break;
                }
            }       
        }
        int sum;
        int gameOver = 1;
        int xwins = 0;
        int owins = 0;
        for (int i = 0; i < 4; i++)
        {
            int sum = board[i][0] + board[i][1] + board[i][2] + board[i][3];
            if (sum >= 3)
            {
                xwins = 1;
                break;
            }
            if (sum == -3 || sum == -4)
            {
                owins = 1;
                break;
            }
            if (sum <= -7)
            {
                gameOver = 0;
            }
        }
        if (xwins)
        {
            cout<<"Case #"<<k<<": X won"<<endl;
            continue;
        }
        if (owins)
        {
            cout<<"Case #"<<k<<": O won"<<endl;
            continue;
        }
        for (int i = 0; i < 4; i++)
        {
            sum = board[0][i] + board[1][i] + board[2][i] + board[3][i];
            if (sum >= 3)
            {
                xwins = 1;
                break;
            }
            if (sum == -3 || sum == -4)
            {
                owins = 1;
                break;
            }
            if (sum <= -7)
            {
                gameOver = 0;
            }
        }
        if (xwins)
        {
            cout<<"Case #"<<k<<": X won"<<endl;
            continue;
        }
        if (owins)
        {
            cout<<"Case #"<<k<<": O won"<<endl;
            continue;
        }
        sum = board[0][0] + board[1][1] + board[2][2] + board[3][3];
        if (sum >= 3)
        {
            cout<<"Case #"<<k<<": X won"<<endl;
            continue;
        }
        if (sum == -3 || sum == -4)
        {
            cout<<"Case #"<<k<<": O won"<<endl;
            continue;
        }
        sum = board[0][3] + board[1][2] + board[2][1] + board[3][0];
        if (sum >= 3)
        {
            cout<<"Case #"<<k<<": X won"<<endl;
            continue;
        }
        if (sum == -3 || sum == -4)
        {
            cout<<"Case #"<<k<<": O won"<<endl;
            continue;
        }
        if (gameOver)
        {
            cout<<"Case #"<<k<<": Draw"<<endl;
            continue;
        }
        else
        {
            cout<<"Case #"<<k<<": Game has not completed"<<endl;
        }
    }
    return 0;
}
