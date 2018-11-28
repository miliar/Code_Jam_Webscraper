#include <iostream>

using namespace std;

int main() {
    int T;
    cin >> T;
    for (int c=1; c<=T; ++c) {
        int N, K;
        cin >> N >> K;
        int m = (1<<N)-1;
        cout << "Case #" << c << ": ";
        if ((K&m) == m) cout << "ON";
        else cout << "OFF";
        cout << "\n";
    }
}
