#include<cstdio>
#include<cstring>
#include<vector>
#include<queue>
#include<cmath>
#include<cctype>
#include<string>
#include<algorithm>
#include<iostream>
using namespace std;
typedef long long LL;
const int NN=100010;

char mat[4][5];

void FF(bool fg_o,bool fg_x,bool fg_kong)
{
    int i,j;
   /* printf("\n");
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
            printf("%c",mat[i][j]);
        printf("\n");
    }*/
    if(fg_o || fg_x)
    {
        if(fg_o)
            printf("O won\n");
        else
            printf("X won\n");
    }
    else
    {
        if(fg_kong)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int ncase,ee=0;
    int i,j;
    bool fgo,fgx,fg_kong;
    int num_o,num_x,num_t;
    scanf("%d",&ncase);
    while(ncase--)
    {
        fgo=false;
        fgx=false;
        fg_kong=false;
        for(i=0;i<4;i++)
        {
            scanf("%s",mat[i]);
            num_o=num_x=num_t=0;
            for(j=0;j<4;j++)
            {
                if(mat[i][j]=='X')
                    num_x++;
                else if(mat[i][j]=='O')
                    num_o++;
                else if(mat[i][j]=='T')
                    num_t++;
                else
                    fg_kong=true;
            }
            if(num_x>=3 && num_x+num_t==4)
                fgx=true;
            if(num_o>=3 && num_o+num_t==4)
                fgo=true;
        }


        for(j=0;j<4;j++)
        {
            num_o=num_x=num_t=0;
            for(i=0;i<4;i++)
            {
                if(mat[i][j]=='X')
                    num_x++;
                else if(mat[i][j]=='O')
                    num_o++;
                else if(mat[i][j]=='T')
                    num_t++;
            }
            if(num_x>=3 && num_x+num_t==4)
                fgx=true;
            if(num_o>=3 && num_o+num_t==4)
                fgo=true;
        }


        num_o=num_x=num_t=0;
        for(i=0,j=0;i<4;i++,j++)
        {
            if(mat[i][j]=='X')
                num_x++;
            else if(mat[i][j]=='O')
                num_o++;
            else if(mat[i][j]=='T')
                num_t++;
        }
        if(num_x>=3 && num_x+num_t==4)
            fgx=true;
        if(num_o>=3 && num_o+num_t==4)
            fgo=true;

        num_o=num_x=num_t=0;
        for(i=0,j=3;i<4;i++,j--)
        {
            if(mat[i][j]=='X')
                num_x++;
            else if(mat[i][j]=='O')
                num_o++;
            else if(mat[i][j]=='T')
                num_t++;
        }
        if(num_x>=3 && num_x+num_t==4)
            fgx=true;
        if(num_o>=3 && num_o+num_t==4)
            fgo=true;

        printf("Case #%d: ",++ee);
        FF(fgo,fgx,fg_kong);
    }
    return 0;
}
