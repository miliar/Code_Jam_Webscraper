#include <iostream>

using namespace std;

int main(){
    int nc=0;
    cin>>nc;
    for (int i=0; i<nc; i++){
        int n,k;
        cin>>n>>k;
        
        int r = k & ((1<<n) -1);
        if (r == ((1<<n) -1) ){
              cout<<"Case #"<<i+1<<": ON"<<endl;
              }
        else
              cout<<"Case #"<<i+1<<": OFF"<<endl;
        
    }
    return 0;
}
