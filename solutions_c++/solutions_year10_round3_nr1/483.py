#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
#define see(x) cout<<#x<<" "<<x<<endl
#define sp system("pause")
bool inter(int a1,int a2,int b1,int b2)
{
     if(a1>b1 && a2<b2)
         return true;
     if(a1<b1 && a2>b2)
         return true;
     return false;
}
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T,n,i,j;
    long long ans;
    int a[1000],b[1000];
    scanf("%d",&T);
    for(int cas=1;cas<=T;cas++)
    {
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%d%d",&a[i],&b[i]);
        }
        ans=0;
        for(i=0;i<n;i++)
            for(j=i+1;j<n;j++)
            {
                if(inter(a[i],b[i],a[j],b[j]))
                    ans++;
            }
        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
