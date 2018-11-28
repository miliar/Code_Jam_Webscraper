#include <iostream>
#include <string>
#include <sstream>
#include <cmath>

using namespace std;

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    int n;
    cin >> n;
    
    for (int p=1; p<=n; ++p) {      
        int wb=1, wo=1;
        int pre=-1, cnt=0, ret=0;
        
        int k, w, t; 
        string c;
        
        cin >> k;
        for (int l=0; l!=k; ++l) {
            cin >> c;
            cin >> w; 
                            
            if (c=="B") {
               t=abs(w-wb)+1;
               if (pre!=0) {
                  t=max(1,t-cnt);
                  cnt=0;
               }
               wb=w; cnt+=t;
               ret+=t; pre=0;
            }
            else {
                 t=abs(w-wo)+1;
                 if (pre!=1) {
                    t=max(1,t-cnt);
                    cnt=0;
                 }
                 wo=w; cnt+=t;
                 ret+=t; pre=1;
              }                            
        }
        
        cout << "Case #" << p << ": " <<  ret << endl;
    }
}
