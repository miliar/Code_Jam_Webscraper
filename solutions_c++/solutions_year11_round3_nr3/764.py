#include <iostream>
#include <algorithm>
using namespace std;
int a[10100];
int T;
int n;
long long l,h;
long long gcd(long long a,long long b){
    if(a) return gcd(b%a,a);
    return b;
}
int check(int x){
    for(int i = 0;i < n;++i)
        if(a[i] % x && x % a[i]) return 0;
    return 1;
}
int main(){
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    cin >> T;
    for(int I = 1;I <= T;++I){
        cout << "Case #" << I << ": ";
        cin >> n >> l >> h;
        for(int i = 0;i < n;++i)
            cin >> a[i];
        int ans(0);
        for(int i = l;i <= h;++i){
            if(check(i)){
                cout << i << endl;
                ans = 1;
                break;
            }
        }
        if(!ans)
            cout << "NO" << endl;
    }
}
