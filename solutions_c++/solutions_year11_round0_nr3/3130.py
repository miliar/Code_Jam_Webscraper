#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#define pb push_back
using namespace std;
int call(int);
int a[20];
int n;
int to(int,int);
int main()
{
    int t;
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        scanf("%d",&n);
        int c;
        for(int i=0;i<n;i++)
        {
            scanf("%d",&c);
            a[i]=c;
        }
        int ans=-1;
        for(int i=0;i<(1<<n)-1;i++)
        {
            ans=max(ans,call(i));
        }
        printf("Case #%d: ",k);
        if(ans==-1)
        {
            printf("NO\n");
            continue;
        }
        printf("%d\n",ans);
    }
    return 0;
}
int call(int x)
{
    int sum1=0,sum2=0;
    int acsum1=0,acsum2=0;
    for(int i=0;i<n;i++)
    {
        if(x&(1<<i))
        sum1=sum1^a[i],acsum1+=a[i];
        else
        sum2=sum2^a[i],acsum2+=a[i];
    }
    if(sum1==sum2)
    return acsum1;
    return -1;
}








