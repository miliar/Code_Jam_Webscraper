#include <iostream>
#include <algorithm>

using namespace std;

int T;
int N, K;

int main() {
    cin >> T;
    int t = 1;
    while (t <= T) {
        cin >> N >> K;
        K %= (1 << N);
        bool res = true;
        for (int i = 0; i < N; i++) {
            res &= ((K & (1 << i)) > 0);
        }
        cout << "Case #" << t << ": ";
        if (res) {
            cout << "ON";
        } else {
            cout << "OFF";
        }
        cout << endl;
        t++;
    }
    return 0;
}

