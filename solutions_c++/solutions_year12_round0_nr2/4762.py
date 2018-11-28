#include <iostream>
#include <cstdio>
using namespace std;
int n,m,s,p,u,v,d,ans;
int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>n;
    for (int i=1;i<=n;++i) {

        cin>>m>>s>>p;

        u = 0;
        v = 0;
        for (int j=1;j<=m;++j) {
            cin>>d;
            if (d>=3*p-2) {
                u++;
            } else if (d>=3*p-4) {
                if (d!=0 && d!=1)
                    v++;
            }
            ans = u+ (v<s?v:s);
        }
        cout<<"Case #";
        cout<<i;
        cout<<": ";
        cout<<ans<<endl;

    }


    return 0;
}
