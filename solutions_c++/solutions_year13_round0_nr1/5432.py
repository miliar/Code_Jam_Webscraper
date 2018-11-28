#include <cstdio>
#include <iostream>

using namespace std;

const char in[]  = "A-small-attempt2.in.txt";
const char out[] = "A.out.txt";

char status[4][4+1];

bool isWon( char player )
{
    for ( int i=0; i<4; ++i )
    {
        int same = 0;
        for ( int j=0; j<4; ++j )
        {
            if ( status[i][j] == 'T' )
                ++same;
            else if ( j == 0 )
            {
                if ( status[i][j] == player ) ++same;
            }
            else if ( status[i][j] == player && ( status[i][j-1] == player || status[i][j-1] == 'T' ))
                ++same;
        }
        if ( same == 4 )
            return true;
    }
    
    for ( int j=0; j<4; ++j )
    {
        int same = 0;
        for ( int i=0; i<4; ++i )
        {
            if ( status[i][j] == 'T' )
                ++same;
            else if ( i == 0 )
            {
                if ( status[i][j] == player ) ++same;
            }
            else if ( status[i][j] == player && ( status[i-1][j] == player || status[i-1][j] == 'T' ))
                ++same;
        }
        if ( same == 4 )
            return true;
    }
    
    {
    int same = 0;
    for ( int i=0,j=0; i<4; ++i,++j )
    {
        if ( status[i][j] == 'T' )
            ++same;
        else if ( i == 0 )
        {
            if ( status[i][j] == player ) ++same;
        }
        else if ( status[i][j] == player && ( status[i-1][j-1] == player || status[i-1][j-1] == 'T' ))
            ++same;
        if ( same == 4 )
            return true;
    }
    }
    
    {
    int same = 0;
    for ( int i=0,j=3; i<4; ++i,--j )
    {
        if ( status[i][j] == 'T' )
            ++same;
        else if ( i == 0 )
        {
            if ( status[i][j] == player ) ++same;
        }
        else if ( status[i][j] == player && ( status[i-1][j+1] == player || status[i-1][j+1] == 'T' ))
            ++same;
        if ( same == 4 )
            return true;
    }
    }

    return false;
}

int main(void)
{
    freopen(in, "rt", stdin);
    freopen(out, "wt", stdout);
    
    int T = 0;
    scanf("%d", &T);
    
    string result;
    char buf[16];
    for (int casenum = 1; casenum <= T; ++casenum)
    {
        for ( int i=0; i<4; ++i ) scanf("%s", &status[i]);
        getchar();
        
        bool isGameCompleted = false;
        bool isXwon          = false;
        bool isOwon          = false;
        
        for ( int i=0; i<4; ++i )
            for ( int j=0; j<4; ++j )
                if ( status[i][j] == '.' )
                {
                    isGameCompleted = false;
                    break;
                }
                else
                    isGameCompleted = true;
        
        isXwon = isWon('X');
        isOwon = isWon('O');
        
        if ( isGameCompleted && !isXwon && !isOwon )
            result = "Draw";
        else if ( isXwon )
            result = "X won";
        else if ( isOwon )
            result = "O won";
        else if ( !isGameCompleted && !isXwon && !isOwon)
            result = "Game has not completed";

        printf("Case #%d: %s\n", casenum, result.c_str());
    }
}
