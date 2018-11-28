#include <iostream>

using namespace std;

int T, t, n;

int main() {
    cin >> T;
    for (t = 0; t < T; t++) {
        cin >> n;
        int rows[n], swaps = 0;
        for (int i = 0; i < n; i++) {
            rows[i] = 0;
            for (int j = 0; j < n; j++) {
                char stanje;
                cin >> stanje;
                if (stanje == '1')
                    rows[i] = j;
            }
        }

        for (int i = 0; i < n; i++) {
            if (rows[i] > i) {
                int target = i;
                while (rows[target] > i)
                    target++;
                for (int j = target; j > i; j--) {
                    swap(rows[j], rows[j - 1]);
                    swaps++;
                }
            }
        }

        cout << "Case #" << t + 1 << ": " << swaps << endl;

    }
}
