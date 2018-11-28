#include <iostream>
#include <fstream>
#include <string>

using namespace std;

typedef unsigned long long ulong;

ulong power(ulong base, ulong pwr) {
    ulong ret = 1;
    for (ulong i = 0; i < pwr; i++) {
        ret *= base;
    }
    return ret;
}

int main() {
    ifstream input("A-large.in");
    ofstream output("A-large.out");
    ulong t, n, k;
    input>>t;
    for (ulong i = 0; i < t; i++) {
        input>>n>>k;
        ulong pwred = power(2, n);
        if (k % pwred != pwred - 1) {
            output<<"Case #"<<i + 1<<": OFF"<<endl;
        } else {
            output<<"Case #"<<i + 1<<": ON"<<endl;
        }
    }
}
