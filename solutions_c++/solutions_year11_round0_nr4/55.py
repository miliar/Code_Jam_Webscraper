#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        int N;
        cin >> N;
        vector<int> A;
        for (int i = 0; i < N; i++) {
            int a;
            cin >> a;
            A.push_back(a - 1);
        }
        int y = 0;
        vector<bool> M(N, true);
        for (int i = 0; i < N; i++) {
            if (M[i]) {
                int cycle_len = 0;
                int p = i;
                do {
                    M[p] = false;
                    cycle_len++;
                    p = A[p];
                } while (M[p]);
                if (cycle_len != 1) {
                    y += cycle_len;
                }
            }
        }
        cout << "Case #" << x << ": " << y << ".000000" << endl;
    }
}
