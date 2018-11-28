#include <iostream>
#include <cmath>

using namespace std;

long long T,N,K,tmp;

int main(){
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>N>>K;
        tmp=pow(2.,(double)N);
        cout<<"Case #"<<i<<": ";
        if(tmp-1 == K%tmp) cout<<"ON\n";
        else cout<<"OFF\n";
    }
    return 0;
}
