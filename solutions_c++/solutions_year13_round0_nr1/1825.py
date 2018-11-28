#include <cstdio>
#include <iostream>
using namespace std;

char board[8][8];

int check(char piece)
{
    int i,j,cnt;
    for(i=0;i<4;i++)
    {
        cnt=0;
        for(j=0;j<4;j++)
        {
            if((board[i][j]==piece)||(board[i][j]=='T'))
            {
                cnt++;
            }
        }
        if(cnt==4)
        {
            return 1;
        }
    }
    for(i=0;i<4;i++)
    {
        cnt=0;
        for(j=0;j<4;j++)
        {
            if((board[j][i]==piece)||(board[j][i]=='T'))
            {
                cnt++;
            }
        }
        if(cnt==4)
        {
            return 1;
        }
    }
    cnt=0;
    for(i=0;i<4;i++)
    {
        if((board[i][i]==piece)||(board[i][i]=='T'))
        {
            cnt++;
        }
    }
    if(cnt==4)
    {
        return 1;
    }
    cnt=0;
    for(i=0;i<4;i++)
    {
        if((board[i][3-i]==piece)||(board[i][3-i]=='T'))
        {
            cnt++;
        }
    }
    if(cnt==4)
    {
        return 1;
    }
    return 0;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int c,t,i,j,cnt;
    scanf("%d",&t);
    for(c=0;c<t;c++)
    {
        cnt=0;
        for(i=0;i<4;i++)
        {
            scanf("%s",board[i]);
            for(j=0;j<4;j++)
            {
                if(board[i][j]!='.')
                {
                    cnt++;
                }
            }
        }
        printf("Case #%d: ",c+1);
        if(check('X')==1)
        {
            printf("X won\n");
        }
        else if(check('O')==1)
        {
            printf("O won\n");
        }
        else if(cnt==16)
        {
            printf("Draw\n");
        }
        else
        {
            printf("Game has not completed\n");
        }
    }
    return 0;
}
