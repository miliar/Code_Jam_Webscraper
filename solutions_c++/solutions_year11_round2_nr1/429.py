#include<stdio.h>
#include<vector>
using namespace std;
vector<int> v[103];
int pld[103],cnt[103],p[103][103];
char str[103];
double ans[103],sum[103];
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("A-large (1).txt","w",stdout);
    int test,cas,n,i,j,c1;
    double sum1;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d",&n);
        for (i=0;i<n;i++)
        {
            scanf("%s",str);
            pld[i]=cnt[i]=0;
            for (j=0;j<n;j++)
            {
                if (str[j]=='1'||str[j]=='0')
                {
                    v[i].push_back(j);
                    p[i][j]=str[j]-'0';
                    cnt[i]+=str[j]-'0';
                    pld[i]++;
                }
            }
        }
        for (i=0;i<n;i++)
        {
            ans[i]=0.25*(cnt[i]*1.0)/pld[i];
            c1=0;
            sum[i]=0.0;
            for (j=0;j<v[i].size();j++)
            {
                c1++;
                sum[i]+=(cnt[v[i][j]]-p[v[i][j]][i])*1.0/(pld[v[i][j]]-1);
            }
            sum[i]/=c1;
            ans[i]+=0.50*sum[i];
        }
        for (i=0;i<n;i++)
        {
            sum1=0.0;
            for (j=0;j<v[i].size();j++)
            {
                sum1+=sum[v[i][j]];
            }
            ans[i]+=0.25*sum1/pld[i];
        }
        printf("Case #%d:\n",cas);
        for (i=0;i<n;i++) printf("%.12lf\n",ans[i]);
        for (i=0;i<n;i++) v[i].clear();
    }
    return 0;
}
