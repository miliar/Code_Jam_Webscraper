#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int T,N;
int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    cin>>T;
    for (int i=1;i<=T;++i) {
        cout<<"Case #"<<i<<": ";
        cin>>N;
        int XORAns=0,Sum=0,Minn=10000000;
        for (int j=1;j<=N;++j) {
            int num;
            scanf("%d",&num);
            XORAns^=num;
            Sum+=num;
            Minn<?=num;
        }
        if (XORAns) cout<<"NO";
        else cout<<Sum-Minn;
        cout<<"\n";
    }
    return 0;
}
