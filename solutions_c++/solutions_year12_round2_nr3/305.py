#include <stdio.h>
#include <vector>
using namespace std;
int a[100],b[100],c[100];
vector <int> g[2000010];
void output(int x)
{
    int cnt=0;
    for (int i=0;i<20;i++)
        if (x&(1<<i)) b[cnt++]=a[i];
    printf("%d",b[0]);
    for (int i=1;i<cnt;i++)
        printf(" %d",b[i]);
    puts("");
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int ii=1;ii<=T;ii++)
    {
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
            scanf("%d",&a[i]);
        for (int i=0;i<=2000000;i++) g[i].clear();
        for (int i=0;i<(1<<n);i++)
        {
            int cnt0=0,cnt1=0;
            for (int j=0;j<n;j++)
                if (i&(1<<j)) b[cnt0++]=a[j];
            if (cnt0==0) continue;
            int sum=0;
            for (int j=0;j<cnt0;j++)
                sum+=b[j];
            g[sum].push_back(i);
        }
        printf("Case #%d:\n",ii);
        bool ans=false;
        for (int i=0;i<=2000000&&!ans;i++)
        {
            int len=g[i].size();
            if (len<2) continue;
            for (int j=0;j<len&&!ans;j++)
                for (int k=j+1;k<len&&!ans;k++)
                    if (!(g[i][j]&g[i][k]))
                    {
                        ans=true;
                        output(g[i][j]);
                        output(g[i][k]);
                    }
        }
        if (!ans) puts("Impossible");
    }
    return 0;
}
