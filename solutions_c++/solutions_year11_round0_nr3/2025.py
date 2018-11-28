#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int t,i;
    long long k[1200];
    int num=1;
    scanf("%d",&t);
    while(t--)
    {
         int n;
         scanf("%d",&n);
         long long res = 0;
         long long sum = 0;
         for(i=0;i<n;i++)
         {
             scanf("%I64d",&k[i]);
             res ^= k[i];
             sum += k[i];
         }
         sort(k,k+n);
         if(res != 0)
           printf("Case #%d: NO\n",num++);
         else
           printf("Case #%d: %d\n",num++,sum-k[0]);
    }
    return 0;
}
