#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

string str;
char board[16];

int main()
{
    int case_namber;
    cin >> case_namber;

    for(int current = 1; current <= case_namber; ++current)
    {
        bool X_won = false;
        bool O_won = false;
        bool has_empty = false;

        int num_X = 0;
        int num_O = 0;
        int num_T = 0;

        int k = 0;
        while(k < 16)
        {
            char buf;
            cin.get(buf);
            if(buf == 'X' || buf == 'O' || buf == 'T' || buf == '.')
            {
                board[k++] = buf;
            }
        }

        for(int i = 0; i < 4; ++i) //rows and cols
        {
            //process row
            num_X = 0; num_O = 0; num_T = 0;

            for(int j = 0; j < 4; ++j)
            {
                if(board[i*4+j] == 'X') num_X++;
                else if(board[i*4+j] == 'O') num_O++;
                else if(board[i*4+j] == 'T') num_T++;
                else if(board[i*4+j] == '.') has_empty = true;
            }

            if((num_X == 3 && num_T == 1) || num_X == 4)
            {
                X_won = true;
                break;
            }
            else if((num_O == 3 && num_T == 1) || num_O == 4)
            {
                O_won = true;
                break;
            }

            //process column
            num_X = 0; num_O = 0; num_T = 0;

            for(int j = 0; j < 4; ++j)
            {
                if(board[i+j*4] == 'X') num_X++;
                else if(board[i+j*4] == 'O') num_O++;
                else if(board[i+j*4] == 'T') num_T++;
                else if(board[i+j*4] == '.') has_empty = true;
            }

            if((num_X == 3 && num_T == 1) || num_X == 4)
            {
                X_won = true;
                break;
            }
            else if((num_O == 3 && num_T == 1) || num_O == 4)
            {
                O_won = true;
                break;
            }
        }

        if(!X_won && !O_won) //process diagonal
        {
            num_X = 0; num_O = 0; num_T = 0;

            for(int i = 0; i < 4; ++i)
            {
                if(board[i+i*4] == 'X') num_X++;
                else if(board[i+i*4] == 'O') num_O++;
                else if(board[i+i*4] == 'T') num_T++;
                //else if(board[i+i*4] == '.') has_empty = true;
            }

            if((num_X == 3 && num_T == 1) || num_X == 4)
            {
                X_won = true;
            }
            else if((num_O == 3 && num_T == 1) || num_O == 4)
            {
                O_won = true;
            }

            num_X = 0; num_O = 0; num_T = 0;

            for(int i = 1; i <= 4; ++i)
            {
                if(board[i*4-i] == 'X') num_X++;
                else if(board[i*4-i] == 'O') num_O++;
                else if(board[i*4-i] == 'T') num_T++;
                //else if(board[i+i*4] == '.') has_empty = true;
            }

            if((num_X == 3 && num_T == 1) || num_X == 4)
            {
                X_won = true;
            }
            else if((num_O == 3 && num_T == 1) || num_O == 4)
            {
                O_won = true;
            }
        }

        cout << "Case #" << current << ": ";
        if(X_won)           cout << "X won";
        else if(O_won)      cout << "O won";
        else if(has_empty)  cout << "Game has not completed";
        else                cout << "Draw";
        cout << endl;
    }
    return 0;
}
