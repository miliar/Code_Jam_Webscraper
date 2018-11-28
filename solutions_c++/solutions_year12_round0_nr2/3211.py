#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T,n,s,p,a,ans;
    cin>>T;
    for (int k=1; k<=T; k++) {
        cout<<"Case #"<<k<<": ";
        ans = 0;
        cin>>n>>s>>p;
        //cout<<n<<" "<<s<<" "<<p<<" ";
        for (int i=0; i<n; i++) {
            cin>>a;
            //cout<<a<<" ";
            int j = a/3+(a%3?1:0);
            if (j>=p) ans++;
            else if (j+1==p && s && (a%3 != 1) && a && (p<=10) && (p>=0)) {
                s--;
                ans++;
            }
        }
        cout<<ans<<endl;
        //cout<<endl;
    }
    return 0;
}
