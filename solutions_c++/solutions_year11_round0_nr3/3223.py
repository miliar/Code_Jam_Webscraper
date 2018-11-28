#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int t; cin >> t;
    for (int cas=1;cas<=t;++cas) {
        int n; cin >> n;
        vector<int> v(n);
        for (int i=0;i<n;++i) cin >> v[i];
        int ans = -1;
        for (int i=1;i<(1<<n)-1;++i) {
            int a1=0,a2=0,b=0; //a suma XOR de "1", b suma bona de "0"
            for (int k=0;k<n;++k) {
                if ((i>>k)&1) a1^=v[k];
                else {
                    a2^=v[k];
                    b+=v[k];
                }
            }
            if (a1==a2) ans=max(ans,b);
        }
        cout << "Case #" << cas << ": ";
        if (ans==-1) cout <<"NO"<<endl;
        else cout << ans << endl;
    } 
}
