#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;


char g[5][5];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        int  p=3;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++)
            {
                scanf(" %c",&g[i][j]);
                if (g[i][j]=='.') p=0;
            }
        for (int i=0;i<4;i++)
        {
            int x1=0,x2=0;
            for (int j=0;j<4;j++)
            {
                if (g[i][j]=='X') x1++;
                if (g[i][j]=='O') x2++;
                if (g[i][j]=='T') {x1++;x2++;}
            }
            if (x1>3) p=1;
            if (x2>3) p=2;
        }
        for (int j=0;j<4;j++)
        {
            int x1=0,x2=0;
            for (int i=0;i<4;i++)
            {
                if (g[i][j]=='X') x1++;
                if (g[i][j]=='O') x2++;
                if (g[i][j]=='T') {x1++;x2++;}
            }
            if (x1>3) p=1;
            if (x2>3) p=2;
        }
        int x1=0,x2=0;
        for (int i=0;i<4;i++)
        {
            if (g[i][i]=='X') x1++;
            if (g[i][i]=='O') x2++;
            if (g[i][i]=='T') {x1++;x2++;}
        }
        if (x1>3) p=1;
        if (x2>3) p=2;
        x1=0;x2=0;
        for (int i=0;i<4;i++)
        {
            if (g[i][3-i]=='X') x1++;
            if (g[i][3-i]=='O') x2++;
            if (g[i][3-i]=='T') {x1++;x2++;}
        }
        if (x1>3) p=1;
        if (x2>3) p=2;
        if (p==0)
        printf("Case #%d: Game has not completed\n",cas);
        if (p==1)
        printf("Case #%d: X won\n",cas);
        if (p==2)
        printf("Case #%d: O won\n",cas);
        if (p==3)
        printf("Case #%d: Draw\n",cas);


    }

}
