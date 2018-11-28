#include <iostream>
#include <cstdio>
using namespace std;
char mat[4][5];
int check()
{
    int x , t;
    for(int i = 0 ; i < 4 ; i ++)
    {
        x = 0 , t = 0;
        for(int j = 0 ; j < 4 ; j ++)
        {
            x += mat[i][j] == 'X';
            t += mat[i][j] == 'T';
        }
        if(x + t == 4) return -1;
    }
    for(int i = 0 ; i < 4 ; i ++)
    {
        x = 0 , t = 0;
        for(int j = 0 ; j < 4 ; j ++)
        {
            x += mat[j][i] == 'X';
            t += mat[j][i] == 'T';
        }
        if(x + t == 4) return -1;
    }
    x = 0 , t = 0;
    for(int i = 0 ; i < 4 ; i ++)
    {
        x += mat[i][i] == 'X';
        t += mat[i][i] == 'T';
    }
    if(x + t == 4) return -1;
    x = 0 , t = 0;
    for(int i = 0 ; i < 4 ; i ++)
    {
        x += mat[i][3-i] == 'X';
        t += mat[i][3-i] == 'T';
    }
    if(x + t == 4) return -1;
    for(int i = 0 ; i < 4 ; i ++)
    {
        x = 0 , t = 0;
        for(int j = 0 ; j < 4 ; j ++)
        {
            x += mat[i][j] == 'O';
            t += mat[i][j] == 'T';
        }
        if(x + t == 4) return 1;
    }
    for(int i = 0 ; i < 4 ; i ++)
    {
        x = 0 , t = 0;
        for(int j = 0 ; j < 4 ; j ++)
        {
            x += mat[j][i] == 'O';
            t += mat[j][i] == 'T';
        }
        if(x + t == 4) return 1;
    }
    x = 0 , t = 0;
    for(int i = 0 ; i < 4 ; i ++)
    {
        x += mat[i][i] == 'O';
        t += mat[i][i] == 'T';
    }
    if(x + t == 4) return 1;
    x = 0 , t = 0;
    for(int i = 0 ; i < 4 ; i ++)
    {
        x += mat[i][3-i] == 'O';
        t += mat[i][3-i] == 'T';
    }
    if(x + t == 4) return 1;

    for(int i = 0; i < 4 ; i ++)
    {
        for(int j = 0 ; j < 4 ; j ++)
        {
            if(mat[i][j] == '.')
                return -2;
        }
    }
    return 0;
}
int main()
{
    freopen("C:/Users/v-y/Downloads/A-large.in","r",stdin);
    freopen("C:/Users/v-y/Downloads/A-large.out","w",stdout);
    int t , cas =  1;
    scanf("%d",&t);
    while(t--)
    {
        for(int i = 0 ; i < 4 ; i ++)
        {
            scanf("%s",mat[i]);
        }
        int ans = check();
        if(ans == -2)
        {
            printf("Case #%d: Game has not completed\n",cas++);
        }
        else if(ans == -1)
        {
            printf("Case #%d: X won\n",cas++);
        }
        else if(ans == 1)
        {
            printf("Case #%d: O won\n",cas++);
        }
        else
        {
            printf("Case #%d: Draw\n",cas++);
        }
    }
    return 0;
}
