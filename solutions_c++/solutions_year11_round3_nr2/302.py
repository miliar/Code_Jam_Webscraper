#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int a[1234567];

int main() {
    int T;
    cin>>T;
    for(int TT=1;TT<=T;TT++) {
        int l,n,c;
        long long t;
        cin>>l>>t>>n>>c;
        for(int i=0;i<c;i++) cin>>a[i];
        for(int i=c;i<n;i++) a[i]=a[i%c];
        for(int i=0;i<n;i++) a[i]=2*a[i];
        long long ans=0;
        int q=0;
        while(t>0 && q<n) {
            if (t>=a[q]) {
                ans+=a[q];
                t-=a[q];
                q++;
            } else {
                a[q]-=t;
                ans+=t;
                t=0; break;
            }
        }
        if (t<0) cerr<<"ERROR"<<endl;
        if (t==0 && q<n) {
            sort(a+q,a+n);
            for(int i=0;i<l && i<n;i++) a[n-1-i]/=2;
            for(int i=q;i<n;i++) ans+=a[i];
        }
        cout<<"Case #"<<TT<<": "<<ans<<endl;
    }
    return 0;
}
