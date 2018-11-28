#include <iostream>
#include <iomanip>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

const int yyy=1111111;
bool isp[yyy];

int main() {
    for(int i=2;i<yyy;i++) isp[i]=true;
    isp[1]=isp[0]=false;
    for(long long i=2;i<yyy;i++)if(isp[i]) {
        for(long long j=i*i;j<yyy;j=j+i) isp[j]=false;
    }
    int T;
    cin>>T;
    for(int TT=1;TT<=T;TT++) {
        int n;
        cin>>n;
        int ans=1;
        for(long long i=2;i*i<=n;i++) if (isp[i]) {
            for(long long j=i*i;j<=n;j*=i) ans++;
        }
        if (n==1) ans=0;
        cout<<"Case #"<<TT<<": "<<ans<<endl;
    }
    return 0;
}
