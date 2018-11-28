#include <iostream>
using namespace std;
int x[100],v[50];
int main(){
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int T,n,k,b,t;
    cin >> T;
    for(int I = 1;I <= T;++I){
        cout << "Case #" << I << ": ";
        cin >> n >> k >> b >> t;
        for(int i = 0;i < n;++i)
            cin >> x[i];
        for(int i = 0;i < n;++i)
            cin >> v[i];
        int res(0),pass(0);
        for(int i = n-1;i >= 0 && pass < k;--i){
            if((b - x[i]) <= v[i] * t){
                ++pass;
                continue;
            }
            res += k - pass;
        }
        if(pass == k) cout << res << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}
