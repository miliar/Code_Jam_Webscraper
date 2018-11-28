#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	int t, i, j, t_x, t_y, cas_no;
	char table[4][4];
	char templine[6];

	bool Xwin, Owin, draw, blank, incomplete, Texists;

	scanf("%d", &t);
	cas_no = 0;

	while(t--)
	{
	    cas_no++;
	    Xwin = Owin = draw = blank = incomplete = Texists = false;

		for(i=0;i<4;i++)
		{
		    scanf("%s", templine);
		    for(j=0;j<4;j++)
		    {
                table[i][j] = templine[j];
                if(table[i][j] == 'T')
                {
                    Texists = true;
                    t_x = i;
                    t_y = j;
                }
                if(table[i][j] == '.')
                    blank = true;
		    }
		}

        for(i=0;i<4;i++)
        {
            Xwin = true;
            for(j=0;j<4;j++)
            {
                if( (table[i][j] == 'O') || (table[i][j] == '.') )
                {
                    Xwin = false;
                    break;
                }
            }

            if(Xwin == true)
                break;

            Xwin = true;
            for(j=0;j<4;j++)
            {
                if( (table[j][i] == 'O') || (table[j][i] == '.') )
                {
                    Xwin = false;
                    break;
                }
            }

            if(Xwin == true)
                break;

            Owin = true;
            for(j=0;j<4;j++)
            {
                if( (table[i][j] == 'X') || (table[i][j] == '.') )
                {
                    Owin = false;
                    break;
                }
            }

            if(Owin == true)
                break;

            Owin = true;
            for(j=0;j<4;j++)
            {
                if( (table[j][i] == 'X') || (table[j][i] == '.') )
                {
                    Owin = false;
                    break;
                }
            }

            if(Owin == true)
                break;
        }

        if( (Xwin == false) && (Owin == false) )
        {
            Xwin = true;
            for(i=0;i<4;i++)
            {
                if( (table[i][i] == 'O') || (table[i][i] == '.') )
                {
                    Xwin = false;
                    break;
                }

            }
        }

        if( (Xwin == false) && (Owin == false) )
        {
            Owin = true;
            for(i=0;i<4;i++)
            {
                if( (table[i][i] == 'X') || (table[i][i] == '.') )
                {
                    Owin = false;
                    break;
                }
            }
        }

        if( (Xwin == false) && (Owin == false) )
        {
            Xwin = true;
            for(i=0;i<4;i++)
            {
                if( (table[i][3-i] == 'O') || (table[i][3-i] == '.') )
                {
                    Xwin = false;
                    break;
                }
            }
        }

        if( (Xwin == false) && (Owin == false) )
        {
            Owin = true;
            for(i=0;i<4;i++)
            {
                if( (table[i][3-i] == 'X') || (table[i][3-i] == '.') )
                {
                    Owin = false;
                    break;
                }
            }
        }


        if( (Xwin == false) && (Owin == false) )
        {
            if(blank == true)
                incomplete = true;
            else
                draw = true;
        }

        if(Xwin == true)
            printf("Case #%d: X won\n", cas_no);
        else if(Owin == true)
            printf("Case #%d: O won\n", cas_no);
        else if(draw == true)
            printf("Case #%d: Draw\n", cas_no);
        else if(incomplete == true)
            printf("Case #%d: Game has not completed\n", cas_no);

	}

	return 0;
}
