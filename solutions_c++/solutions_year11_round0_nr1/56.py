#include <algorithm>
#include <cstdlib>
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        int N;
        cin >> N;
        // 0: blue, 1: orange
        int pos[2] = {1, 1};
        int time[2] = {0, 0};
        for (int i = 0; i < N; i++) {
            char R;
            int P;
            cin >> ws >> R >> P;
            int me = (R == 'B') ? 0 : 1;
            int other = (R == 'B') ? 1 : 0;
            time[me] += abs(P - pos[me]);
            time[me] = max(time[me], time[other]);
            time[me] += 1;
            pos[me] = P;
        }
        int y = max(time[0], time[1]);
        cout << "Case #" << x << ": " << y << endl;
    }
}
