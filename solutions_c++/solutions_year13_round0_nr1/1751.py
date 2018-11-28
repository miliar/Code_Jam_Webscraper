#include<stdio.h>
#include<string>
#include<iostream>
using namespace std;
int main()
{
    //freopen("A-small-attempt0.in","r",stdin);
    //freopen("output.txt","w",stdout);
    int t,i,j,k;
    char c;
    string crap;
    scanf("%d",&t);
    getline(cin,crap);
    for(k=1;k<=t;++k)
    {
        int xwon=0,owon=0,dotleft=0;
        char b[4][4];
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                c=getchar();
                b[i][j]=c;
                if(c=='.')
                    dotleft=1;
            }
            c=getchar();
        }
        c=getchar();
        for(i=0;i<4;i++)
        {
            if((b[i][0]=='X' || b[i][0]=='T') && (b[i][1]=='X'|| b[i][1]=='T') && (b[i][2]=='X' || b[i][2]=='T') && (b[i][3]=='X'|| b[i][3]=='T'))
                {
                    xwon=1;
                    break;
                }
            if((b[i][0]=='O' || b[i][0]=='T') && (b[i][1]=='O'|| b[i][1]=='T') && (b[i][2]=='O' || b[i][2]=='T') && (b[i][3]=='O'|| b[i][3]=='T'))
                {
                    owon=1;
                    break;
                }
        }
        for(j=0;j<4;j++)
        {
            if((b[0][j]=='X' || b[0][j]=='T') && (b[1][j]=='X'|| b[1][j]=='T') && (b[2][j]=='X' || b[2][j]=='T') && (b[3][j]=='X'|| b[3][j]=='T'))
                {
                    xwon=1;
                    break;
                }
            if((b[0][j]=='O' || b[0][j]=='T') && (b[1][j]=='O'|| b[1][j]=='T') && (b[2][j]=='O' || b[2][j]=='T') && (b[3][j]=='O'|| b[3][j]=='T'))
                {
                    owon=1;
                    break;
                }
        }
        if((b[0][0]=='X' || b[0][0]=='T') && (b[1][1]=='X' || b[1][1]=='T') && (b[2][2]=='X' || b[2][2]=='T') && (b[3][3]=='X' || b[3][3]=='T'))
            xwon=1;
        else if((b[0][0]=='O' || b[0][0]=='T') && (b[1][1]=='O' || b[1][1]=='T') && (b[2][2]=='O' || b[2][2]=='T') && (b[3][3]=='O' || b[3][3]=='T'))
            owon=1;
        else if((b[3][0]=='X' || b[3][0]=='T') && (b[2][1]=='X' || b[2][1]=='T') && (b[1][2]=='X' || b[1][2]=='T') && (b[0][3]=='X' || b[0][3]=='T'))
            xwon=1;
        else if((b[3][0]=='O' || b[3][0]=='T') && (b[2][1]=='O' || b[2][1]=='T') && (b[1][2]=='O' || b[1][2]=='T') && (b[0][3]=='O' || b[0][3]=='T'))
            owon=1;
        if(xwon)
             printf("Case #%d: X won\n",k);
        else if(owon)
             printf("Case #%d: O won\n",k);
        else if(!dotleft && !xwon && !owon)
            printf("Case #%d: Draw\n",k);
        else if(dotleft && !xwon && !owon)
            printf("Case #%d: Game has not completed\n",k);
    }
    return 0;
}
