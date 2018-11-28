#include <iostream>
using namespace std;


double f[1001][1001];
double ans[1001];
bool b[1001];
int a[1001];
int n;

int main()
{
    freopen("111.in","r",stdin);
    freopen("111.out","w",stdout);
    memset(f,0,sizeof(f));
    memset(ans,0,sizeof(ans));
    f[1][1]=0;
    for (int i=2;i<=1000;i++)
    {
        f[i][0]=1;
        for (int j=1;j<=i;j++) f[i][0]/=j;
        double t=1,sum=0;
        for (int j=1;j<=i;j++)
        {
            f[i][j]=f[i][j-1]*(i-j+1);
            if (sum>0) f[i][j]/=sum;
            t/=j;
            if (j>1)
            {
                if (j&1) sum-=t;
                else sum+=t;
            }
            if (sum>0)  f[i][j]*=sum;
        }
        f[i][1]=0;
    }
    ans[1]=0;
    for (int i=2;i<=1000;i++)
    {
        for (int j=1;j<=i;j++)
            ans[i]+=f[i][i-j]*(ans[i-j]+1);
        ans[i]=(ans[i]+f[i][i])/(1-f[i][i]);
    }
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        for (int i=1;i<=n;i++) scanf("%d",a+i);
        double tot=0;
        memset(b,1,sizeof(b));
        for (int i=1;i<=n;i++)
            if (b[i])
            {
                 int L=1;
                 for (int j=a[i];j!=i;j=a[j])
                 {
                     b[j]=0;
                     L++;
                 }
                 tot+=ans[L];
            }
        printf("Case #%d: %.6lf\n",cas,tot);
    }
    return 0;
}
