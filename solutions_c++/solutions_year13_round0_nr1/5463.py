#include<stdio.h>
char input[5][5];
bool down_check(int j,int k)
{
    return ((j+1)<4 && (j+2)<4 && (j+3)<4);
}
bool lower_diagonal_check(int j,int k)
{
    return ((j+1)<4 && (j+2)<4 && (j+3)<4 && (k+1)<4 && (k+2)<4 && (k+3)<4);
}
bool right_check(int j,int k)
{
    return ((k+1)<4 && (k+2)<4 && (k+3)<4);
}
bool upper_diagonal_check(int j,int k)
{
    return ((j-1)>=0 && (j-2)>=0 && (j-3)>=0 && (k+1)<4 && (k+2)<4 && (k+3)<4);
}
int main()
{
    int test_cases;
    bool game_not_ended_possible;
    bool game_draw,x_win,o_win;
    char symbol;
    scanf("%d",&test_cases);
    for(int i=0;i<test_cases;i++)
    {
        game_not_ended_possible=game_draw=x_win=o_win=false;
        for(int j=0;j<4;j++)
        {
            scanf("%s",input[j]);
            //printf("Line:%s\n",input[j]);
            for(int k=0;k<4;k++)
            {
                if(input[j][k]=='.')
                {
                    game_not_ended_possible=true;
                }
            }
        }
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(input[j][k]=='T')
                {
                    //printf("<2>\n");
                    if(down_check(j,k))
                    {
                        if(input[j+1][k]=='X' && input[j+2][k]=='X' && input[j+3][k]=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(input[j+1][k]=='O' && input[j+2][k]=='O' && input[j+3][k]=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(lower_diagonal_check(j,k))
                    {
                        if(input[j+1][k+1]=='X' && input[j+2][k+2]=='X' && input[j+3][k+3]=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(input[j+1][k+1]=='O' && input[j+2][k+2]=='O' && input[j+3][k+3]=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(upper_diagonal_check(j,k))
                    {
                        //printf("<1>\n");
                        if(input[j-1][k+1]=='X' && input[j-2][k+2]=='X' && input[j-3][k+3]=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(input[j-1][k+1]=='O' && input[j-2][k+2]=='O' && input[j-3][k+3]=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(right_check(j,k))
                    {
                        if(input[j][k+1]=='X' && input[j][k+2]=='X' && input[j][k+3]=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(input[j][k+1]=='O' && input[j][k+2]=='O' && input[j][k+3]=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    continue;
                }
                if(down_check(j,k))
                {
                    symbol=input[j][k];
                    if(input[j+1][k]==symbol && input[j+2][k]==symbol && input[j+3][k]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j+1][k]=='T' && input[j+2][k]==symbol && input[j+3][k]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j+1][k]==symbol && input[j+2][k]=='T' && input[j+3][k]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j+1][k]==symbol && input[j+2][k]==symbol && input[j+3][k]=='T')
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                }
                if(right_check(j,k))
                {
                    symbol=input[j][k];
                    if(input[j][k+1]==symbol && input[j][k+2]==symbol && input[j][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j][k+1]=='T' && input[j][k+2]==symbol && input[j][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j][k+1]==symbol && input[j][k+2]=='T' && input[j][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j][k+1]==symbol && input[j][k+2]==symbol && input[j][k+3]=='T')
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                }
                if(lower_diagonal_check(j,k))
                {
                    symbol=input[j][k];
                    if(input[j+1][k+1]==symbol && input[j+2][k+2]==symbol && input[j+3][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j+1][k+1]=='T' && input[j+2][k+2]==symbol && input[j+3][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j+1][k+1]==symbol && input[j+2][k+2]=='T' && input[j+3][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j+1][k+1]==symbol && input[j+2][k+2]==symbol && input[j+3][k+3]=='T')
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                }
                if(upper_diagonal_check(j,k))
                {
                    symbol=input[j][k];
                    if(input[j-1][k+1]==symbol && input[j-2][k+2]==symbol && input[j-3][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j-1][k+1]=='T' && input[j-2][k+2]==symbol && input[j-3][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j-1][k+1]==symbol && input[j-2][k+2]=='T' && input[j-3][k+3]==symbol)
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                    else if(input[j-1][k+1]==symbol && input[j-2][k+2]==symbol && input[j-3][k+3]=='T')
                    {
                        if(symbol=='X')
                        {
                            x_win=true;
                            break;
                        }
                        else if(symbol=='O')
                        {
                            o_win=true;
                            break;
                        }
                    }
                }
            }
            if(x_win || o_win)
                break;
        }
        if(x_win)
        {
            printf("Case #%d: X won\n",i+1);
        }
        else if(o_win)
        {
            printf("Case #%d: O won\n",i+1);
        }
        else
        {
            if(game_not_ended_possible)
            {
                printf("Case #%d: Game has not completed\n",i+1);
            }
            else
            {
                printf("Case #%d: Draw\n",i+1);
            }
        }
    }
}
