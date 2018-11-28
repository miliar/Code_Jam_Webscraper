#include <iostream>

using namespace std;

int t,n,a[41];

int work()
{
    int i,j;
    cin>>n;
    for (i=1;i<=n;i++)
    {
        a[i]=0;
        for (j=1;j<=n;j++)
        {
            char pp;
            cin>>pp;
            if (pp=='1') a[i]=j;
        }
        }
    int ans=0;
    for (i=1;i<=n;i++)
    {
        if (a[i]>i)
        {
                   for (j=i+1;j<=n;j++)
                       if (a[j]<=i) break;
                   ans+=(j-i);
                   while (j>=i+1){swap(a[j],a[j-1]);j--;}
        }
    }
    return ans;
}           

int main()
{
    freopen("gcj1.in","r",stdin);
    freopen("gcj1.out","w",stdout);
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<": "<<work()<<endl;
    }
    return 0;
}
