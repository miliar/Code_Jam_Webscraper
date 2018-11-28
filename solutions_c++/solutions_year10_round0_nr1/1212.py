#include <iostream>

using namespace std;

int main(int argc, char* argv[]) {
    long long K, p;
    int N;
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> N >> K;
        if (N == 0) {
            cout << "Case #" << i << ": OFF" << endl;
        } else {
            p = 1 << N;
            if (K % p == p - 1) {
                cout << "Case #" << i << ": ON" << endl;
            } else {
                cout << "Case #" << i << ": OFF" << endl;
            }
        }
    }
    return 0;
}
