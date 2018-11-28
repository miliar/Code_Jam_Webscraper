#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

char line[64];
char map[64][64];
int tt,n,m;

bool can()
{
    bool flag=true;
    while (flag)
    {
        flag=false;
        int x=0,y=0;
        for (int i=1; i<=n && !flag; i++)
            for (int j=1; j<=m; j++)
                if (map[i][j]=='#')
                {
                    x=i;
                    y=j;
                    flag=true;
                    break;
                }
        if (flag)
        {
            if (x<n && y<m && map[x+1][y]=='#' && map[x][y+1]=='#' && map[x+1][y+1]=='#')
            {
                map[x][y]='/';
                map[x][y+1]='\\';
                map[x+1][y]='\\';
                map[x+1][y+1]='/';
            }
            else
                return false;
        }
    }
    return true;
}

int main()
{
    freopen("square.in","r",stdin);
    freopen("square.out","w",stdout);
    gets(line);
    sscanf(line,"%d",&tt);
    for (int ii=1; ii<=tt; ii++)
    {
        gets(line);
        sscanf(line,"%d%d",&n,&m);
        memset(map,'.',sizeof(map));
        for (int i=1; i<=n; i++)
            gets(map[i]+1);
        printf("Case #%d:\n",ii);
        if (!can())
        {
            printf("Impossible\n");
        }
        else
        {
            for (int i=1; i<=n; i++)
            {
                for (int j=1; j<=m; j++)
                    putchar(map[i][j]);
                putchar('\n');
            }
        }
    }
    return 0;
}
