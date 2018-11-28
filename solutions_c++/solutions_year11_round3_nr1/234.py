#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int dx[5]={0,0,1,1},dy[5]={0,1,0,1};
char s[10]="/\\\\/";
char a[105][105];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        int n,m;
        printf("Case #%d:\n",cas);
        scanf("%d%d",&n,&m);
        for (int i=0;i<n;i++)
            scanf("%s",a[i]);
        bool flag=true;
        for (int i=0;i<n;i++)
            for (int j=0;j<m;j++)
                if (a[i][j]=='#')
                {
                    for (int k=0;k<4;k++)
                    {
                        int tx=i+dx[k],ty=j+dy[k];
                        if (tx>=0 && tx<n && ty>=0 && ty<m && a[tx][ty]=='#')
                            a[tx][ty]=s[k];
                        else flag=false;
                    }
                }
        if (!flag) puts("Impossible");
        else
        {
            for (int i=0;i<n;i++) puts(a[i]);
        }
    }
}
