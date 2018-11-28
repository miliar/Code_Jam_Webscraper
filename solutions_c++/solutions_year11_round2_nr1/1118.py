#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

char map[105][105];
struct node
{
    double wp,owp,oowp;
}a[105];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++)
    {
        printf("Case #%d:\n",cas);
        int n;
        scanf("%d",&n);
        for (int i=0;i<n;i++)
        {
            scanf("%s",map[i]);
            int len=strlen(map[i]);
            int cnt=0,tot=0;
            for (int j=0;j<len;j++)
            {
                if (map[i][j]=='1') cnt++;
                if (map[i][j]!='.') tot++;
            }
            a[i].wp=(double)cnt/(double)tot;
        }
        for (int i=0;i<n;i++)
        {
            double sum=0;
            int totop=0;
            for (int j=0;j<n;j++)
            {
                if (i==j) continue;
                if (map[i][j]=='.') continue;
                totop++;
                int t1=0,t2=0;
                for (int k=0;k<n;k++)
                {
                    if (k==i) continue;
                    if (map[j][k]=='1') t1++;
                    if (map[j][k]!='.') t2++;
                }
                sum+=(double)t1/(double)t2;
            }
            a[i].owp=sum/(double)totop;
        }
        for (int i=0;i<n;i++)
        {
            double sum=0;
            int totop=0;
            for (int j=0;j<n;j++)
            {
                if (i==j) continue;
                if (map[i][j]=='.') continue;
                sum+=a[j].owp;
                totop++;
            }
            a[i].oowp=sum/(double)totop;
        }
        for (int i=0;i<n;i++)
        {
            double rpi=0.25*a[i].wp+0.50*a[i].owp+0.25*a[i].oowp;
            printf("%.8lf\n",rpi);
        }
    }
}
