#include <iostream>
#include <string>

using namespace std;

int main() {

    int cases = 0;
    cin >> cases;
    
    for( int i=0; i<cases; i++)
    {
        char board[4][4];
        string line;
        for(int j=0; j<4; j++)
        {
            cin>>line;
            for(int k=0; k<4; k++)
            {
                board[j][k] = line[k];
            }
        }
        
        int won = 0;
        int can_fill = 0;
        int j =0;
        int k =0;
        int l =0;

        for(j=0; j<4; j++)
        {
            char c = board[j][0];
            char d = board[0][j];
            
            for(k=0; k<4; k++)
            {
                if(board[j][k] == '.')
                {
                    can_fill = 1;
                    break;
                }
                else if((board[j][k] == c)||(board[j][k] == 'T'))
                {
                    continue;
                }
                else
                {
                    break;
                }
            }
            for(l=0; l<4; l++)
            {
                if(board[l][j] == '.')
                {
                    can_fill = 1;
                    break;
                }
                else if((board[l][j] == d)||(board[l][j] == 'T'))
                {
                    continue;
                }
                else
                {
                    break;
                }
            }
            if((k == 4))
            {
                if( c == 'X')
                {
                    won = 1;
                }
                else if( c == 'O')
                {
                    won = 2;
                }
                break;
            }
            if((l ==4))
            {
                if( d == 'X')
                {
                    won = 1;
                }
                else if( d == 'O')
                {
                    won = 2;
                }
                break;
            }
        }
        char diag1 = board[0][0];
        for(j =0, k =0; j<4; j++, k++)
        {
            if(board[j][k] == '.')
            {
                can_fill = 1;
                break;
            }
            else if((board[j][k] == diag1)||(board[j][k] == 'T'))
            {
                continue;
            }
            else
            {
                break;
            }
        }
        if(j == 4)
        {
            if( diag1 == 'X')
            {
               won = 1;
            }
            else if( diag1 == 'O')
            {
                won = 2;
            }
        }

        char diag2 = board[0][3];
        for(j =0, k =3; j<4; j++, k--)
        {
            if(board[j][k] == '.')
            {
                can_fill = 1;
                break;
            }
            else if((board[j][k] == diag2)||(board[j][k] == 'T'))
            {
                continue;
            }
            else
            {
                break;
            }
        }
        if(j == 4)
        {
            if( diag2 == 'X')
            {
               won = 1;
            }
            else if( diag2 == 'O')
            {
                won = 2;
            }
        }


        cout<<"Case #"<<i+1<<": ";
        
        if( won == 1)
        {
            cout<<"X won"<<endl;
        }
        else if( won == 2)
        {
            cout<<"O won"<<endl;
        }
        else if( can_fill == 0)
        {
            cout<<"Draw"<<endl;
        }
        else if( can_fill == 1)
        {
            cout<<"Game has not completed"<<endl;
        }
    }
    return 0;
}