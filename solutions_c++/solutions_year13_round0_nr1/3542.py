#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
	int t, i, j, tx, ty, cas;
	char board[4][4];
	char templine[6];

	bool xwon, owon, draw, dot, notcomp, Tflag;

	scanf("%d", &t);
	cas = 0;

	while(t--)
	{
	    cas++;
	    xwon = owon = draw = dot = notcomp = Tflag = false;

		for(i=0;i<4;i++)
		{
		    scanf("%s", templine);
		    for(j=0;j<4;j++)
		    {
                board[i][j] = templine[j];
                if(board[i][j] == 'T')
                {
                    Tflag = true;
                    tx = i;
                    ty = j;
                }
                if(board[i][j] == '.')
                    dot = true;
		    }
		}

        for(i=0;i<4;i++)
        {
            xwon = true;
            for(j=0;j<4;j++)
            {
                if( (board[i][j] == 'O') || (board[i][j] == '.') )
                {
                    xwon = false;
                    break;
                }
            }

            if(xwon == true)
                break;

            xwon = true;
            for(j=0;j<4;j++)
            {
                if( (board[j][i] == 'O') || (board[j][i] == '.') )
                {
                    xwon = false;
                    break;
                }
            }

            if(xwon == true)
                break;

            owon = true;
            for(j=0;j<4;j++)
            {
                if( (board[i][j] == 'X') || (board[i][j] == '.') )
                {
                    owon = false;
                    break;
                }
            }

            if(owon == true)
                break;

            owon = true;
            for(j=0;j<4;j++)
            {
                if( (board[j][i] == 'X') || (board[j][i] == '.') )
                {
                    owon = false;
                    break;
                }
            }

            if(owon == true)
                break;
        }

        if( (xwon == false) && (owon == false) )
        {
            xwon = true;
            for(i=0;i<4;i++)
            {
                if( (board[i][i] == 'O') || (board[i][i] == '.') )
                {
                    xwon = false;
                    break;
                }

            }
        }

        if( (xwon == false) && (owon == false) )
        {
            owon = true;
            for(i=0;i<4;i++)
            {
                if( (board[i][i] == 'X') || (board[i][i] == '.') )
                {
                    owon = false;
                    break;
                }
            }
        }

        if( (xwon == false) && (owon == false) )
        {
            xwon = true;
            for(i=0;i<4;i++)
            {
                if( (board[i][3-i] == 'O') || (board[i][3-i] == '.') )
                {
                    xwon = false;
                    break;
                }
            }
        }

        if( (xwon == false) && (owon == false) )
        {
            owon = true;
            for(i=0;i<4;i++)
            {
                if( (board[i][3-i] == 'X') || (board[i][3-i] == '.') )
                {
                    owon = false;
                    break;
                }
            }
        }


        if( (xwon == false) && (owon == false) )
        {
            if(dot == true)
                notcomp = true;
            else
                draw = true;
        }

        if(xwon == true)
            printf("Case #%d: X won\n", cas);
        else if(owon == true)
            printf("Case #%d: O won\n", cas);
        else if(draw == true)
            printf("Case #%d: Draw\n", cas);
        else if(notcomp == true)
            printf("Case #%d: Game has not completed\n", cas);

	}

	return 0;
}
