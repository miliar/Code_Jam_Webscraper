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
        
        int n; cin>>n;
        
        int ot=0, bt=0;
        int op=1, bp=1;
        
        while (n --> 0) {
            char robot; int dest; cin>>robot>>dest;
            
            if (robot=='O') {
                int dist = abs(dest-op);
                ot = max(bt, ot + dist)+1;
                op = dest;
            }
            else {
                int dist = abs(dest-bp);
                bt = max(ot, bt + dist)+1;
                bp = dest;
            }
        }
        
        cout<<"Case #"<<t<<": "<<max(ot, bt)<<endl;
    }
    
    return 0;
}
