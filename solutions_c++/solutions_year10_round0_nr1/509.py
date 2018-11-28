#include <iostream>
using namespace std;

int main() {
    int T;
    int x = 0;
    cin >> T;
    while(T--) {
        int N, K;
        cin >> N >> K;
        cout << "Case #" << ++x << ": " << (((K + 1) % (1 << N)) ? "OFF" : "ON") << endl;
    }
}

