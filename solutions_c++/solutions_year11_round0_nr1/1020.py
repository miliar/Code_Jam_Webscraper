#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t;
    cin >> t;

    for(int z = 1; z <= t; z++) {
        int n;
        cin >> n;

        int last_time[2] = {0, 0}, last_pos[2] = {1, 1}, cur_time = 0;
        for(int i = 0; i < n; i++) {
            char player; int pos;
            cin >> player >> pos;

            bool p1 = player == 'O';
            cur_time = max(cur_time, abs(last_pos[p1] - pos) + last_time[p1]) + 1;
            last_time[p1] = cur_time;
            last_pos[p1] = pos;
        }

        cout << "Case #" << z << ": " << cur_time << endl;
    }

}
