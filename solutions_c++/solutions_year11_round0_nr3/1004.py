#include<iostream>
#include<math.h>
#include<fstream>
#include<algorithm>
#include<string>
#include<stack>
#include<vector>
typedef long long lint;
using namespace std;
int main()
{
    freopen("agrahri.in","r",stdin);
    freopen("test-large.out","w",stdout);
    lint tt;
    cin>>tt;
    for(lint xx=1;xx<=tt;xx++)
    {
        lint n;cin>>n;
        lint sum=0,exr=0,smlst;
        lint m;
        cin>>m;
        sum=m;exr=m;smlst=m;
        for(lint y=0;y<n-1;y++)
        {
            cin>>m;sum+=m;exr^=m;if(smlst>m)smlst=m;
        }
       // cout<<"sum="<<sum<<" exr="<<exr<<" smlst="<<smlst<<"\n";
        if(exr!=0)
        cout<<"Case #"<<xx<<": NO\n";
        else cout<<"Case #"<<xx<<": "<<sum-smlst<<"\n";
    }
	return 0;
}
