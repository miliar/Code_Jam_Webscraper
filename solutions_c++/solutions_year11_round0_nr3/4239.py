#include <iostream>
#include <cassert>
using namespace std;

int main() {
    int N;
    cin >> N;
    for(int t = 0; t < N; t++) {
        int n, c;
        cin >> n >> c;
        int min_c = c;
        int sum = c;
        int chor = c;
        for (int i = 1; i < n; i++) {
            cin >> c;
            chor ^= c;
            sum += c;
            if (c < min_c) min_c = c;
        }

        cout << "Case #" << t + 1 << ": ";

        if (chor != 0) {
            cout << "NO" << endl;
        } else {
            cout << sum - min_c << endl;
        }
    }
    return 0;
}
