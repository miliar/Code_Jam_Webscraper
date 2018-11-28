#include <cstdio>
#include <memory>
using namespace std;

int mp[150][150];
int color[150][150];
int st = 1;
int x,y,xs,ys,t;

int mp1(int x,int y)
{
    if(x < 0 || y<0 || x>=xs || y>= ys) return 0;
    return 1;    
}

int go(int x,int y)
{
    if(mp1(x,y) && color[x][y] != 0)
    {
        return color[x][y];
    }

    int m = 100000000;
    if(mp1(x+1,y) && m > mp[x+1][y]) m = mp[x+1][y];
    if(mp1(x-1,y) && m > mp[x-1][y]) m = mp[x-1][y];
    if(mp1(x,y+1) && m > mp[x][y+1]) m = mp[x][y+1];
    if(mp1(x,y-1) && m > mp[x][y-1]) m = mp[x][y-1];
    
    if(mp1(x,y-1) &&  mp[x][y-1] < mp[x][y] && mp[x][y-1] == m)
    {
        return color[x][y] = go(x,y-1);
    }
    if(mp1(x-1,y) &&  mp[x-1][y] < mp[x][y] && mp[x-1][y] == m)
    {
        return color[x][y] = go(x-1,y);
    }
    if(mp1(x+1,y) &&  mp[x+1][y] < mp[x][y] && mp[x+1][y] == m)
    {
        return color[x][y] = go(x+1,y);
    }
    if(mp1(x,y+1) &&  mp[x][y+1] < mp[x][y] && mp[x][y+1] == m)
    {
        return color[x][y] = go(x,y+1);
    }

    color[x][y] = st++;
    return color[x][y];
}


int main()
{

    scanf("%d",&t);
    for(int ti = 0;ti<t;ti++)
    {
        scanf("%d%d",&ys,&xs);
        memset(mp,0,sizeof(mp));
        memset(color,0,sizeof(color));
        st = 1;

        for(y=0;y<ys;y++)
            for(x = 0;x<xs;x++)
                scanf("%d",&mp[x][y]);

        for(y=0;y<ys;y++)
            for(x = 0;x<xs;x++)
                if(color[x][y] == 0)
                    go(x,y);
        
        int let[40];
        memset(let,0,sizeof(let));
        char l = 1;

/*        for(y=0;y<ys;y++)
        {
            for(x = 0;x<xs;x++)
            printf("%2d ",color[x][y]);
            puts("");
        }


/*/        
        for(y=0;y<ys;y++)
        {
            for(x = 0;x<xs;x++)
            {
                if(let[color[x][y]] == 0)
                {
                    let[color[x][y]] = l++;
                }
            }
//                printf("%2d ",color[x][y]);
//            puts("");
        }
        printf("Case #%d:\n",ti+1);
        for(y=0;y<ys;y++)
        {
            for(x = 0;x<xs;x++)
            {
                
                printf("%c ",color[x][y] + 'a'-1);

            }
            puts("");
        }/**/
    }
    return 0;
}