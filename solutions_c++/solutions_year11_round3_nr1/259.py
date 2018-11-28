#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define maxn 100
int T,r,c;
char mp[maxn][maxn];
bool check(int x,int y)
{
    if(x>=0&&x<r&&y>=0&&y<c&&mp[x][y] == '#')
        return true;
    else
        return false;
}
int turn(int x,int y)
{
    if(check(x,y))
        mp[x][y] = '/';
    else
        return 1;
    if(check(x+1,y))
        mp[x+1][y] = '\\';
    else
        return 1;
    if(check(x,y+1))
        mp[x][y+1] = '\\';
    else
        return 1;
    if(check(x+1,y+1))
        mp[x+1][y+1] = '/';
    else
        return 1;
    return 0;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    char ch;
    int cs,check,i,j;
    while(scanf("%d",&T)!=EOF)
    {
        cs = 1;
        while(T--)
        {
            scanf("%d%d",&r,&c);
            scanf("%c",&ch);
            for(i = 0; i < r ; i++)
            {
                scanf("%s",mp[i]);
            }
            check = 0;
            for(i = 0; i < r ; i++)
            {
                for(j = 0; j < c ; j++)
                {
                    if(mp[i][j] == '#')
                    {
                        check = turn(i,j);
                    }
                    if(check)
                        break;
                }
                if(check)
                    break;
            }
            printf("Case #%d:\n",cs++);
            if(check)
                printf("Impossible\n");
            else
            {
                for(i = 0; i < r;i++)
                {
                    printf("%s\n",mp[i]);
                }
            }
        }
    }
    return 0;
}
