#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    int T, a[4][4], cnt = 0;
    char ch;
    scanf("%d", &T);
    getchar();
    while(T--) //cout<<T<<endl, T--)
    {
        memset(a, 0, sizeof(a));
        printf("Case #%d: ", ++cnt);
        int f_full = 1;
        int cX, cO, cT, f_win = 0;
        for(int i=0; i<4; i++)
        {
            cX = cO = cT = 0;
            for(int j=0; j<4;j++)
            {
                ch = getchar();
                switch(ch)
                {
                    case 'X':
                        a[i][j] = 1;
                        cX ++;
                        break;
                    case 'T':
                        a[i][j] = -1;
                        cT ++;
                        break;
                    case 'O':
                        a[i][j] = 2;
                        cO ++;
                        break;
                    case '.':
                        a[i][j] = 0;
                        f_full = 0;
                        break;
                    default:
                        break;
                }
            }
            getchar();
        }

        /*
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                cout<<a[i][j]<<' ';
            cout<<endl;
        }
        */

        if(!f_win)
        {
            for(int i=0; i<4;i++)
            {
                cX = cO = cT = 0;
                for(int j=0; j<4; j++)
                {
                    switch(a[i][j])
                    {
                        case -1:
                            cT++;
                            break;
                        case 1:
                            cX++;
                            break;
                        case 2:
                            cO++;
                            break;
                    }
                }
                if(!f_win)
                {
                    if(cX == 4 || (cX == 3 && cT == 1))
                    {
                        printf("X won\n");
                        f_win = 1;
                        break;
                    }
                    if(cO == 4 || (cO == 3 && cT == 1))
                    {
                        printf("O won\n");
                        f_win = 1;
                        break;
                    }
                }
            }
        }
        if(!f_win)
        {
            for(int i=0; i<4;i++)
            {
                cX = cO = cT = 0;
                for(int j=0; j<4; j++)
                {
                    switch(a[j][i])
                    {
                        case -1:
                            cT++;
                            break;
                        case 1:
                            cX++;
                            break;
                        case 2:
                            cO++;
                            break;
                    }
                }
                if(!f_win)
                {
                    if(cX == 4 || (cX == 3 && cT == 1))
                    {
                        printf("X won\n");
                        f_win = 1;
                        break;
                    }
                    if(cO == 4 || (cO == 3 && cT == 1))
                    {
                        printf("O won\n");
                        f_win = 1;
                        break;
                    }
                }
            }
        }
        if(!f_win)
        {
            cX = cO = cT = 0;
            for(int j=0; j<4; j++)
            {
                switch(a[j][j])
                {
                    case -1:
                        cT++;
                        break;
                    case 1:
                        cX++;
                        break;
                    case 2:
                        cO++;
                        break;
                }
            }
            if(!f_win)
            {
                if(cX == 4 || (cX == 3 && cT == 1))
                {
                    printf("X won\n");
                    f_win = 1;
                    getchar();
                    continue;
                }
                if(cO == 4 || (cO == 3 && cT == 1))
                {
                    printf("O won\n");
                    f_win = 1;
                    getchar();
                    continue;
                }
            }
        }
        if(!f_win)
        {
            cX = cO = cT = 0;
            for(int j=0; j<4; j++)
            {
                switch(a[j][3-j])
                {
                    case -1:
                        cT++;
                        break;
                    case 1:
                        cX++;
                        break;
                    case 2:
                        cO++;
                        break;
                }
            }
            if(!f_win)
            {
                if(cX == 4 || (cX == 3 && cT == 1))
                {
                    printf("X won\n");
                    f_win = 1;
                    getchar();
                    continue;
                }
                if(cO == 4 || (cO == 3 && cT == 1))
                {
                    printf("O won\n");
                    f_win = 1;
                    getchar();
                    continue;
                }
            }
        }
        if(!f_win)
        {
            if(f_full) printf("Draw\n");
            else printf("Game has not completed\n");
        }
        getchar();
    }
    return 0;
}
