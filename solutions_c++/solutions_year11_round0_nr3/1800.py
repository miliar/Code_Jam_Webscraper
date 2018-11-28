#include<stdio.h>
#include<algorithm>
using namespace std;
int arr[1003];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.txt","w",stdout);
    int test,cas,n,sum,i,res;
    scanf("%d",&test);
    for (cas=1;cas<=test;cas++)
    {
        scanf("%d",&n);
        sum=0;
        for (i=0;i<n;i++)
        {
            scanf("%d",&arr[i]);
            sum+=arr[i];
        }
        sort(arr,arr+n);
        res=0;
        for (i=1;i<n;i++) res=res^arr[i];
        if (res!=arr[0]) printf("Case #%d: NO\n",cas);
        else printf("Case #%d: %d\n",cas,sum-arr[0]);
    }
    return 0;
}
