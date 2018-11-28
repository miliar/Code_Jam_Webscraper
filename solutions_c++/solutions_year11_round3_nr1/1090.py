#include<cstdio>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<map>
#include<iostream>
#include<cstdlib>
#include<queue>
#include<sstream>
#include<queue>
#include<ctype.h>

using namespace std;

#define re return
#define co continue
#define pb push_back
#define br break
#define sz size


#define pf printf
#define sf scanf

int main()
{

    //freopen("sample.in","r",stdin);
    freopen("a.in","r",stdin);
    freopen("a.ans","w",stdout);


    int t;
    sf("%d",&t);
    int kase=1;
    char grid[51][51];
    while (t--)
    {
        int r,c;
        sf("%d %d",&r,&c);
        int i,j;
        for(i=0;i<r;i++)
            sf("%s",grid[i]);
        bool doable =  true;
        for(i=0;i<=r-2;i++)
            for(j=0;j<=c-2;j++)
                if ( grid[i][j] == '#')
                {
                    // replace
                    if ( grid[i][j] == '#' && grid[i][j+1] == '#' && grid[i+1][j] == '#' && grid[i+1][j+1] == '#' )
                    {
                        grid[i][j] = '/';
                        grid[i][j+1] = '\\';
                        grid[i+1][j] = '\\';
                        grid[i+1][j+1] = '/' ;
                    }


                }
        for(i=0;i<r;i++)
            for(j=0;j<c;j++)
                if ( grid[i][j] == '#')
                    doable = false;
        pf("Case #%d:\n",kase++);
        if ( doable )
        {
            for(i=0;i<r;i++)
                pf("%s\n",grid[i]);
        }
        else
        {
            pf("Impossible\n");
        }

    }
    return 0;
}
