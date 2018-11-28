#include<stdio.h>
#include<math.h>
#include<algorithm>
using namespace std;
double arr[1000003],arr1[1000003];
int main()
{
    freopen("B-small-attempt0 (1).in","r",stdin);
    freopen("B-small-attempt0 (1).txt","w",stdout);
    int test,cas,c,n,i,v,j;
    double d,p,lo,hi,mid,pos;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d%lf",&c,&d);
        n=0;
        for (i=0;i<c;i++)
        {
            scanf("%lf%d",&p,&v);
            for (j=0;j<v;j++) arr[n++]=p;
        }
        lo=0.0;
        hi=1e+10;
        while (fabs(hi-lo)>1e-11)
        {
            mid=(lo+hi)/2.0;
            arr1[0]=arr[0]-mid;
            for (i=1;i<n;i++)
            {
                if (arr1[i-1]+d<arr[i]+1e-11)
                {
                    pos=max(arr[i]-mid,arr1[i-1]+d);
                }
                else
                {
                    if (arr1[i-1]+d+1e-11>arr[i]+mid) break;
                    pos=arr1[i-1]+d;
                }
                arr1[i]=pos;
            }
            if (i<n) lo=mid;
            else hi=mid;
        }
        printf("Case #%d: %.10lf\n",cas,(lo+hi)/2.0);
    }
    return 0;
}
