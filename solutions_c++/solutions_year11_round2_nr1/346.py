#include <iostream>
using namespace std;

int n;
char a[200][200];
int w[200],s[200];
double wp[200],owp[200],oowp[200];

int main()
{
    freopen("a2.in","r",stdin);
    freopen("a2.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        memset(w,0,sizeof(w));
        memset(s,0,sizeof(s));
        for (int i=1;i<=n;i++)
        {
            getchar();
            for (int j=1;j<=n;j++)
            {
                a[i][j]=getchar();
                if (a[i][j]=='1') w[i]++;
                if (a[i][j]!='.') s[i]++;
            }
        }
        for (int i=1;i<=n;i++) wp[i]=double(w[i])/s[i];
        for (int i=1;i<=n;i++)
        {
            owp[i]=0;
            for (int j=1;j<=n;j++)
                if (a[i][j]!='.') owp[i]+=double(w[j]-(a[j][i]-48))/(s[j]-1);
            owp[i]/=s[i];
        }
        for (int i=1;i<=n;i++)
        {
            oowp[i]=0;
            for (int j=1;j<=n;j++)
                if (a[i][j]!='.') oowp[i]+=owp[j];
            oowp[i]/=s[i];
        }
        printf("Case #%d:\n",cas);
        for (int i=1;i<=n;i++) printf("%.8lf\n",0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
    }
}
        
        
        
