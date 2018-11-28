#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    
    int c;
    cin >> c;
    
    for (int p=1; p<=c; ++p) {
        int n;
        cin >> n;
        
        int cnt=0;
        for (int k=1; k<=n; ++k) {
            int s;
            cin >> s;
            if (s!=k) ++cnt;
        }
        
        double ret;
        if (!cnt) ret=0;
        else ret=(double)cnt;
            
        cout << "Case #" << p << ": ";
        printf("%6lf\n",ret);
    }
    
    return 0;
}
