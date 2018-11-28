#include<iostream>
using namespace std;
int main(){
    int T,N,K,i=1;
    cin>>T;
    while(i<=T){
               cin>>N>>K;
               cout<<"Case #"<<i<<": ";
               if(((K+1)%(1<<N)) == 0)
                             cout<<"ON\n";
               else
                             cout<<"OFF\n";
               i++;
    }
    return 0;
}
