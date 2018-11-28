#include <stdio.h>

using namespace std;

int main()
{
    int T; scanf("%d", &T);
    char b[5][5];
    int stat; scanf("%c", &b[0][0]);
    for (int c = 1; c <= T; c++)
    {        
        for (int j = 0; j < 4; j++)
            for (int k = 0; k < 5; k++)
                scanf("%c", &b[j][k]);
                
        int x = 0, o = 0;
        int xp = 0, op = 0;
        int xd = 0, od = 0;
        int xd2 = 0, od2 = 0;
        int p1 = 0, p2 = 0, p3 = 0, p4 = 0;
        bool inc = false;
        for (int i = 0; i < 4; i++)
        {
            for (int j = 0; j < 4; j++)
            {                
                if (b[i][j] == 'X') 
                    x++;
                if (b[i][j] == 'O')
                    o++;
                if (b[j][i] == 'X') 
                    xp++;
                if (b[j][i] == 'O')
                    op++;
                if (b[i][j] == 'T')
                    p1++;
                if (b[j][i] == 'T')
                    p2++;


                if (i == j)
                {
                    if (b[i][j] == 'X') 
                        xd++;
                    if (b[i][j] == 'O')
                        od++;
                    if (b[i][j] == 'T')
                        p3++;
                }

                if (i + j == 3)
                {
                    if (b[i][j] == 'X') 
                        xd2++;
                    if (b[i][j] == 'O')                    
                        od2++; 
                    if (b[i][j] == 'T')
                        p4++;                   
                }

                if (b[i][j] == '.')
                    inc = true;                  
                
            }                                

            if (x + p1  == 4
                || o + p1 == 4
                || xp + p2 == 4
                || op + p2 == 4
                || xd + p3 == 4
                || od + p3 == 4
                || xd2 + p4 == 4
                || od2 + p4 == 4)
            break;

        x = o = 0;
            xp = op = 0;
            p1 = p2 = 0;
        }
        
        scanf("%c", &b[0][0]);
        if (x + p1 == 4 || xp + p2 == 4 || xd + p3 == 4 || xd2 + p4 == 4)
            printf("Case #%d: X won\n", c);
        else if (o + p1 == 4 || op + p2 == 4 || od + p3 == 4 || od2 + p4 == 4)
            printf("Case #%d: O won\n", c);
        else if (inc)
            printf("Case #%d: Game has not completed\n", c);
        else
            printf("Case #%d: Draw\n", c);
    }
}
