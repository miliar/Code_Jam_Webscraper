#include <iostream>
#include <cstdio>

int cases, xs, ys, i;
char board[7][7], inp[7];
void kitten ()
{
    for(int g=1; g<=4; g++)
    {
        scanf("%s", inp);
        for(int j=1; j<=4; j++)
        {
            board[j][g]=inp[j-1];
        }
    }
    for(int g=1; g<=4; g++)
    {
        xs=0;
        for(int j=1; j<=4; j++)
        {
            if(board[j][g]=='X' || board[j][g]=='T')
            {
                xs++;
            }
        }
        if(xs==4)
        {
            printf("Case #%d: X won\n", i);
            return;
        }
    }
    for(int g=1; g<=4; g++)
    {
        xs=0;
        for(int j=1; j<=4; j++)
        {
            if(board[g][j]=='X' || board[g][j]=='T')
            {
                xs++;
            }
        }
        if(xs==4)
        {
            printf("Case #%d: X won\n", i);
            return;
        }
    }
    xs=0;
    for(int g=1; g<=4; g++)
    {
        if(board[g][g]=='X' || board[g][g]=='T')
        {
            xs++;
        }
    }
    if(xs==4)
    {
        printf("Case #%d: X won\n", i);
        return;
    }
    xs=0;
    for(int g=1, j=4; g<=4; g++, j--)
    {
        if(board[j][g]=='X' || board[j][g]=='T')
        {
            xs++;
        }
    }
    if(xs==4)
    {
        printf("Case #%d: X won\n", i);
        return;
    }
    for(int g=1; g<=4; g++)
    {
        xs=0;
        for(int j=1; j<=4; j++)
        {
            if(board[j][g]=='O' || board[j][g]=='T')
            {
                xs++;
            }
        }
        if(xs==4)
        {
            printf("Case #%d: O won\n", i);
            return;
        }
    }
    for(int g=1; g<=4; g++)
    {
        xs=0;
        for(int j=1; j<=4; j++)
        {
            if(board[g][j]=='O' || board[g][j]=='T')
            {
                xs++;
            }
        }
        if(xs==4)
        {
            printf("Case #%d: O won\n", i);
            return;
        }
    }
    xs=0;
    for(int g=1; g<=4; g++)
    {
        if(board[g][g]=='O' || board[g][g]=='T')
        {
            xs++;
        }
    }
    if(xs==4)
    {
        printf("Case #%d: O won\n", i);
        return;
    }
    xs=0;
    for(int g=1, j=4; g<=4; g++, j--)
    {
        if(board[j][g]=='O' || board[j][g]=='T')
        {
            xs++;
        }
    }
    if(xs==4)
    {
        printf("Case #%d: O won\n", i);
        return;
    }
    for(int g=1; g<=4; g++)
    {
        for(int j=1; j<=4; j++)
        {
            if(board[j][g]=='.')
            {
                printf("Case #%d: Game has not completed\n", i);
                return;
            }
        }
    }
    printf("Case #%d: Draw\n", i);
}
int main()
{
    scanf("%d", &cases);
    for(i=1; i<=cases; i++)
    {
        kitten();
    }
    return 0;
}

