#include <string>
#include <cstdio>
#include <iostream>
using namespace std;

int main(){
    
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    
    int t, n, m, k;
    
    cin>>t;
    for (int j=1; j<=t; j++){
          m=1;
          cin>>n>>k;
          for (int i=1; i<=n; i++) m*=2;
          if (k%m==m-1) cout<<"Case #"<<j<<": ON"<<endl;
              else cout<<"Case #"<<j<<": OFF"<<endl;
          }
    
    return 0;
}
