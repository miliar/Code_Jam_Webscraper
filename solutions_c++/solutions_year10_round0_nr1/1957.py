// snapper, mrozik, 2010
#include <iostream>
using namespace std;

int main() {
    int tt; cin>>tt;
    for (int t=1; t<=tt; t++) {
        
        unsigned n, k; cin>>n>>k;
        unsigned s = (1<<n)-1;
        bool onOff = ((k&s)==s);
        cout<<"Case #"<<t<<": "<<(onOff ? "ON" : "OFF")<<endl;
    }
    
    return 0;
}
