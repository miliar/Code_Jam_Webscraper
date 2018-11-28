#include <iostream>
#include <cstdio>
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    
    int ntest;
    cin>>ntest;
    
    int n,k,t;
    for(int test=0;test<ntest;test++){
        cin>>n>>k;
        int t = (1<<n);
        cout<<"Case #"<<test+1<<": ";
        if (k%t == t-1) cout<<"ON"<<endl; else cout<<"OFF"<<endl;
    }
    
    return 0;
}
