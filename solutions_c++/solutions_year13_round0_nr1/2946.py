#include <cctype>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <cstring>

#include <fstream>
#include <iostream>

#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <utility>

using namespace std;



enum gameState { xWin, oWin, draw, nc };




int main(void)
{
	int T;
	int i,j,k,l,n,m,x,y;

    gameState state;
	char board[4][4];
    int rowSum[4];
    int colSum[4];
    int diaSum[2];

	fstream input, output;

	input.open("A-large.in", fstream::in);
	output.open("output.txt", fstream::out);

	if ( ! input.is_open() || ! output.is_open() )
	{
		cout << "well..." << endl;
		return -1;
	}

	input >> T;

	for ( n = 0; n < T; n++ )
	{
        state = draw;
        
        for ( i = 0; i < 4; i++ )
        {
            rowSum[i] = 0;
            colSum[i] = 0;
            diaSum[i%2] = 0;
        }
        
        for ( x = 0; x < 4; x++ )
        {
            for ( y = 0; y < 4; y++ )
            {
                input >> board[x][y];
                
                if ( board[x][y] == '.' )
                    state = nc;
                
                else
                {
                    rowSum[y] += board[x][y];
                    colSum[x] += board[x][y];
                    if ( x == y )
                        diaSum[0] += board[x][y];
                    if ( x + y == 3 )
                        diaSum[1] += board[x][y];
                }
            }
        }
        
        for ( i = 0; i < 4; i++ )
        {
            if (   rowSum[i] == 'X'*4
                || rowSum[i] == 'X'*3+'T'
                || colSum[i] == 'X'*4
                || colSum[i] == 'X'*3+'T'
                || diaSum[i%2] == 'X'*4
                || diaSum[i%2] == 'X'*3+'T' )
            {
                state = xWin;
                break;
            }
            
            if (   rowSum[i] == 'O'*4
                || rowSum[i] == 'O'*3+'T'
                || colSum[i] == 'O'*4
                || colSum[i] == 'O'*3+'T'
                || diaSum[i%2] == 'O'*4
                || diaSum[i%2] == 'O'*3+'T' )
            {
                state = oWin;
                break;
            }
        }
        
        
        
		output << "Case #" << n+1 << ": ";
        
        switch (state) {
            case xWin:
                output << "X won" << endl;
                break;
            case oWin:
                output << "O won" << endl;
                break;
            case draw:
                output << "Draw" << endl;
                break;
            case nc:
                output << "Game has not completed" << endl;
                break;
        }
	}

	input.close();
	output.close();

	return 0;
}







/* */