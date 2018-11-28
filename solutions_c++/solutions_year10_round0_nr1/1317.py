#include <iostream>
#include <cstring>
#include <stack>
#include <queue>
#include <cstdlib>
#include <vector>
using namespace std;

long long power(long long a) {
    long long ret = 1;
    for (long long i = 0; i < a; i++) {
        ret *= 2;
    }
    return ret;
}

int main (void) {
    long long T;
    cin >> T;
    for (long long i = 0; i < T; i++) {
        long long N, K;
        cin >> N >> K;
        long long p = power(N);
        K %= p;
        if (K == (p - 1)) { cout << "Case #" << i + 1 << ": ON"  << endl; }
        else              { cout << "Case #" << i + 1 << ": OFF"  << endl; }
    }
    return 0;
}
