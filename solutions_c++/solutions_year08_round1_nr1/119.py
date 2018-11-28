#include<iostream>
#include<algorithm> 
using namespace std;
int main()
{
    int casen,n;
    int a[1000],b[1000];
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout); 
    scanf("%d",&casen);
    for (int casei=1;casei<=casen;casei++)
    {
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
          scanf("%d",&a[i]);
        for (int i=1;i<=n;i++)
          scanf("%d",&b[i]);
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        long long ans=0;
        for (int i=1;i<=n;i++)
          ans+=(long long)((long long)a[i]*(long long)b[n+1-i]);
        cout <<"Case #"<<casei<<": "<<ans<<endl;
    }
    return 0;
}
