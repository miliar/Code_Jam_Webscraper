#include <iostream>
using namespace std;
int x[100],v[50];
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T,n,k,b,t;
    cin >> T;
    for(int I = 1;I <= T;++I){
        cout << "Case #" << I << ": ";
        cin >> n >> k >> b >> t;
        for(int i = 0;i < n;++i)
            cin >> x[i];
        for(int i = 0;i < n;++i)
            cin >> v[i];
        int ans(0),cur(0);
        for(int i = n-1;i >= 0 && cur < k;--i){
            if((b - x[i]) <= v[i] * t){
                ++cur;
                continue;
            }
            ans += k - cur;
        }
        if(cur == k) cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}
