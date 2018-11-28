#include<iostream>
using namespace std;

int max(int a, int b) { return (b<a) ? a : b; }
int abs(int a) { return (a < 0) ? -a : a; }
int main() {
    int T;
    cin >> T;
    for (int t=1; t <= T; ++t) {
        int N; cin >> N;
        int po = 1, pb = po, to = 0, tb = to;

        for (; N>0; --N) {
            char col; cin >> col;
            int but; cin >> but;
            if (col == 'B') {
                tb = max(tb + abs(but - pb) + 1, to + 1);
                pb = but;
            } else {
                to = max(to + abs(but - po) + 1, tb + 1);
                po = but;
            }
//            cout << pb << " " << tb << " -- " << po << " " << to << endl;
        }
        cout << "Case #" << t << ": " << max(tb,to) << "\n";
    }
    return 0;
}
