#include<set>
#include<cmath>
#include<vector>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B.out","w",stdout);
    int t,n,s,p,f[105];
    cin>>t;
    for (int cnt=1;cnt<=t;cnt++)
    {
        cin>>n>>s>>p;
        for (int i=0;i<n;i++)
            cin>>f[i];
        sort(f,f+n);
//        for (int i=0;i<n;i++)
//            cout<<f[i]<<" ";
//        cout<<endl;
        int ans(0),sum(0);
        for (int i=0;i<n;i++)
        {
            int sp,usp;
            if (f[i]%3==0) {sp=f[i]/3+1; usp=f[i]/3;}
            if (f[i]%3==1) {sp=f[i]/3+1; usp=f[i]/3+1;}
            if (f[i]%3==2) {sp=f[i]/3+2; usp=f[i]/3+1;}
            if (f[i]==1) {sp=0; usp=1;}
            if (f[i]==0) {sp=0; usp=0;}
            //cout<<sp<<" "<<usp<<endl;
            if (sum<s && sp>=p && usp<p) {sum++; ans++;}
            if (usp>=p) ans++;
        }
        cout<<"Case #"<<cnt<<": "<<ans<<endl;
    }
    fclose(stdin);
    fclose(stdout);
}
