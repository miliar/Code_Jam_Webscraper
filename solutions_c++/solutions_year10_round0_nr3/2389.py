#include <iostream>

using namespace std;

int main()
{
    int T, R, k, N;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        cin >> R >> k >> N;
        int groups[N];
        for (int j = 0; j < N; j++) {
            cin >> groups[j];
        }
        int ride = 1;
        int group = 0;
        int cost = 0;
        while (ride <= R) {
            int total = 0;
            int temp = group;
            while (total + groups[group] <= k) {
                total += groups[group];
                if (group == N - 1) group = 0;
                else group++;
                if (group == temp) break;
            }
            cost += total;
            ride++;
        }
        cout << "Case #" << i << ": " << cost << endl;
    }
    return 0;
}
