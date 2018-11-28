#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

void reading();


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);

    reading();

    return 0;
}

bool isCovered(char Table[][5])
{
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            if( Table[i][j] == '.')
                return false;

    return true;

}

bool check_diagonals(char Table[][5], int& isX) // still to fix the T case
{
    int a[4][4]; a[0][0]=1; a[0][3]=1;
    int isX1 = 3; int isX2 = 3 ;

    // initialize X1, X2

    if(Table[0][0] == 'X' )
        isX1 = 1;
    if(Table[0][0] == 'O' )
        isX1 = 0;
    if(Table[0][0] == 'T' )
    {
        if(Table[1][1] == 'X' )
            isX1 = 1;
        if(Table[1][1] == 'O' )
            isX1 = 0;
    }

    if(Table[0][3] == 'X' )
        isX2 = 1;
    if(Table[0][3] == 'O' )
        isX2 = 0;
    if(Table[0][3] == 'T' )
    {
        if(Table[1][2] == 'X' )
            isX2 = 1;
        if(Table[1][2] == 'O' )
            isX2 = 0;
    }

    // build a small dynamic
    for(int i=1; i < 4; i++)
    {
        if( ( Table[i][i] == Table[i-1][i-1] ) ||( (Table[i][i]=='T') || (Table[i-1][i-1]=='T') ))
           if( i!= 1)
                if ( (Table[i-1][i-1] == 'T') && (Table[i-2][i-2] != Table[i][i]) )
                    a[i][i] = 1;
                else
                    a[i][i] = a[i-1][i-1] + 1;
            else
                a[i][i] = a[i-1][i-1] + 1;

        else
            a[i][i] = 1;

        if( (Table[i][3-i] == Table[i-1][3-i+1]) || ( (Table[i][3-i] == 'T') || Table[i-1][3-i+1] == 'T'))
           if(i != 1)
                if((Table[i-1][3-i+1] == 'T') && (Table[i-2][3-i+2] != Table[i][3-i] ))
                    a[i][3-i] = 1;
                else
                    a[i][3-i] = a[i-1][3-i+1]+1;
            else
                a[i][3-i] = a[i-1][3-i+1] + 1;
        else
            a[i][3-i] = 1;
    }

    if( (a[3][3] == 4) && (isX1!=3) )
    {
        isX=isX1;
        return true;
    }
    if( (a[3][0] == 4) && (isX2!=3) )
    {
        isX = isX2;
        return true;
    }
    isX = 3;
    return false;
}

bool check_line(int line, char Table[][5], int& isX)
{
    int a[4]; a[0] = 1;
    int isX1 = 3;

    if( Table[line][0] == 'X' )
        isX1 = 1;
    if( Table[line][0] == 'O' )
        isX1 = 0;
    if( Table[line][0] == 'T' )
    {
        if( Table[line][1] == 'X' )
            isX1 = 1;
        if( Table[line][1] == 'O' )
            isX1 = 0;
    }

    for(int i=1; i < 4; i++)
    {
        if( (Table[line][i] == Table[line][i-1]) || ( (Table[line][i-1]=='T') || Table[line][i] == 'T') )
            if( i != 1)
                if( (Table[line][i-1] == 'T') && (Table[line][i-2] != Table[line][i]) )
                    a[i] = 1;
                else
                    a[i] = a[i-1] + 1;
            else
                a[i] = a[i-1] + 1;

        else
            a[i] = 1;
    }

    if ( (a[3] == 4) && (isX1 != 3) )
    {
        isX = isX1;
        return true;
    }

    isX = 3;
    return false;

}

bool check_column(int column, char Table[][5], int& isX)
{
    int a[4]; a[0] = 1;
    int isX1 = 3;

    if( Table[0][column] == 'X' )
        isX1 = 1;
    if( Table[0][column] == 'O' )
        isX1 = 0;
    if( Table[0][column] == 'T' )
    {
        if( Table[1][column] == 'X' )
            isX1 = 1;
        if( Table[1][column] == 'O' )
            isX1 = 0;
    }

    for(int i=1; i < 4; i++)
    {
        if( (Table[i][column] == Table[i-1][column]) || ( (Table[i-1][column]=='T') || Table[i][column] == 'T') )
            if( i != 1)
                if( (Table[i-1][column] == 'T') && (Table[i-2][column] != Table[i][column]) )
                    a[i] = 1;
                else
                    a[i] = a[i-1] + 1;
            else
                a[i] = a[i-1] + 1;

        else
            a[i] = 1;
    }

    if ( (a[3] == 4) && (isX1 != 3) )
    {
        isX = isX1;
        return true;
    }

    isX = 3;
    return false;

}


void reading()
{
    int T;
    scanf("%d",&T);

    int i,j;
    char k[4];
    fgets(k,3,stdin);

    int isX; // keeps track on who won
    bool won;
    bool covered;

    char Table[5][5];

    for(i=1; i <= T; i++)
    {
        covered = false;
        bool stopper = false;
        isX = 3;

        for(j=0; j<4; j++)
            scanf("%s",&Table[j]);
        //    fgets(Table[j],5,stdin);
        fgets(k,3,stdin);

        covered = isCovered(Table);

        won = check_diagonals(Table,isX);
        if( won )
        {
                if( isX == 1)
                {
                    printf("Case #%d: X won\n",i);
                    stopper = true;
                }
                else
                {
                    printf("Case #%d: O won\n",i);
                    stopper = true;
                }
        }
        for(j=0; (j < 4) && (stopper == false); j++)
        {
            won = check_line(j, Table, isX);

            if( won )
            {
                if( isX == 1)
                {
                    printf("Case #%d: X won\n",i);
                    stopper = true;
                }
                else
                {
                    printf("Case #%d: O won\n",i);
                    stopper = true;
                }
            }
            if( !stopper )
            {
                won = check_column(j, Table, isX);

                if( won )
                 {
                    if( isX == 1)
                    {
                        printf("Case #%d: X won\n",i);
                        stopper = true;
                    }
                    else
                    {
                        printf("Case #%d: O won\n",i);
                        stopper = true;
                    }
                 }
            }

        }

        if( !stopper && (isX == 3) && covered )
            printf("Case #%d: Draw\n",i);

        else if(!stopper && (isX == 3) && !covered)
            printf("Case #%d: Game has not completed\n",i);
    }
}
