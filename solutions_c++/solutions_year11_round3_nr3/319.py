#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        int N, L, H;
        vector<int> notes;

        cin >> N >> L >> H;
        for (int j = 0; j < N; ++j) {
            int x; cin >> x;
            notes.push_back(x);
        }

        int sol = -1;
        for (int k = L; k <= H; ++k) {
            bool ok = true;
            for (int j = 0; j < N; ++j)
                if (notes[j] % k != 0 && k % notes[j] != 0) {
                    ok = false; break;
                }

            if (ok) {
                sol = k; break;
            }
        }

        cout << "Case #" << i+1 << ": ";
        if (sol == -1) cout << "NO"; else cout << sol;
        cout << endl;
    }

    return 0;
}
