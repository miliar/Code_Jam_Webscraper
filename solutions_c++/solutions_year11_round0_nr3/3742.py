#include <cstdlib>
#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    long long testN;
    cin >> testN;
    for (long long test = 1; test <= testN; ++test) {
        long long N;
        cin >> N;
        long long true_sum = 0;
        long long xor_sum = 0;
        long long min_c = 0;
        for (long long i = 0; i < N; ++i) {
            long long c;
            cin >> c;
            if (!min_c || c < min_c) min_c = c;
            xor_sum ^= c;
            true_sum += c;
        }
        cout << "Case #" << test << ": ";
        if (xor_sum)
            cout << "NO" << endl;
        else
            cout << true_sum - min_c << endl;
    }
    return 0;
}

