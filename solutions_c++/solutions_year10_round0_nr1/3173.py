#include<iostream>
#include <cmath>
using namespace std;

int main(){
    freopen("input.in","rt",stdin);
    freopen("output.out","wt",stdout);
    
    int T,N;
    long long K;
    cin>>T;
    for (int i=1 ; i<=T ; i++){
        cin>>N>>K;
        cout<<"Case #"<<i<<": ";
        
        long long pw = pow(2.0,N*1.0);
        //cout<<"pow is "<<pw<<endl;
        if ((K+1) % pw == 0 )
           cout<<"ON\n";
        else cout<<"OFF\n";
    }
    //system("pause");
    return 0;
}
