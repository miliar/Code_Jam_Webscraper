#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>

using namespace std;

#define NN 1024

int tt,n,m,d;
int map[500][500];

inline double abs(double x)
{
    return (x>0)?(x):(-x);
}

bool check(int x,int y,int r)
{
    double tx=(x*2.0+r-1.0)/2.0,ty=(y*2.0+r-1.0)/2.0;
    double ansx=0,ansy=0;
    for (int i=x;i<x+r;i++)
        for (int j=y;j<y+r;j++)
        {
            if ((i==x || i==x+r-1)&&(j==y || j==y+r-1)) continue;
            ansx+=(i-tx)*map[i][j];
            ansy+=(j-ty)*map[i][j];
        }
    return (abs(ansx)<1e-6 && abs(ansy)<1e-6);
}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    scanf("%d\n",&tt);
    for (int ii=1;ii<=tt;ii++)
    {
        scanf("%d%d%d\n",&n,&m,&d);
        for (int i=1;i<=n;i++)
        {
            char ch;
            for (int j=1;j<=m;j++)
            {
                scanf("%c",&ch);
                map[i][j]=ch-48;
            }
            scanf("\n");
        }
        int ans=0;
        for (int i=1;i<n-1;i++)
            for (int j=1;j<m-1;j++)
            {
                int r=min(n-i+1,m-j+1);
                for (int k=3;k<=r;k++)
                {
                    if (i==2 && j==2 && k==5)
                    {
                        i++;
                        i--;
                    }
                    if (check(i,j,k) && k>ans)
                        ans=k;
                }
            }
        printf("Case #%d: ",ii);
        if (ans==0)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n",ans);
    }
    return 0;
}
