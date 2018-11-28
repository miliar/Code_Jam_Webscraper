#include <iostream>
#include <fstream>
using namespace std;

bool xTest( char x )
{
    if( x == 'X' || x == 'T' )
        return true;
    else
        return false;
}

bool oTest( char o )
{
    if( o == 'O' || o == 'T' )
        return true;
    else
        return false;
}

int main()
{
    int t;
    ifstream cin("A-large.in");
    ofstream cout("b.txt");
    cin >> t;
    char str[4][4];
    int i, j, k;
    for( k = 1; k <= t; k++ )
    {
        bool isFull = true;
        for( i = 0; i < 4; i++ )
            for( j = 0; j < 4; j++ )
            {
                cin >> str[i][j];
                if( str[i][j] == '.' )
                    isFull = false;
            }
 /*       for( i = 0; i < 4; i++ )
        {
            for( j = 0; j < 4; j++ )
                cout << str[i][j] << " ";
            cout << endl;
        }
*/
        bool xWin = false, oWin = false;
        if( xTest(str[0][0]) && xTest(str[1][1])
           && xTest(str[2][2]) && xTest(str[3][3]) )
           xWin = true;
        else if( xTest(str[0][3]) && xTest(str[1][2])
           && xTest(str[2][1]) && xTest(str[3][0]) )
           xWin = true;
        else
        {
            for( i = 0; i < 4; i++ )
            {
                if( xTest(str[i][0]) && xTest(str[i][1])
               && xTest(str[i][2]) && xTest(str[i][3]) )
               {
                   xWin = true;
                   break;
               }
               if( xTest(str[0][i]) && xTest(str[1][i])
               && xTest(str[2][i]) && xTest(str[3][i]) )
                {
                    xWin = true;
                    break;
                }
            }
        }
        if( oTest(str[0][0]) && oTest(str[1][1])
           && oTest(str[2][2]) && oTest(str[3][3]) )
           oWin = true;
        else if( oTest(str[0][3]) && oTest(str[1][2])
           && oTest(str[2][1]) && oTest(str[3][0]) )
           oWin = true;
        else
        {
            for( i = 0; i < 4; i++ )
            {
                if( oTest(str[i][0]) && oTest(str[i][1])
               && oTest(str[i][2]) && oTest(str[i][3]) )
               {
                   oWin = true;
                   break;
               }
               if( oTest(str[0][i]) && oTest(str[1][i])
               && oTest(str[2][i]) && oTest(str[3][i]) )
               {
                   oWin = true;
                   break;
               }
            }
        }
        cout << "Case #" << k << ": ";
        if( xWin && !oWin )
        {
            cout << "X won";
        }
        else if( !xWin && oWin )
        {
            cout << "O won";
        }
        else if( (xWin && oWin && isFull) || ( !xWin && !oWin && isFull) )
        {
            cout << "Draw";
        }
        else if( !xWin && !oWin && !isFull )
        {
            cout << "Game has not completed";
        }
        cout << endl;
    }
    return 0;
}
