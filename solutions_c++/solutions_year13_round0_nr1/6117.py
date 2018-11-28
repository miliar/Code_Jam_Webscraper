#include <iostream>
#include <string>
#include <sstream>

using namespace std;

/* return value : 0 - X won
 *                1 - O won
 *                2 - Draw
 *                3 - Incomplete
 */

char board[4][4];

int result()
{
/*    for (int i = 0; i < 4; i++){
        for (int j = 0; j < 4; j++)
            cout << board[i][j];
        cout << endl;
    }*/
    bool empty = false;
    char firstchar;
    for (int i = 0; i <4; i++)
    {
        if (board[i][0] == '.')
        {
            empty = true;
        }
        else
        {
            if(board[i][0] == 'T')
                firstchar = board[i][1];
            else
                firstchar = board[i][0];
            if((board[i][1] == firstchar || board[i][1] == 'T') && (board[i][2] == firstchar || board[i][2] == 'T') && (board[i][3] == firstchar || board[i][3] == 'T'))
            {
                if(firstchar == 'X')
                    return 0;
                else 
                    if(firstchar == 'O')
                        return 1;
                    else
                        empty = true;
            }
            else
                if(board[i][1] == '.' || board[i][2] == '.'|| board[i][3] == '.')
                    empty = true;

        }
    }
    for (int i = 0; i <4; i++)
    {
        if (board[0][i] != '.')
        {
            if(board[0][i] == 'T')
                firstchar = board[1][i];
            else
                firstchar = board[0][i];
            if((board[1][i] == firstchar || board[1][i] == 'T') && (board[2][i] == firstchar || board[2][i] == 'T') && (board[3][i] == firstchar || board[3][i] == 'T'))
            {
                if(firstchar == 'X')
                    return 0;
                else 
                    if(firstchar == 'O')
                        return 1;
            }
        }
    }
    if (board[0][0] != '.')
    {
        if(board[0][0] == 'T')
            firstchar = board[1][1];
        else
            firstchar = board[0][0];
        if((board[1][1] == firstchar || board[1][1] == 'T') && (board[2][2] == firstchar || board[2][2] == 'T') && (board[3][3] == firstchar || board[3][3] == 'T'))
        {
            if(firstchar == 'X')
                return 0;
            else 
                if(firstchar == 'O')
                    return 1;
        }
    }
    if (board[0][3] != '.')
    {
        if(board[0][3] == 'T')
            firstchar = board[1][2];
        else
            firstchar = board[0][3];
        if((board[1][2] == firstchar || board[1][2] == 'T') && (board[2][1] == firstchar || board[2][1] == 'T') && (board[3][0] == firstchar || board[3][0] == 'T'))
        {
            if(firstchar == 'X')
                return 0;
            else 
                if(firstchar == 'O')
                    return 1;
        }
    }
    if (empty)
        return 3;
    else
        return 2;
}

int main()
{
    int t;
    cin >> t;
    for (int i =1; i < t+1; i++)
    {
        string s;
        for (int j = 0; j <4; j++)
        {
            cin >> s;
            board[j][0] = s[0];
            board[j][1] = s[1];
            board[j][2] = s[2];
            board[j][3] = s[3];
        }
        int res = result();
        s = "Case #";
       /* stringstream ss;
        ss << i;
        s += ss.getstring();*/
        cout << s << i;
        s = ": ";
        switch(res)
        {
        case 0: s+= "X won";
                break;
        case 1: s+= "O won";
                break;
        case 2: s+= "Draw";
                break;
        case 3: s+= "Game has not completed";\
                break;
        }
        cout << s << endl;
    }
}

