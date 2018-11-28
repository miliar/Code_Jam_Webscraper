#include <iostream>
#include<algorithm>

using namespace std;

int t,i,j,k,p,q,f[105][105],a[105];

int work(int l,int r)
{
    if (f[l][r]>-1) return f[l][r];
    if (l>r) return 0;
    int k;
    for (k=l;k<=r;k++)
    {
        int temp=a[r+1]-a[l-1]-2+work(l,k-1)+work(k+1,r);
        if (f[l][r]==-1) f[l][r]=temp;
        else f[l][r]=min(f[l][r],temp);
    }
    return f[l][r];
}

int main()
{
    freopen("gcj3.in","r",stdin);
    freopen("gcj3.out","w",stdout);
    cin>>t;
    for (int ii=1;ii<=t;ii++)
    {
        memset(f,0xff,sizeof(f));
        cin>>p>>q;
        a[0]=0;
        for (i=1;i<=q;i++) cin>>a[i];
        sort(a+1,a+q+1);
        a[q+1]=p+1;
        cout<<"Case #"<<ii<<": "<<work(1,q)<<endl;
    }
    return 0;
}
