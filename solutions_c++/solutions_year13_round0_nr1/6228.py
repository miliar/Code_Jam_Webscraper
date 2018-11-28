#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;
//int codes
//0 == No winner
//1 == X won
//2 == O won
int findGameState( char grid[][4] )
{
    for( int i =0; i<4; i++ )
    {
        if( (grid[i][0]==grid[i][1])&&(grid[i][1]==grid[i][2])&&(grid[i][2]==grid[i][3]))
        {
            if( grid[i][0] == 'X' )
                return 1;
            else if( grid[i][0] == 'O' )
                return 2;
        }
    }
    for( int j =0; j<4; j++ )
    {
        if( (grid[0][j]==grid[1][j])&&(grid[1][j]==grid[2][j])&&(grid[2][j]==grid[3][j]))
        {
            if( grid[0][j] == 'X' )
                return 1;
            else if( grid[0][j] == 'O' )
                return 2;
        }
    }
    if( (grid[0][0]==grid[1][1])&&(grid[1][1]==grid[2][2])&&(grid[2][2]==grid[3][3]))
    {
        if( grid[0][0] == 'X' )
            return 1;
        else if( grid[0][0] == 'O' )
            return 2;
    }
    if( (grid[0][3]==grid[1][2])&&(grid[1][2]==grid[2][1])&&(grid[2][1]==grid[3][0]))
    {
        if( grid[0][3] == 'X' )
            return 1;
        else if( grid[0][3] == 'O' )
            return 2;
    }

    return 0;
}

int main()
{
    int cases;
    cin >> cases;
    for(int i=0; i<cases;i++)
    {
        char xgrid[4][4];
        char ogrid[4][4];
        bool unfinished = false;
        for(int j =0; j<4; j++)
        {
            string row;
            cin >> row;
            for(int k=0; k<4;k++)
            {
                if(row[k] == '.')
                    unfinished = true;
                if(row[k] == 'T' )
                {
                    xgrid[j][k] = 'X';
                    ogrid[j][k] = 'O';
                }
                else
                {
                    xgrid[j][k] = row[k];
                    ogrid[j][k] = row[k];     
                }
            }
        }
        int result = findGameState(xgrid);
        if( result )
        {
            if( result == 1 )
                cout << "Case #" << i+1 <<": X won"<<endl;
            else
                cout << "Case #" << i+1 <<": O won"<<endl;
        }
        else
        {
            result = findGameState(ogrid);

            if( result )
            {
                if( result == 1 )
                    cout << "Case #" << i+1 <<": X won"<<endl;
                else
                    cout << "Case #" << i+1 <<": O won"<<endl;
            }
            else if (unfinished)
                cout << "Case #" << i+1 <<": Game has not completed"<<endl;
            else
                cout << "Case #" << i+1 <<": Draw"<<endl;
        }
   /*    for( int h=0; h<4; h++)
        {
            for(int j=0;j<4;j++)
            {
                cout << ogrid[h][j];
            }
            cout << endl;
        } */
    }


}














