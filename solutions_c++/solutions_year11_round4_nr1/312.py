#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
using namespace std;

struct way {
    int l,s;
} a[100000];

bool operator<(way x,way y) {
    return x.s<y.s;
}

int main() {
    int T;
    cin>>T;
    for(int TT=1;TT<=T;TT++) {
        int x,s,r,t,n;
        cin>>x>>s>>r>>t>>n;
        int sw=x;
        for (int i=0;i<n;i++) {
            int p,q,u;
            cin>>p>>q>>u;
            a[i].l=q-p;
            a[i].s=u;
            sw-=q-p;
        }
        a[n].l=sw;
        a[n].s=0;
        n++;
        double ans=0;
        double run=t;
        sort(a,a+n);
        for(int i=0;i<n;i++) {
            //cerr<<a[i].s<<' '<<a[i].l<<endl;
            double runtime=a[i].l*1.0/(r+a[i].s);
            double walktime=a[i].l*1.0/(s+a[i].s);
            if (run>runtime) {
                ans+=runtime;
                run-=runtime;
            } else if (run>0) {
                double rundis=(r+a[i].s)*run;
                ans+=run;
                ans+=(a[i].l-rundis)*1.0/(s+a[i].s);
                run=-1;
            } else ans+=walktime;
        }
        cout<<setprecision(8);
        cout<<fixed;
        cout<<"Case #"<<TT<<": "<<ans<<endl;
    }
    return 0;
}
