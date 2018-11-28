
#include<stdio.h>

char array[5][5];
int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("sum.out","w",stdout);
    int n,i,j,count=0;
    scanf("%d",&n);
    while(n--)
    {
        int sign=0;
        ++count;
        for(i=1; i<=4; i++)
            scanf("%s",array[i]+1);
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
                if(array[i][j]=='.'||array[i][j]=='X')
                    break;
                else if(j==4&&(array[i][j]=='O'||array[i][j]=='T'))
                    sign=1;
            if(sign==1)
                break;
        }
        if(!sign)
            for(i=1; i<=4; i++)
            {
                for(j=1; j<=4; j++)
                    if(array[j][i]=='.'||array[j][i]=='X')
                        break;
                    else if(j==4&&(array[j][i]=='O'||array[j][i]=='T'))
                        sign=1;
                if(sign==1)
                    break;
            }
        if(!sign)
        {
            for(i=1; i<=4; i++)
                if(i==4&&(array[i][i]=='O'||array[i][i]=='T'))
                    sign=1;
                else if(array[i][i]=='.'||array[i][i]=='X')
                    break;
        }
        if(!sign)
        {
            for(i=1; i<=4; i++)
                if(i==4&&(array[i][4-i+1]=='O'||array[i][4-i+1]=='T'))
                    sign=1;
                else if(array[i][4-i+1]=='.'||array[i][4-i+1]=='X')
                    break;
        }
        if(!sign)
            for(i=1; i<=4; i++)
            {
                for(j=1; j<=4; j++)
                    if(array[i][j]=='.'||array[i][j]=='O')
                        break;
                    else if(j==4&&(array[i][j]=='X'||array[i][j]=='T'))
                        sign=2;
                if(sign==2)
                    break;
            }
        if(!sign)
            for(i=1; i<=4; i++)
            {
                for(j=1; j<=4; j++)
                    if(array[j][i]=='.'||array[j][i]=='O')
                        break;
                    else if(j==4&&(array[j][i]=='X'||array[j][i]=='T'))
                        sign=2;
                if(sign==2)
                    break;
            }
        if(!sign)
        {
            for(i=1; i<=4; i++)
                if(i==4&&(array[i][i]=='X'||array[i][i]=='T'))
                    sign=2;
                else if(array[i][i]=='.'||array[i][i]=='O')
                    break;
        }
        if(!sign)
        {
            for(i=1; i<=4; i++)
                if(i==4&&(array[i][4-i+1]='X'||array[i][4-i+1]=='T'))
                    sign=2;
                else if(array[i][4-i+1]=='.'||array[i][4-i+1]=='O')
                    break;
        }
        if(!sign)
        {
            for(i=1; i<=4; i++)
            {
                for(j=1; j<=4; j++)
                    if(array[i][j]=='.')
                        break;
                if(array[i][j]=='.')
                    break;
            }
            if(i==5)
                sign=3;
        }
        if(sign==1)
            printf("Case #%d: O won\n",count);
        else if(sign==2)
            printf("Case #%d: X won\n",count);
        else if(sign==3)
            printf("Case #%d: Draw\n",count);
        else
            printf("Case #%d: Game has not completed\n",count);
    }
    return 0;
}
