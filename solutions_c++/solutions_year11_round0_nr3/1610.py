// GCJ 2011, mrozik
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
using namespace std;

int main() {
    
    int t, T; cin>>T;
    for (int t=1; t<=T; t++) {
        
        int sum=0, xor_=0, min_=0x7fffffff;
        
        int n; cin>>n;
        while ( n --> 0 ) {
            int c; cin>>c;
            sum+=c;
            xor_^=c;
            min_=min(min_, c);
        }
        
        cout<<"Case #"<<t<<": ";
        if (xor_!=0)
            cout<<"NO"<<endl;
        else
            cout<<(sum-min_)<<endl;
    }
    
    return 0;
}
