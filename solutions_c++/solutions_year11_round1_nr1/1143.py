#include <iostream>
using namespace std;

double ep = 0.000001;

double abs(double n) {
    if (n > 0)
        return n;
    else return -n;
}

long long gcd(long long a, long long b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

int main() {
    int cs;
    cin >> cs;
    for (int cc = 1; cc <= cs; cc++) {
        long long n, pd, pg;
        cin >> n >> pd >> pg;
        bool ok = false;
        long long g = gcd(pd, 100);
        if ((pd == 0 || n >= 100 / g) && (pg == 100 ? pd == 100 : true) && (pg == 0 ? pd == 0 : true))
            ok = true;
        cout << "Case #" << cc << ": ";
        if (ok)
            cout << "Possible";
        else cout << "Broken";
        cout << "\n";
    }
}
