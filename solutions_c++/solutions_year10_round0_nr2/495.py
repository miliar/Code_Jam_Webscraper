#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int t[5],dist[5];

int main()
{
    int c,i,j,k,n;
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);

    cin>>c;
    for(i=1;i<=c;i++)
    {
        cin>>n;
        for(j=0;j<n;j++)
            cin>>t[j];
        sort(t,t+n);
        for(j=1;j<n;j++)
            dist[j]=t[j]-t[j-1];
        int GCD=dist[1];
        for(j=2;j<n;j++)
        GCD=__gcd(GCD,dist[j]);
        int ans;

        if(t[0]%GCD==0)
            ans=0;
        else
            ans=GCD-(t[0]%GCD);
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
return 0;
}
