#include <iostream>
#include <fstream>
using namespace std;
ofstream fout("holstein.out");
long long T,N,K;
long long num[32];
int main(){
    cin>>T;
    num[0]=1;
    for(int i=1;i<=30;i++){
            num[i]=2*num[i-1];
    }
    for(int i=1;i<=T;i++){
            cin>>N>>K;
            if(K%num[N]==num[N]-1) fout<<"Case #"<<i<<": "<<"ON"<<endl;
            else fout<<"Case #"<<i<<": "<<"OFF"<<endl; 
    }
}
