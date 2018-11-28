#include <iostream>
#include <cmath>

using namespace std;

//typedef vector<bitset> bv;

void doCase(int caseNum) {
    int L, P, C;

    cin >> L >> P >> C;

    double f = (double) P / (double) L;

    // Logc(f)
    double flog = log10(f) / log10(C);

    // Log2(flog)
    double ans = log10(flog) / log10(2);

    long realans = (long) ceil(ans);

    if (realans < 0) realans = 0;

    cout << "Case #" << caseNum << ": " << realans << endl;
}

int main() {
    int T;

    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i+1);
    }
}
