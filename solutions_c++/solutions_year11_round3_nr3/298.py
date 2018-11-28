#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int a[12345];

int main() {
    int T;
    cin>>T;
    for(int TT=1;TT<=T;TT++) {
        int n,l,h;
        cin>>n>>l>>h;
        for(int i=0;i<n;i++) cin>>a[i];
        int ans=0;
        for(int w=l;w<=h;w++) {
            bool ok=true;
            for(int i=0;i<n;i++) {
                if (a[i]%w!=0 && w%a[i]!=0 ) {
                    ok=false;
                    break;
                }
            }
            if (ok) {
                ans=w;
                break;
            }
        }
        cout<<"Case #"<<TT<<": ";
        if (ans>0) cout<<ans<<endl;
        else cout<<"NO"<<endl;
    }
    return 0;
}
