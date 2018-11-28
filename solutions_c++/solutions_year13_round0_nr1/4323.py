#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

int main()
{
    int cse, t = 1;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    scanf("%d", &cse);
    while(cse --)
    {
        char a[5][5];
        for(int i = 0; i < 4; i ++)
            scanf("%s", a[i]);
        bool Xwin = false;
        bool Owin = false;
        printf("Case #%d: ", t ++);
        for(int i = 0; i < 4; i ++)
        {
            for(int j = 0; j < 4; j ++)
            {
                if(a[i][j] != 'X' && a[i][j] != 'T')
                    break;
                if(j == 3)
                    Xwin = true;
            }
            if(Xwin == true)
                break;
        }
        for(int j = 0; j < 4; j ++)
        {
            for(int i = 0; i < 4; i ++)
            {
                if(a[i][j] != 'X' && a[i][j] != 'T')
                    break;
                if(i == 3)
                    Xwin = true;
            }
        }
        for(int i = 0; i < 4; i ++)
        {
            if(a[i][i] != 'X' && a[i][i] != 'T')
                break;
            if(i == 3)
                Xwin = true;
        }
        for(int i = 0; i < 4; i ++)
        {
            if(a[i][3 - i] != 'X' && a[i][3 - i] != 'T')
                break;
            if(i == 3)
                Xwin = true;
        }
        if(Xwin == true)
        {
            printf("X won\n");
            continue;
        }
        for(int i = 0; i < 4; i ++)
        {
            for(int j = 0; j < 4; j ++)
            {
                if(a[i][j] != 'O' && a[i][j] != 'T')
                    break;
                if(j == 3)
                    Owin = true;
            }
            if(Owin == true)
                break;
        }
        for(int j = 0; j < 4; j ++)
        {
            for(int i = 0; i < 4; i ++)
            {
                if(a[i][j] != 'O' && a[i][j] != 'T')
                    break;
                if(i == 3)
                    Owin = true;
            }
        }
        for(int i = 0; i < 4; i ++)
        {
            if(a[i][i] != 'O' && a[i][i] != 'T')
                break;
            if(i == 3)
                Owin = true;
        }
        for(int i = 0; i < 4; i ++)
        {
            if(a[i][3 - i] != 'O' && a[i][3 - i] != 'T')
                break;
            if(i == 3)
                Owin = true;
        }
        if(Owin == true)
        {
            printf("O won\n");
            continue;
        }
        bool draw = true;
        for(int i = 0; i < 4; i ++)
        {
            for(int j = 0; j < 4; j ++)
                if(a[i][j] == '.')
                    draw = false;
        }
        if(draw == true)
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
}
