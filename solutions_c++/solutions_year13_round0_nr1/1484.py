#include<stdio.h>
#include<iostream>
#include<vector>
#include<map>
#include<queue>
#include<limits.h>
#include<string.h>
#include<algorithm>
#include<stdlib.h>
typedef long long ll;
using namespace std;
char board[5][5];
int ndot;
int func()
{
    int nX,nO,i,j;
    for(i=0; i<4; i++)
    {
        nX=0;
        nO=0;
        for(j=0; j<4; j++)
        {
            if(board[i][j]=='X')nX++;
            else if(board[i][j]=='O')nO++;
            else if(board[i][j]=='T')
            {
                nX++;
                nO++;
            }
            else
                ndot++;
        }
        if(nX==4)return 1;
        if(nO==4)return 0;
    }
    for(j=0; j<4; j++)
    {
        nX=0;
        nO=0;
        for(i=0; i<4; i++)
        {
            if(board[i][j]=='X')nX++;
            else if(board[i][j]=='O')nO++;
            else if(board[i][j]=='T')
            {
                nX++;
                nO++;
            }
            else
                ndot++;
        }
        if(nX==4)return 1;
        if(nO==4)return 0;
    }
    nX=0;
    nO=0;
    for(i=0;i<4;i++)
    {
        if(board[i][i]=='X')nX++;
        else if(board[i][i]=='O')nO++;
        else if(board[i][i]=='T')
        {
            nX++;
            nO++;
        }
        else
        ndot++;
    }
    if(nX==4)return 1;
    if(nO==4)return 0;
    nX=0;
    nO=0;
    for(i=3;i>=0;i--)
    {
        if(board[i][3-i]=='X')nX++;
        else if(board[i][3-i]=='O')nO++;
        else if(board[i][3-i]=='T')
        {
            nX++;
            nO++;
        }
        else
        ndot++;
    }
    if(nX==4)return 1;
    if(nO==4)return 0;
    return -1;
}
int main()
{
    int t,i,j,ans,count=0;
//    freopen("A-large.in","r",stdin);
//    freopen("output1.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        count++;
        ndot=0;
        for(i=0; i<4; i++)
            scanf("%s",board[i]);
        ans=func();
        if(ans==1)printf("Case #%d: X won\n",count);
        else if(ans==0)printf("Case #%d: O won\n",count);
        else
        {
            if(ndot==0)printf("Case #%d: Draw\n",count);
            else
            printf("Case #%d: Game has not completed\n",count);
        }
    }
    return 0;
}
