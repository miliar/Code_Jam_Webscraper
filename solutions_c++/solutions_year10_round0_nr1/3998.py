#include<iostream>
#include<iomanip>
using namespace std;

int main() {
    long T, N, K; cin >> T;
    for (long i=1; i<=T; i++) {
        cin >> N >> K;
        long b = 1; b <<= N; --b;
        cout << "Case #" << i << ": ";
        if (b == (b & K)) cout << "ON" << endl;
        else cout << "OFF" << endl;
    }
    return 0;
}
