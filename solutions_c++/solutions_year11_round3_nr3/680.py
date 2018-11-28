#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;
int n,l,h;
int a[1200];
int main()
{
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,k;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d%d%d",&n,&l,&h);
        for(int i=0;i<n;i++)
        scanf("%d",&a[i]);
        int ans=-1;
        for(int i=l;i<=h;i++)
        {
            int j;
            for(j=0;j<n;j++)
            {
                if(i%a[j]!=0&&a[j]%i!=0)
                break;
            }
            if(j==n){
            ans=i;break;}
        }
        if(ans==-1)
        printf("Case #%d: NO\n",k);
        else
        printf("Case #%d: %d\n",k,ans);
    }
    return 0;
}
