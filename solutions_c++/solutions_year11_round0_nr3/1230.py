#include<iostream>

using namespace std;

int main(){
    freopen("C-large.in","r",stdin);
    freopen("x.out","w",stdout);
    int tc,n;
    cin>>tc;
    for(int t=1;t<=tc;t++){
        cin>>n;
        long long sum=0,xr=0,m=-1u/2,c;
        for(int i=0;i<n;i++){
            cin>>c;
            xr^=c;
            sum+=c;
            m<?=c;
        }
        if(xr)printf("Case #%d: NO\n",t);
        else printf("Case #%d: %d\n",t,sum-m);
    }
    return 0;
}
