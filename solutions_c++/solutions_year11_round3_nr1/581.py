#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <stack>
#include <string>
#include <map>
using namespace std;
char mp[100][100];
int vst[100][100];
int n,m;

bool solve(int x,int y)
{
    if(x+1<n&&y+1<m&&mp[x][y]=='#'&&mp[x+1][y+1]=='#'&&mp[x+1][y]=='#'&&mp[x][y+1]=='#')
    {
        mp[x][y]='/';
        mp[x+1][y+1]='/';
        mp[x+1][y]=mp[x][y+1]='\\';
        vst[x][y]=vst[x+1][y]=vst[x][y+1]=vst[x+1][y+1]=1;
        return true;
    }
    return false;


}

int main()
{
    int t,cas;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);
    cas=0;
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
          scanf("%s",mp[i]);
        bool flag=true;
        memset(vst,0,sizeof(vst));
        for(int i=0;i<n&&flag;i++)
          for(int j=0;j<m&&flag;j++)
          {
              if(mp[i][j]=='#'&&!vst[i][j])
              {
                  bool re=solve(i,j);
                  if(!re)
                    {

                        flag=false;
                    }
              }
         }
        printf("Case #%d:\n",++cas);
        if(!flag)
          printf("Impossible\n");
        else
         {
             for(int i=0;i<n;i++)
               printf("%s\n",mp[i]);
         }

    }

}
