#include<iostream>
#include<cstdio>
#include<fstream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>

using namespace std;

int sum,mini,n;
long long tot;

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);
    int cs;
    cin>>cs;
    for (int k=1;k<=cs;k++){
        cin>>n;
        tot=0;
        sum=0;
        mini=10000000;
        for (int i=1;i<=n;i++){
            int t;
            cin>>t;
            sum^=t;
            mini=min(mini,t);
            tot+=long(t);
            }
        cout<<"Case #"<<k<<": ";
        if (sum==0) cout<<tot-mini<<endl;
           else cout<<"NO"<<endl;
        }
}
