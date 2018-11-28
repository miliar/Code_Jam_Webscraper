#include <iostream>
#include <cmath>
using namespace std;

int a[600][600];
int n,m,d;

int calc(int enx, int eny, int L)
{
    int stx=enx-L+1,sty=eny-L+1;
    double mx=double(stx+enx)/2,my=double(sty+eny)/2;
    double sx=0,sy=0;
    for (int i=stx;i<=enx;i++)
        for (int j=sty;j<=eny;j++)
        {
            if (i==stx&&j==sty) continue;
            if (i==stx&&j==eny) continue;
            if (i==enx&&j==sty) continue;
            if (i==enx&&j==eny) continue;
            sx+=double(i-mx)*a[i][j];
            sy+=double(j-my)*a[i][j];
        }
    if (fabs(sx)<1e-8&&fabs(sy)<1e-8) return L;
    else return 0;
}
        
    

int main()
{
    freopen("b2.in","r",stdin);
    freopen("b2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d%d%d",&n,&m,&d);
        for (int i=1;i<=n;i++)
        {
            getchar();
            for (int j=1;j<=m;j++)
            {
                char c=getchar();
                a[i][j]=c-'0'+d;
            }
        }
        int ans=0;
        for (int i=3;i<=n;i++)
            for (int j=3;j<=m;j++)
                for (int k=max(ans,3);k<=min(i,j);k++)
                    ans>?=calc(i,j,k);
        if (ans==0) printf("Case #%d: IMPOSSIBLE\n",cas);
        else printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
