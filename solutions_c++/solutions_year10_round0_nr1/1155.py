#include <iostream>

using namespace std;

unsigned snaper (unsigned long long N, unsigned long long K) {
    return ((K & ((1 << N) - 1)) + 1) >> N;
}

int main (int argc, char *argv[]) {
    static const char *state[] = {"OFF", "ON"};
    unsigned T;
    cin >> T;
    for (unsigned i = 0; i < T; ++i) {
        unsigned long long N, K;
        cin >> N >> K;
        unsigned st = snaper(N, K);
        cout << "Case #" << (i+1) << ": " << state[st] << endl;
    }
    return 0;
}
