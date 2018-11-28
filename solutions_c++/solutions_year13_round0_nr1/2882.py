//
//  main.cpp
//  cj13_round0_a
//
//  Created by Peizhi Wu on 4/12/13.
//  Copyright (c) 2013 Peizhi Wu. All rights reserved.
//

#include <iostream>
#include <cstdio>

int main()
{
    int T, TN, i, j, flag, end;
    char ch;
    int xmap[4][4], omap[4][4];
    freopen("/Users/Peizhi/Documents/cpp/cj13_round0_a/cj13_round0_a/A-large.in","r",stdin);
    freopen("/Users/Peizhi/Documents/cpp/cj13_round0_a/cj13_round0_a/A-large.txt","w",stdout);
    scanf("%d\n", &TN);
    for (T = 0; T<TN; T++)
    {
        flag = 0;
        end = 0;                   //draw
        for (i = 0; i<4; i++)
            for (j = 0; j<4; j++)
            {   scanf("%c", &ch);
                if (ch=='\n') scanf("%c", &ch);
                if (ch == '.')
                    {   end = 1;       //no finished
                        xmap[i][j] = 0;
                        omap[i][j] = 0;
                    }
                else if(ch == 'X')
                {
                    xmap[i][j] = 1;
                    omap[i][j] = 0;
                }
                else if(ch == 'O')
                {
                    xmap[i][j] = 0;
                    omap[i][j] = 1;
                }
                else if(ch == 'T')
                {
                    xmap[i][j] = 1;
                    omap[i][j] = 1;
                }
            }
//        for (i = 0; i<4; i++){
//            for (j = 0; j<4; j++)
//                printf("%d ", omap[i][j]);
//            printf("\n");
//        }
        for (i = 0; i<4; i++)
        {   if (xmap[i][0]+xmap[i][1]+xmap[i][2]+xmap[i][3] > 3)
                flag =2;
            else if (omap[i][0]+omap[i][1]+omap[i][2]+omap[i][3] > 3)
                flag =3;
            else if (xmap[0][i]+xmap[1][i]+xmap[2][i]+xmap[3][i] > 3)
                flag =2;
            else if (omap[0][i]+omap[1][i]+omap[2][i]+omap[3][i] > 3)
                flag =3;
        }
        if (xmap[0][0]+xmap[1][1]+xmap[2][2]+xmap[3][3] > 3)
            flag =2;
        else if (omap[0][0]+omap[1][1]+omap[2][2]+omap[3][3] > 3)
            flag =3;
        if (xmap[0][3]+xmap[1][2]+xmap[2][1]+xmap[3][0] > 3)
            flag =2;
        else if (omap[0][3]+omap[1][2]+omap[2][1]+omap[3][0] > 3)
            flag =3;
        printf("Case #%d: ", T+1);
        switch (flag)
        {
            case (0):
                if (end)
                    printf("Game has not completed\n");
                else
                    printf("Draw\n");
                break;
            case (2): printf("X won\n"); break;
            case (3): printf("O won\n");
        }
        getchar();
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


