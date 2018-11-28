#include<iostream>
using namespace std;
int a[1005],b[1005];
int main()
{
    freopen("a.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        scanf("%d%d",&a[i],&b[i]);
        int ans=0;
        for(int i=0;i<n;i++)
           for(int j=i+1;j<n;j++)
           if((a[i]>a[j]&&b[i]<b[j])||(b[i]>b[j]&&a[i]<a[j]))ans++;
        printf("Case #%d: %d\n",cas++,ans);
    }
    return 0;    
}
