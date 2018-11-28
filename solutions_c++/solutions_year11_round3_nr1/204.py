#include <cstring>
#include <cstdio>
#include <iostream>
using namespace std;

char grid[55][55];

int main()
{
    freopen("A-large.in", "rt", stdin);
    freopen("out.txt", "wt", stdout);
    int T, R, C;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        memset(grid, 0, sizeof(grid));
        cin>>R>>C;
        for (int i=0; i<R; ++i)
        {
            cin>>grid[i];
        }
        bool possible = 1;
        for (int i=0; i<R && possible; ++i)
        {
            for (int j=0; j<C && possible; ++j)
            {
                if (grid[i][j]=='#')
                {
                    if (grid[i+1][j]=='#' && grid[i][j+1]=='#'  && grid[i+1][j+1]=='#' )
                    {
                        grid[i][j]='/';
                        grid[i+1][j]='\\';
                        grid[i][j+1]='\\';
                        grid[i+1][j+1]='/';
                    }
                    else
                    {
                        possible = 0;
                    }
                }
            }
        }
        printf("Case #%d:\n", cas);
        if (!possible) printf("Impossible\n");
        else
        {
            for (int i=0; i<R; ++i) cout<<grid[i]<<endl;
        }
    }
    return 0;
}
