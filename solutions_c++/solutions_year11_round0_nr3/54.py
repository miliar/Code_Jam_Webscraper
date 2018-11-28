#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        int N;
        cin >> N;
        int sum = 0;
        int total = 0;
        int min = -1;
        for (int i = 0; i < N; i++) {
            int c;
            cin >> c;
            sum ^= c;
            total += c;
            if (min == -1 || c < min) {
                min = c;
            }
        }
        if (sum == 0) {
            cout << "Case #" << x << ": " << total - min << endl;
        } else {
            cout << "Case #" << x << ": NO" << endl;
        }
    }
}
