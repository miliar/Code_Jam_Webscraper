#include <iostream>
#include <algorithm>
using namespace std;

typedef long long bignum;

bignum gcd(bignum m, bignum n) {
    bignum r;
    while(n != 0) {
        r = m % n;
        m = n;
        n = r;
    }
    return m;
}

int main() {
    int T, N;
    bignum g[1000];
    cin >> T;
    
    for(int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        cin >> N;
        for(int i = 0; i < N; ++i) {
            cin >> g[i];
        }
        sort(g, g + N);
        bignum v = g[1] - g[0];
        for(int i = 2; i < N; ++i) {
            v = gcd(v, g[i] - g[i-1]);
        }
        if(v != 0 && g[0] % v != 0) v = v - g[0] % v;
        else v = 0;

        cout << v << endl;
    }

}
