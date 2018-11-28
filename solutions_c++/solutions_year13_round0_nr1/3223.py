#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    freopen("a1.in","r",stdin);
    freopen("out.txt","w",stdout);
    char map[10][10];
    char temp[10];
    int n;
    scanf("%d",&n);
    for(int k = 0;k < n; ++k)
    {
         cin.getline(temp,10);
        for(int i = 0;i < 4; ++i)
        {
                cin.getline(map[i],10);
        }
        int cal1 = 0,cal2 = 0,empty = 0;
        int ans = -1;
        for(int i = 0;i < 4; ++i)
        {
            cal1 = 0; cal2 = 0;
            for(int j = 0;j < 4; ++j)
            {
                if(map[i][j] == 'X' || map[i][j] == 'T')
                    cal1++;
                if(map[i][j] == 'O' || map[i][j] == 'T')
                    cal2++;
                if(map[i][j] == '.')
                {
                    empty++;
                }
            }
            if(cal1 >= 4)
            {
                   ans = 1;
                   break;
            }
            if(cal2 >= 4)
            {
                ans = 2;
                break;
            }

        }

        if(ans == -1)
        {
            for(int i = 0;i < 4; ++i)
            {
                cal1 = 0; cal2 = 0;
                for(int j = 0;j < 4; ++j)
                {
                    if(map[j][i] == 'X' || map[j][i] == 'T')
                    cal1++;
                    if(map[j][i] == 'O' || map[j][i] == 'T')
                    cal2++;
                }
                if(cal1 >= 4)
                {
                   ans = 1;
                   break;
                }
                if(cal2 >= 4)
                {
                    ans = 2;
                    break;
                }
            }
        }
        if(ans == -1)
        {
            cal1 = 0; cal2 = 0;
            for(int i = 0;i < 4; ++i)
            {
                if(map[i][i] == 'X' || map[i][i] == 'T')
                cal1++;
                if(map[i][i] == 'O' || map[i][i] == 'T')
                cal2++;
            }
            if(cal1 >= 4)
            {
                ans = 1;
            }
            if(cal2 >= 4)
            {
                ans = 2;
            }
        }
        if(ans == -1)
        {
            cal1 = 0; cal2 = 0;
            for(int i = 0;i < 4; ++i)
            {
                if(map[i][3-i] == 'X' || map[i][3-i] == 'T')
                cal1++;
                if(map[i][3-i] == 'O' || map[i][3-i] == 'T')
                cal2++;
            }
            if(cal1 >= 4)
            {
                ans = 1;
            }
            if(cal2 >= 4)
            {
                ans = 2;
            }
        }
        if(ans == -1 && empty == 0)
        {
            ans = 3;
        }
        printf("Case #%d: ",k+1);
        if(ans == 1)
        printf("X won\n");
        if(ans == 2)
        printf("O won\n");
        if(ans == 3)
        printf("Draw\n");
        if(ans == -1)
        printf("Game has not completed\n");
    }
    return 0;
}
