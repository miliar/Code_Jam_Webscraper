#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    int t;
    char chess[5][5];
    scanf("%d",&t);
    for (int cases = 1;cases<=t;++cases)
    {
        printf("Case #%d: ",cases);
        for(int i=0;i<4;++i)
        {
            scanf("%s",chess[i]);
        }
        int ans = -1;
        for (int i=0;i<4;++i)
        {
            if ((chess[i][0] == 'O' || chess[i][0] == 'T') &&
                (chess[i][1] == 'O' || chess[i][1] == 'T') &&
                (chess[i][2] == 'O' || chess[i][2] == 'T') &&
                (chess[i][3] == 'O' || chess[i][3] == 'T')
                )
            {
                if (ans == -1) ans = 0;
                else if (ans == 1) ans = 2;
            }
            if ((chess[i][0] == 'X' || chess[i][0] == 'T') &&
                (chess[i][1] == 'X' || chess[i][1] == 'T') &&
                (chess[i][2] == 'X' || chess[i][2] == 'T') &&
                (chess[i][3] == 'X' || chess[i][3] == 'T')
                )
            {
               if (ans == -1) ans = 1;
                else if (ans == 0) ans = 2;
            }
        }
        for (int i=0;i<4;++i)
        {
            if ((chess[0][i] == 'O' || chess[0][i] == 'T') &&
                (chess[1][i] == 'O' || chess[1][i] == 'T') &&
                (chess[2][i] == 'O' || chess[2][i] == 'T') &&
                (chess[3][i] == 'O' || chess[3][i] == 'T')
                )
            {
                if (ans == -1) ans = 0;
                else if (ans == 1) ans = 2;
            }
            if ((chess[0][i] == 'X' || chess[0][i] == 'T') &&
                (chess[1][i] == 'X' || chess[1][i] == 'T') &&
                (chess[2][i] == 'X' || chess[2][i] == 'T') &&
                (chess[3][i] == 'X' || chess[3][i] == 'T')
                )
            {
               if (ans == -1) ans = 1;
                else if (ans == 0) ans = 2;
            }
        }
        if ((chess[0][0] == 'O' || chess[0][0] == 'T') &&
            (chess[1][1] == 'O' || chess[1][1] == 'T') &&
            (chess[2][2] == 'O' || chess[2][2] == 'T') &&
            (chess[3][3] == 'O' || chess[3][3] == 'T')
            )
        {
            if (ans == -1) ans = 0;
            else if (ans == 1) ans = 2;
        }
        if ((chess[0][0] == 'X' || chess[0][0] == 'T') &&
            (chess[1][1] == 'X' || chess[1][1] == 'T') &&
            (chess[2][2] == 'X' || chess[2][2] == 'T') &&
            (chess[3][3] == 'X' || chess[3][3] == 'T')
            )
        {
           if (ans == -1) ans = 1;
            else if (ans == 0) ans = 2;
        }
        if ((chess[0][3] == 'O' || chess[0][3] == 'T') &&
            (chess[1][2] == 'O' || chess[1][2] == 'T') &&
            (chess[2][1] == 'O' || chess[2][1] == 'T') &&
            (chess[3][0] == 'O' || chess[3][0] == 'T')
            )
        {
            if (ans == -1) ans = 0;
           else if (ans == 1) ans = 2;
        }
        if ((chess[0][3] == 'X' || chess[0][3] == 'T') &&
            (chess[1][2] == 'X' || chess[1][2] == 'T') &&
            (chess[2][1] == 'X' || chess[2][1] == 'T') &&
            (chess[3][0] == 'X' || chess[3][0] == 'T')
            )
        {
           if (ans == -1) ans = 1;
            else if (ans == 0) ans = 2;
        }
        if (ans == -1)
        {
            bool flag = false;
            for (int i=0;i<4;++i)
            {
                for (int j=0;j<4;++j)
                {
                    if (chess[i][j] == '.') flag = true;
                }
            }
            if (flag == false) ans = 2;
        }
        switch(ans)
        {
            case 0: puts("O won");break;
            case 1: puts("X won");break;
            case 2: puts("Draw");break;
            case -1: puts("Game has not completed");break;
        }
    }
    return 0;
}
