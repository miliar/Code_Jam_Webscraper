#include <iostream>
using namespace std;

int main() {
    int N, T, S, P, ans;
    int tmp, tmpmod;
    cin >> T;
    for (int a=1; a<=T; a++) {
        ans=0;
        cin >> N >> S >> P;
        for (int i=0; i<N; i++) {
            cin >> tmp;
            if (tmp==0) {
               if (P==0) ans++;
            } else {
                tmpmod = tmp%3;
                tmp = tmp/3;
                if (tmpmod==0) {
                   if (tmp>=P) {
                       ans++;            
                   } else if (tmp+1>=P) {
                       if (S>0) {
                           ans++;
                           S--;            
                       }      
                   }       
                } else if(tmpmod==1) {
                   if (tmp>=P-1) {
                       ans++;            
                   }   
                } else if(tmpmod==2) {
                    if (tmp>=P-1) {
                       ans++;            
                   } else if (tmp+1>=P-1) {
                       if (S>0) {
                           ans++;
                           S--;            
                       }      
                   }   
                }
            }   
        }
        cout << "Case #" << a << ": " << ans << endl;
    }
}
