#include<iostream>
using namespace std;
int main(){
    long T,K,N,count=0;
    cin>>T;
    while(T--){
        count++;
        cin>>N>>K;
        cout<<"Case #"<<count<<": ";
        if((K+1)%(1<<N)==0){
            cout<<"ON"<<endl;
        }else{
            cout<<"OFF"<<endl;
        }
    }
    return 0;
}
