#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

const int MAXN=55;

int n,m;
char str[MAXN][MAXN];
bool flag;

bool check(int x,int y)
{
    if(x>=0&&x<n&&y>=0&&y<m&&str[x][y]=='#')return true;
    return false;
}

void solve()
{
    for(int i=0; i<n; ++i)
        for(int j=0; j<m; ++j)
        {
            if(str[i][j]=='#')
            {
                if(check(i+1,j)&&check(i,j+1)&&check(i+1,j+1))
                {
                    str[i][j]='/',str[i][j+1]='\\',str[i+1][j]='\\',str[1+i][j+1]='/';
                }
                else
                {
                    flag=true;
                    return ;
                }
            }
        }
}

int main()
{
    freopen("in.txt","r",stdin);
//    freopen("out.txt","w",stdout);
    int t,cases=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&n,&m);
        for(int i=0; i<n; ++i)
            scanf("%s",str[i]);
        flag=false;
        solve();
        printf("Case #%d:\n",cases++);
        if(flag)
        {
            printf("Impossible\n");
        }
        else
        {
            for(int i=0;i<n;++i)
            printf("%s\n",str[i]);
        }
    }
    return 0;
}
