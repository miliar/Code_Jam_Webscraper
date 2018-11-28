#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large-attempt22.out","w",stdout);
    long long t,i,j,n,a[1000];
    scanf("%lld",&t);
    for(i=0;i<t;i++)
    {
                    long sum=0;
                    scanf("%lld",&n);
                    for(j=0;j<n;j++)
                    scanf("%lld",&a[j]);
                    for(j=0;j<n;j++)
                    sum=sum^a[j];
                    if(sum!=0)
                    {
                    printf("Case #%lld: NO\n",i+1);
                    continue;
                    }
                    long min=10000000;
                    sum=0;
                    for(j=0;j<n;j++)
                    {
                                    if(a[j]<min)
                                    min=a[j];
                                    sum+=a[j];
                    }
                    printf("Case #%lld: %lld\n",i+1,sum-min);
    }
    return 0;
}
