#include <iostream>
#include <cmath>
using namespace std;
long long l,p,c;
int main(){
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    int T;
    cin >> T;
    for(int I = 1;I <= T;++I){
        cin >> l >> p >> c;
        long long tmp(1),x(0),ans(0);
        while(l * tmp * c < p){
            tmp *= c;
            ++x;
        }
        tmp = 1;
        while(tmp <= x){
            tmp *= 2;
            ++ans;
        }
        cout << "Case #" << I << ": " << ans << endl;
    }
}
