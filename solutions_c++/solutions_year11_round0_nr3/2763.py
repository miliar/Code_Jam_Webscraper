#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int t,n,in[1200],i,j;
    //freopen("GCS.in","r",stdin);
    freopen("GCS.out","w",stdout);
    scanf("%d",&t);
    for(int cn=1;cn<=t;cn++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)scanf("%d",in+i);
        sort(in,in+n);
        int ok=0,ma=0;
        for(i=0;i<(1<<n);i++)
        {
            int o=0;
            int sum1=0,sum2=0;
            vector<int> l1,l2;
            l1.clear();l2.clear();
            for(j=0;j<n;j++)
                if(i&(1<<j))l1.push_back(in[j]);
                else l2.push_back(in[j]);
            if(l1.size()==0||l2.size()==0)continue;
            for(j=1,sum1=l1[0];j<l1.size();j++)
            {
                //printf("%d^%d=%d\n",sum1,l1[j],sum1^l1[j]);
                sum1=sum1^l1[j];
            }
            for(j=1,sum2=l2[0];j<l2.size();j++)
            {
                //printf("%d^%d=%d\n",sum2,l2[j],sum2^l2[j]);
                sum2=sum2^l2[j];
            }
            if(sum1==sum2)ok=o=1;
            if(o)
            {
                for(j=0,sum1=0;j<l1.size();j++)sum1+=l1[j];
                ma=max(ma,sum1);
            }
        }
        printf("Case #%d: ",cn);
        if(ok)printf("%d\n",ma);
        else printf("NO\n");
    }
    return 0;
}
