#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> VI;

int abs(int x) {
    if (x < 0) return -x;
    return x;
}

int main() {
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        int n;
        cin >> n;
        VI robot(n), button(n);
        for (int i = 0; i < n; ++i) {
            char c;
            cin >> c >> button[i];
            --button[i];
            if (c == 'O') robot[i] = 0;
            else robot[i] = 1;
        }
        cout << "Case #" << cas << ": ";
        VI time(2, 0), pos(2, 0);
        for (int i = 0; i < n; ++i) {
            int distance = abs(button[i] - pos[robot[i]]) + 1;
            pos[robot[i]] = button[i];
            if (time[1 - robot[i]] < time[robot[i]] + distance) time[robot[i]] = time[robot[i]] + distance;
            else time[robot[i]] = time[1 - robot[i]] + 1;
        }
        cout << max(time[0], time[1]) << endl;
    }
}