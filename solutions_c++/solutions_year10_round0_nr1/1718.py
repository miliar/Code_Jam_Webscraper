#include<iostream>
#include<cstdio>
using namespace std;
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,n;long long k;
    cin>>t;
    for(int i=1;i<=t;++i){
        cin>>n>>k;
        if(k%(1<<n)==(1<<n)-1) cout<<"Case #"<<i<<": "<<"ON"<<endl;
        else cout<<"Case #"<<i<<": "<<"OFF"<<endl;
    }
    return 0;
} 
