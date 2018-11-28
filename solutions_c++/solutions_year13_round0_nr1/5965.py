#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
using namespace std;


int main() 
{

        freopen ("A-large.in","r",stdin);
        freopen ("out.txt","w",stdout);

        int T;
        scanf("%d",&T);


        int testcase=0;
        while(T--)
        {
            char s[4][5];
            for(int i=0;i<4;i++)
            {
                scanf("%s",s[i]);
            }
            
            scanf("%*[^\n]");

            //check if O won or X won
            //1. check all rows
            int flagO=0;
            int flagX=0;
            for(int r=0;r<4;r++)
            {
                int countO=0;
                int countT=0;
                int countX=0;
                for(int c=0;c<4;c++)
                {
                    if(s[r][c]=='O') ++countO;
                    if(s[r][c]=='T') ++countT;
                    if(s[r][c]=='X') ++countX;
                }

                if(countO==4 || (countO==3 && countT==1))
                {
                    flagO=1;
                    break;
                }
                
                if(countX==4 || (countX==3 && countT==1))
                {
                    flagX=1;
                    break;
                }

            }

            if(flagO == 1)
            {
                printf("Case #%d: O won\n",++testcase);
                continue;
            }

            if(flagX == 1)
            {
                printf("Case #%d: X won\n",++testcase);
                continue;
            }


            //2. check all columns
            flagO=0;
            flagX=0;
            for(int c=0;c<4;c++)
            {
                int countO=0;
                int countT=0;
                int countX=0;
                for(int r=0;r<4;r++)
                {
                    if(s[r][c]=='O') ++countO;
                    if(s[r][c]=='T') ++countT;
                    if(s[r][c]=='X') ++countX;
                }

                if(countO==4 || (countO==3 && countT==1))
                {
                    flagO=1;
                    break;
                }
                
                if(countX==4 || (countX==3 && countT==1))
                {
                    flagX=1;
                    break;
                }

            }

            if(flagO == 1)
            {
                printf("Case #%d: O won\n",++testcase);
                continue;
            }

            if(flagX == 1)
            {
                printf("Case #%d: X won\n",++testcase);
                continue;
            }

            //3.check diagonals
            flagO=0;
            flagX=0;
            int countO=0;
            int countT=0;
            int countX=0;
            //forward diagonal
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                {
                    if(i==j) 
                    {
                        if(s[i][j] == 'O' ) ++countO;
                        if(s[i][j] == 'X' ) ++countX;
                        if(s[i][j] == 'T' ) ++countT;
                    }
                }
                if(countO==4 || (countO==3 && countT==1))
                {
                    flagO=1;
                    break;
                }
                
                if(countX==4 || (countX==3 && countT==1))
                {
                    flagX=1;
                    break;
                }
            }   

            if(flagO == 1)
            {
                printf("Case #%d: O won\n",++testcase);
                continue;
            }

            if(flagX == 1)
            {
                printf("Case #%d: X won\n",++testcase);
                continue;
            }



            countO=0;
            countT=0;
            countX=0;

            if(s[0][3] == 'O') ++countO;if(s[0][3] == 'X') ++countX; if(s[0][3] == 'T') ++countT;
            if(s[1][2] == 'O') ++countO;if(s[1][2] == 'X') ++countX; if(s[1][2] == 'T') ++countT;
            if(s[2][1] == 'O') ++countO;if(s[2][1] == 'X') ++countX; if(s[2][1] == 'T') ++countT;
            if(s[3][0] == 'O') ++countO;if(s[3][0] == 'X') ++countX; if(s[3][0] == 'T') ++countT;
            
            if(countO==4 || (countO==3 && countT==1))
            {
                    flagO=1;
                    
            }
                
            if(countX==4 || (countX==3 && countT==1))
            {
                    flagX=1;
                
            }

            if(flagO == 1)
            {
                printf("Case #%d: O won\n",++testcase);
                continue;
            }

            if(flagX == 1)
            {
                printf("Case #%d: X won\n",++testcase);
                continue;
            }





            //4. check if . is present, if yes then game is not complete, else game is draw
            int flagDot=0;
            for(int i=0;i<4;i++)
            {
                for(int j=0;j<4;j++)
                {
                    if(s[i][j]=='.')
                    {
                        flagDot=1;
                        break;
                    }
                }

                if(flagDot)
                {
                    break;
                }
            }


            if(flagDot)
            {
                printf("Case #%d: Game has not completed\n",++testcase);
            }
            else
            {
                printf("Case #%d: Draw\n",++testcase);
            }
        }

		return 0;
}


