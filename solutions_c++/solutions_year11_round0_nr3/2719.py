#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    int T; cin >> T;
    for (int t = 0; t < T; t++) {
        cout << "Case #" << t + 1 << ": ";
        int N; cin >> N;
        vector<int> C(N);
        for (int i = 0; i < N; i++) cin >> C[i];
        sort(C.begin(), C.end());
        int result = 0;
        for (int i = 0; i < N; i++) result ^= C[i];
        if (result != 0) {
            cout << "NO" << endl;
            continue;
        }
        int sum = 0;
        for (int i = 1; i < N; i++) sum += C[i];
        cout << sum << endl;
    }
}
