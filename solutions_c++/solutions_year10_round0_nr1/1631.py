#include <cstdio>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
    int z;
    long long n, k, m;
    cin >> z;
    for(int ca = 1; ca <= z; ++ ca) {
        cin >> n >> k;
        m = 1 << n;
        k %= m;
        cout << "Case #" << ca << ": ";
        if(k == m-1) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
    return 0;
}
