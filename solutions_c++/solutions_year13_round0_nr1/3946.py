#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

char game[6][6];

bool judge(char game[6][6] , char hdl)
{
    if((game[1][1]==hdl || game[1][1]=='T') && game[2][1]==hdl && game[3][1]==hdl && game[4][1]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl && (game[2][1]==hdl || game[2][1]=='T') && game[3][1]==hdl && game[4][1]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl && game[2][1]==hdl && (game[3][1]==hdl || game[3][1]=='T') && game[4][1]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl && game[2][1]==hdl && game[3][1]==hdl && (game[4][1]==hdl || game[4][1]=='T'))
    {
        return true;
    }
    else if((game[1][2]==hdl || game[1][2]=='T') && game[2][2]==hdl && game[3][2]==hdl && game[4][2]==hdl)
    {
        return true;
    }
    else if(game[1][2]==hdl && (game[2][2]==hdl || game[2][2]=='T') && game[3][2]==hdl && game[4][2]==hdl)
    {
        return true;
    }
    else if(game[1][2]==hdl && game[2][2]==hdl && (game[3][2]==hdl || game[3][2]=='T') && game[4][2]==hdl)
    {
        return true;
    }
    else if(game[1][2]==hdl && game[2][2]==hdl && game[3][2]==hdl && (game[4][2]==hdl || game[4][2]=='T'))
    {
        return true;
    }
    else if((game[1][3]==hdl || game[1][3]=='T') && game[2][3]==hdl && game[3][3]==hdl && game[4][3]==hdl)
    {
        return true;
    }
    else if(game[1][3]==hdl && (game[2][3]==hdl || game[2][3]=='T') && game[3][3]==hdl && game[4][3]==hdl)
    {
        return true;
    }
    else if(game[1][3]==hdl && game[2][3]==hdl && (game[3][3]==hdl || game[3][3]=='T') && game[4][3]==hdl)
    {
        return true;
    }
    else if(game[1][3]==hdl && game[2][3]==hdl && game[3][3]==hdl && (game[4][3]==hdl || game[4][3]=='T'))
    {
        return true;
    }
    else if((game[1][4]==hdl || game[1][4]=='T')  && game[2][4]==hdl && game[3][4]==hdl && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[1][4]==hdl  && (game[2][4]==hdl || game[2][4]=='T') && game[3][4]==hdl && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[1][4]==hdl  && game[2][4]==hdl && (game[3][4]==hdl || game[3][4]=='T') && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[1][4]==hdl  && game[2][4]==hdl && game[3][4]==hdl && (game[4][4]==hdl || game[4][4]=='T'))
    {
        return true;
    }
    else if((game[1][1]==hdl || game[1][1]=='T') && game[1][2]==hdl && game[1][3]==hdl && game[1][4]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl&& (game[1][2]==hdl || game[1][2]=='T') && game[1][3]==hdl && game[1][4]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl && game[1][2]==hdl && (game[1][3]==hdl || game[1][3]=='T') && game[1][4]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl && game[1][2]==hdl && game[1][3]==hdl && (game[1][4]==hdl || game[1][4]=='T'))
    {
        return true;
    }
    else if((game[2][1]==hdl || game[2][1]=='T') && game[2][2]==hdl && game[2][3]==hdl && game[2][4]==hdl)
    {
        return true;
    }
    else if(game[2][1]==hdl && (game[2][2]==hdl || game[2][2]=='T') && game[2][3]==hdl && game[2][4]==hdl)
    {
        return true;
    }
    else if(game[2][1]==hdl  && game[2][2]==hdl && (game[2][3]==hdl || game[2][3]=='T') && game[2][4]==hdl)
    {
        return true;
    }
    else if(game[2][1]==hdl && game[2][2]==hdl && game[2][3]==hdl && (game[2][4]==hdl || game[2][4]=='T'))
    {
        return true;
    }
    else if((game[3][1]==hdl || game[3][1]=='T') && game[3][2]==hdl && game[3][3]==hdl && game[3][4]==hdl)
    {
        return true;
    }
    else if(game[3][1]==hdl && (game[3][2]==hdl || game[3][2]=='T') && game[3][3]==hdl && game[3][4]==hdl)
    {
        return true;
    }
    else if(game[3][1]==hdl && game[3][2]==hdl && (game[3][3]==hdl || game[3][3]=='T') && game[3][4]==hdl)
    {
        return true;
    }
    else if(game[3][1]==hdl && game[3][2]==hdl && game[3][3]==hdl && (game[3][4]==hdl || game[3][4]=='T'))
    {
        return true;
    }
    else if((game[4][1]==hdl || game[4][1]=='T') && game[4][2]==hdl && game[4][3]==hdl && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[4][1]==hdl && (game[4][2]==hdl || game[4][2]=='T') && game[4][3]==hdl && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[4][1]==hdl && game[4][2]==hdl && (game[4][3]==hdl || game[4][3]=='T') && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[4][1]==hdl && game[4][2]==hdl && game[4][3]==hdl && (game[4][4]==hdl || game[4][4]=='T'))
    {
        return true;
    }
    else if((game[1][4]==hdl || game[1][4]=='T') && game[2][3]==hdl && game[3][2]==hdl && game[4][1]==hdl)
    {
        return true;
    }
    else if(game[1][4]==hdl && (game[2][3]==hdl || game[2][3]=='T') && game[3][2]==hdl && game[4][1]==hdl)
    {
        return true;
    }
    else if(game[1][4]==hdl && game[2][3]==hdl && (game[3][2]==hdl || game[3][2]=='T') && game[4][1]==hdl)
    {
        return true;
    }
    else if(game[1][4]==hdl && game[2][3]==hdl && game[3][2]==hdl && (game[4][1]==hdl || game[4][1]=='T'))
    {
        return true;
    }
    else if((game[1][1]==hdl || game[1][1]=='T') && game[2][2]==hdl && game[3][3]==hdl && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl && (game[2][2]==hdl || game[2][2]=='T') && game[3][3]==hdl && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl && game[2][2]==hdl && (game[3][3]==hdl || game[3][3]=='T') && game[4][4]==hdl)
    {
        return true;
    }
    else if(game[1][1]==hdl && game[2][2]==hdl && game[3][3]==hdl && (game[4][4]==hdl || game[4][4]=='T'))
    {
        return true;
    }

    return false;

}

int main()
{
    freopen( "input.in", "r", stdin );
	freopen( "output.out", "w", stdout );

	int test,kase=0;
	scanf("%d",&test);

	while(test--)
	{
        int val1=0,val2=0,valt=0;

        scanf("%s", game[1] + 1);
        scanf("%s", game[2] + 1);
        scanf("%s", game[3] + 1);
        scanf("%s", game[4] + 1);

        for(int i=1;i<=4;i++)
        {
            for(int j=1 ;j<=4 ;j++)
            {
                if(game[i][j]=='X')
                {
                    val1++;
                }
                else if(game[i][j]=='O')
                {
                    val2++;
                }
                else if(game[i][j]=='T')
                {
                    valt++;
                }
            }
        }

        printf("Case #%d:",++kase);


        if((val1 - val2 < 2) && val1 >= val2)
        {
            if((val1 > val2) && judge(game , 'X'))
            {
                printf(" X won\n");
            }
            else if((val1 == val2) && judge(game, 'O'))
            {
                printf(" O won\n");
            }
            else if(val1 + val2 + valt==16)
            {
                printf(" Draw\n");
            }
            else
            {
                printf(" Game has not completed\n");
            }
        }

	}

    return 0;
}
