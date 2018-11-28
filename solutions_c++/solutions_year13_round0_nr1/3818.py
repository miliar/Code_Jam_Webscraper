#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#include<limits.h>

int readint()
{
    int t=0;
    char c;
    c=getchar();
    while(c<'0' || c>'9')
        c=getchar();
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    return t;
}

int main()
{
    int t=readint();
    char arr[10][10];
    int cnt,i,j,flag1,flag2,s;
    for(s=1; s<=t; s++)
    {
        cnt=flag1=flag2=0;
        printf("Case #%d: ",s);
        for(i=1; i<=4; i++)
            {scanf("%s",&arr[i][1]);
            //printf("%s\n",&arr[i][1]);
            }
        getchar();
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                if(arr[i][j]=='O' || arr[i][j]=='T')
                {
                    if(j<=1 && (arr[i][j+1]=='O' || arr[i][j+1]=='T') && (arr[i][j+2]=='O' || arr[i][j+2]=='T') && (arr[i][j+3]=='O' || arr[i][j+3]=='T'))
                    {
                        flag1=1;
                        break;
                    }
                    else if(i<=1 && (arr[i+1][j]=='O' || arr[i+1][j]=='T') && (arr[i+2][j]=='O' || arr[i+2][j]=='T') && (arr[i+3][j]=='O' || arr[i+3][j]=='T'))
                    {
                        flag1=1;
                        break;
                    }
                    else if(i<=1 && j<=1 && (arr[i+1][j+1]=='O' || arr[i+1][j+1]=='T') && (arr[i+2][j+2]=='O' || arr[i+2][j+2]=='T') && (arr[i+3][j+3]=='O' || arr[i+3][j+3]=='T'))
                    {
                        flag1=1;
                        break;
                    }
                    else if(i>=4 && j<=1 && (arr[i-1][j+1]=='O' || arr[i-1][j+1]=='T') && (arr[i-2][j+2]=='O' || arr[i-2][j+2]=='T') && (arr[i-3][j+3]=='O' || arr[i-3][j+3]=='T'))
                    {
                        flag1=1;
                        break;
                    }

                }
                if(arr[i][j]=='.')
                        cnt++;
            }
            if(flag1==1)
                break;

        }
        for(i=1; i<=4; i++)
        {
            for(j=1; j<=4; j++)
            {
                if(arr[i][j]=='X' || arr[i][j]=='T')
                {
                    if(j<=1 && (arr[i][j+1]=='X' || arr[i][j+1]=='T') && (arr[i][j+2]=='X' || arr[i][j+2]=='T') && (arr[i][j+3]=='X' || arr[i][j+3]=='T'))
                    {
                        flag2=1;
                        break;
                    }
                    else if(i<=1 && (arr[i+1][j]=='X' || arr[i+1][j]=='T') && (arr[i+2][j]=='X' || arr[i+2][j]=='T') && (arr[i+3][j]=='X' || arr[i+3][j]=='T'))
                    {
                        flag2=1;
                        break;
                    }
                    else if(i<=1 && j<=1 && (arr[i+1][j+1]=='X' || arr[i+1][j+1]=='T') && (arr[i+2][j+2]=='X' || arr[i+2][j+2]=='T') && (arr[i+3][j+3]=='X' || arr[i+3][j+3]=='T'))
                    {
                        flag2=1;
                        break;
                    }
                    else if(i>=4 && j<=1 && (arr[i-1][j+1]=='X' || arr[i-1][j+1]=='T') && (arr[i-2][j+2]=='X' || arr[i-2][j+2]=='T') && (arr[i-3][j+3]=='X' || arr[i-3][j+3]=='T'))
                    {
                        flag2=1;
                        break;
                    }

                }

            }
            if(flag2==1)
                break;
        }
        if(flag1==1 && flag2==0)
        {
            printf("O won\n");
            continue;
        }
        else if(flag1==0 && flag2==1)
        {
            printf("X won\n");
            continue;
        }
        else if(cnt!=0 && flag2==0 && flag1==0)
        {
            printf("Game has not completed\n");
            continue;
        }
        else{
            printf("Draw\n");
            continue;
        }
    }
    return 0;
}

