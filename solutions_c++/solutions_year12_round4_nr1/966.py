#include <iostream>
#include <cstring>
#include <string>
#include <algorithm>
#include <cstdlib>
#include <cstdio>
using namespace std;
int vine[10005];
int pos[10005];
int n;
int far=0;
int dp[10005];
int des;
void solve()
{
    far=0;
    dp[0]=pos[0]*2;
    far=dp[0];
    for(int i=1;i<n;i++)
    {
//        if(far<pos[i])
//            break;
        for(int j=i-1;j>=0;j--)
        {
            if(dp[j]>=pos[i])
                dp[i]=max(dp[i],pos[i]+min(vine[i],pos[i]-pos[j]));
        }
        far = max(far,dp[i]);
    }
    for(int i=0;i<n;i++)
    {
        if(dp[i]>=des)
        {
            cout<<"YES"<<endl;
            return;
        }
    }
    cout<<"NO"<<endl;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out4.txt","w",stdout);
    int t;
    int cas=1;
    cin>>t;
    while(t--)
    {
        memset(dp,0,sizeof(dp));
        far=0;
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>pos[i]>>vine[i];
        cin>>des;
        cout<<"Case #"<<cas++<<": ";
        solve();

    }
    return 0;
}
