#include <iostream>
#include <cmath>

using namespace std;

int main() {
    freopen("C.in","r",stdin);
    freopen("C.out","w",stdout);
    
    int c;
    cin >> c;
    
    for (int p=1; p<=c; ++p) {
        int n;
        cin >> n; 
        
        int tmp=0, sum=0, x=1000000000;
        
        for (int k=1; k<=n; ++k) {
            int s;
            cin >> s;
            
            sum+=s; 
            tmp^=s;
            x=min(x,s);
        }
            
        cout << "Case #" << p << ": ";
        
        if (tmp) cout << "NO";
        else cout << sum-x;
        
        cout << endl;
    }
    
    return 0;
}
