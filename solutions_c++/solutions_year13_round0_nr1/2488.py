#include <iostream>
#include <fstream>
using namespace std;
typedef long long lld;
char board[5][5];
int main ()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    lld i,j,ii,t;
    char sym,h;
    bool success=false,full;
    scanf("%lld",&t);
    for (i=1;i<=t;i++)
    {
        full=true;
        for (j=1;j<=4;j++)
        {
            for (ii=1;ii<=4;ii++)
            {
                scanf("%c",&h);
                if (h==(char)10)
                {
                    ii--;
                    continue;
                }
                board[j][ii]=h;
                if (h=='.') full=false;
            }
        }
        for (j=1;j<=4;j++)
        {
            for (ii=1;ii<=4;ii++)
            {
                sym=board[j][ii];
                if (sym!='T'&&sym!='.') break;
            }
            if (sym=='.'||sym=='T')
            {
                success=false;
                break;
            }
            success=true;
            for (ii=1;ii<=4;ii++)
            {
                if (board[j][ii]=='.')
                {
                    success=false;
                    break;
                }
                if (board[j][ii]==sym||board[j][ii]=='T') continue;
                success = false;
                break;
            }
            if (success)
            {
                printf("Case #%lld: %c won\n",i,sym);
                break;
            }
        }
        if (success) continue;
        for (ii=1;ii<=4;ii++)
        {
            for (j=1;j<=4;j++)
            {
                sym=board[j][ii];
                if (sym!='T'&&sym!='.') break;
            }
            if (sym=='.'||sym=='T')
            {
                success=false;
                break;
            }
            success=true;
            for (j=1;j<=4;j++)
            {
                if (board[j][ii]=='.')
                {
                    success=false;
                    break;
                }
                if (board[j][ii]==sym||board[j][ii]=='T') continue;
                success = false;
                break;
            }
            if (success)
            {
                printf("Case #%lld: %c won\n",i,sym);
                break;
            }
        }
        if (success) continue;
        success=true;
        sym=board[1][1];
        if (sym=='T') sym=board[2][2];
        for (ii=1;ii<=4;ii++)
        {
            if (board[ii][ii]=='.'||(board[ii][ii]!='T'&&board[ii][ii]!=sym))
            {
                success=false;
                break;
            }
        }
        if (success)
        {
            printf("Case #%lld: %c won\n",i,sym);
            continue;
        }

        success=true;
        sym=board[1][4];
        if (sym=='T') sym=board[2][3];
        for (ii=1;ii<=4;ii++)
        {
            if (board[ii][4-ii+1]=='.'||(board[ii][4-ii+1]!='T'&&board[ii][4-ii+1]!=sym))
            {
                success=false;
                break;
            }
        }
        if (success)
            {
                printf("Case #%lld: %c won\n",i,sym);
                continue;
            }

        if (full)
            printf("Case #%lld: Draw\n",i);
        else
            printf("Case #%lld: Game has not completed\n",i);
    }
}
