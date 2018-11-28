#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;
int n,m;
    char map[55][55];
    int cases = 1;
int dir[4][2] = {{0,0},{1,0},{0,1},{1,1}};
bool solve()
{
    int i,j,k;
    int temx,temy;
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(map[i][j]=='#')
            {
                for(k=0;k<4;k++)
                {
                    temx = i+dir[k][0];
                    temy = j+dir[k][1];
                    if(temx<n && temy <m && map[temx][temy]=='#')
                    {
                        if(k==0) map[temx][temy] = '/';
                        if(k==1) map[temx][temy] = '\\';
                        if(k==2) map[temx][temy] = '\\';
                        if(k==3) map[temx][temy] = '/';
                    }
                    else return false;
                }
            }
        }
    }
    return true;
}
int main()
{
//    freopen("A-large.in","r",stdin);
//    freopen("A-large.out","w",stdout);
    int t;
    int i,j;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            scanf("%s",map[i]);
        }
        printf("Case #%d:\n",cases++);
        if(!solve())
            printf("Impossible\n");
        else
        {
            for(i=0;i<n;i++)
            {
                for(j=0;j<m;j++)
                {
                    printf("%c",map[i][j]);
                }
                printf("\n");
            }
        }
    }
    return 0;
}
