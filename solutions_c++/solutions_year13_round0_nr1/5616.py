#include <stdio.h>
#include <iostream>
#include <stack>
#include <vector>
#include <string>
#include <math.h>
#include <limits>
#include <algorithm>

using namespace std;

char won(vector<string> &grid, bool &haveDot)
{
    for (int i=0; i<grid.size(); i++)
    {
        char ch=grid[i][0];
        if (ch=='T') ch=grid[i][0];
        int j;
        for (j=0; j<grid[i].size(); j++)
        {
            if (grid[i][j]=='.') haveDot=true;
            if (grid[i][j]=='.') break;
            if (grid[i][j]!=ch && grid[i][j]!='T') break;
        }
        if (j==grid[i].size()) return ch;
    }

    for (int j=0; j<grid[0].size(); j++)
    {
        char ch=grid[0][j];
        if (ch=='T') ch=grid[1][j];
        int i;
        for (i=0; i<grid.size(); i++)
        {
            if (grid[i][j]=='.') break;
            if (grid[i][j]!=ch && grid[i][j]!='T') break;
        }
        if (i==grid.size()) return ch;
    }

    char ch=grid[0][0];
    if (ch=='T') ch=grid[1][1];
    int i,j;
    for (i=0; i<grid.size(); i++)
    {
        if (grid[i][i]=='.') break;
        if (grid[i][i]!=ch && grid[i][i]!='T') break;
    }
    if (i==grid.size()) return ch;

    ch=grid[0][3];
    if (ch=='T') ch=grid[1][2];
    for (i=0,j=3; i<grid.size(); i++,j--)
    {
        if (grid[i][j]=='.') break;
        if (grid[i][j]!=ch && grid[i][j]!='T') break;
    }
    if (i==grid.size()) return ch;
    return 'N';
}

int main()
{
    freopen("asmall.in","r",stdin);
    freopen("asmall.out","w",stdout);
    int T,cas;
    cin>>T;
    char ch;
    for (cas=1; cas<=T; cas++)
    {
        vector<string> grid(4);
        for (int i=0; i<4; i++) cin>>grid[i];
        bool haveDot=false;
        if ((ch=won(grid,haveDot))=='N')
        {
            if (haveDot) printf("Case #%d: Game has not completed\n",cas);
            else printf("Case #%d: Draw\n",cas);
        }
        else
        {
            printf("Case #%d: %c won\n",cas,ch);
        }
    }
    return 0;
}
