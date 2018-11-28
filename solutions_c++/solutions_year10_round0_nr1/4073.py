#include<iostream>
#include<fstream>

#include<cmath>
using namespace std;

int T,N,K;
int main() {
    cin>>T;
    for(int i=0;i<T;i++) {
        cin>>N>>K;
        int a=pow(2,N);
        while(K>a) K-=a;
        cout<<"Case #"<<(i+1)<<": ";
        if(K==a-1) cout<<"ON";
        else cout<<"OFF";
        cout<<endl;
    }
}
