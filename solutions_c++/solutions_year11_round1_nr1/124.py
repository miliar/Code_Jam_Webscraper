#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0)return a;
    else return gcd(b, a%b);
}

bool solve(long long n, long long pd, long long pg) {
    if (pd == 0) {
        if (pg == 100)return false;
        else return true;
    } else if (pd == 100) {
        if (pg == 0)return false;
        else return true;
    } else {
        if (pg == 100 || pg == 0)return false;
        if (n >= 100/gcd(pd,100))return true;
        else return false;
    }
}

int main() {
    int T;
    cin >> T;
    for (int i=0; i<T; i++) {
        long long n,pd,pg;
        cin >> n >> pd >> pg;
        cout << "Case #" << i+1 << ": ";
        if (solve(n,pd,pg))cout << "Possible" << endl;
        else cout << "Broken" << endl;
    }
    return 0;
}
