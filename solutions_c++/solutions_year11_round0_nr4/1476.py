#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int T,N;
int main(){
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    cin>>T;
    for (int i=1;i<=T;++i) {
        cout<<"Case #"<<i<<": ";
        cin>>N;
        int cnt=0;
        for (int j=1;j<=N;++j) {
            int num;
            scanf("%d",&num);
            if (num!=j) ++cnt;
        }
        cout<<cnt<<".000000\n";
    }
    return 0;
}
