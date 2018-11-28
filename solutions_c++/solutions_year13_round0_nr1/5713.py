//
//  main.cpp
//  acm
//
//  Created by Anton Kholkin on 4/6/13.
//  Copyright (c) 2013 Anton Kholkin. All rights reserved.
//

#include <iostream>
#include <map>
#include <vector>

#define MOD 1000000009

using namespace std;

int main(int argc, const char * argv[])
{
    freopen( "input.txt", "r", stdin );
    freopen( "output.txt", "w+", stdout );
    
    int pos[10][4][2] = {
        { {0,0}, {0,1}, {0,2}, {0,3} },
        { {1,0}, {1,1}, {1,2}, {1,3} },
        { {2,0}, {2,1}, {2,2}, {2,3} },
        { {3,0}, {3,1}, {3,2}, {3,3} },
        
        { {0,0}, {1,0}, {2,0}, {3,0} },
        { {0,1}, {1,1}, {2,1}, {3,1} },
        { {0,2}, {1,2}, {2,2}, {3,2} },
        { {0,3}, {1,3}, {2,3}, {3,3} },

        { {0,0}, {1,1}, {2,2}, {3,3} },
        { {0,3}, {1,2}, {2,1}, {3,0} }
    };

    int _; scanf( "%d", &_ );
    
    for ( int tc = 0; tc < _; tc++ )
    {
        char grid[4][4] = {0};
        char c;
        int i = 0, j = 0;
        while( ( c = getc(stdin) ) && c != EOF )
        {
            if ( c == '.' ||  c == 'O' || c == 'X' || c == 'T' )
            {
                grid[ i ][ j ] = c;
                if ( j == 3 ) i++, j = 0;
                else j++;
            }
            if ( i == 4 ) break;
        }
        bool notComplete = false,
             winO = false,
             winX = false;
        for ( int i = 0; i < 10; i++ )
        {
            char last = 'T', cnt = 0, who = 0;
            for ( int j = 0; j < 4; j++ )
            {
                int row = pos[ i ][ j ][ 0 ], col = pos[ i ][ j ][ 1 ];
                char curr = grid[ row ][ col ];
                if ( ( curr == 'X' || curr == 'O' || curr == 'T' ) && ( curr == last || last == 'T' || curr == 'T' ) )
                {
                    cnt++;
                    if ( curr != 'T' ) who = curr;
                }
                else
                {
                    if ( curr == '.' ) notComplete = true;
                    cnt = 0;
                }
                last = curr;
            }
            if ( cnt == 4 )
            {
                if ( who == 'X' ) winX = true; else winO = true;
                break;
            }
        }
        char * s;
        if ( winX ) s = "X won";
        else if ( winO ) s = "O won";
        else if ( notComplete ) s = "Game has not completed";
        else s = "Draw";
        
        printf( "Case #%d: %s\n", tc+1, s );
    }
    
    return 0;
}

