#include<stdio.h>
#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#include<set>
#include<map>
#include<utility>
#include<vector>
#include<string>
#include<stack>
#include<queue>
using namespace std;
char board[4][5];
int main()
{
    freopen("inputAlarge.in", "r", stdin);
    freopen("Bout.txt", "w", stdout);
    int t,T,i,j;
    bool f,fx,fo;
    scanf("%d", &T);
    for (t=1; t<=T; ++t)
    {
        for (i=0; i<4; ++i) scanf("%s", board[i]);
        fx = fo = false;
        for (i=0; i<4; ++i)
        {
            for (j=0; j<4; ++j)
            {
                if (board[i][j]=='O' || board[i][j]=='.') break;
            }
            if (j==4) fx = true;
            for (j=0; j<4; ++j)
            {
                if (board[i][j]=='X' || board[i][j]=='.') break;
            }
            if (j==4) fo = true;
            for (j=0; j<4; ++j)
            {
                if (board[j][i]=='O' || board[j][i]=='.') break;
            }
            if (j==4) fx = true;
            for (j=0; j<4; ++j)
            {
                if (board[j][i]=='X' || board[j][i]=='.') break;
            }
            if (j==4) fo = true;
        }
        for (i=0; i<4; ++i)
        {
            if (board[i][i]=='O' || board[i][i]=='.') break;
        }
        if (i==4) fx = true;
        for (i=0; i<4; ++i)
        {
            if (board[i][i]=='X' || board[i][i]=='.') break;
        }
        if (i==4) fo = true;
        for (i=0; i<4; ++i)
        {
            if (board[i][3-i]=='O' || board[i][3-i]=='.') break;
        }
        if (i==4) fx = true;
        for (i=0; i<4; ++i)
        {
            if (board[i][3-i]=='X' || board[i][3-i]=='.') break;
        }
        if (i==4) fo = true;

        /*if (fx && fo) puts("ki je holo!");
        else*/ if (fx) printf("Case #%d: X won\n",t);
        else if (fo) printf("Case #%d: O won\n",t);
        else
        {
            f = true;
            for (i=0; i<4 && f; ++i)
            {
                for (j=0; j<4 && f; ++j)
                {
                    if (board[i][j]=='.') f = false;
                }
            }
            if (!f) printf("Case #%d: Game has not completed\n",t);
            else printf("Case #%d: Draw\n",t);
        }
    }
    return 0;
}
