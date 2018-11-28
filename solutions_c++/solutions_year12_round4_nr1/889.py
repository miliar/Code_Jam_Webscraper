#include <iostream>
#include <algorithm>

using namespace std;

long long d[10005], l[10005];
int N;
long long D;

// bool solve() {
//     long long r = 2 * d[0];
//     int prev = 0;
//     int i = 1;
//     long long ma = 0;
//     int mi = 0;
//         // cout << r << endl;
//     while(true) {
//         bool stop = true;
//         if (r >= D) {
//             cout << "YES" << endl;
//             return;
//         }
//         while(i < N && d[i] <= r) {
//             if (ma < d[i]+min(l[i], d[i] - d[prev])) {
//                 ma = d[i] + min(l[i], d[i] - d[prev]);
//                 mi = i;
//             }
//             ++i;
//             stop = false;
//         }
//         if (stop) {
//             cout << "NO" << endl;
//             return;
//         }
//         prev = mi;
//         r = ma;
//         if (i == N) {
//             if (r >= D) {
//                 cout << "YES" << endl;
//             }
//             else
//                 cout << "NO" << endl;
//             return;
//         }
//         ma = d[i];
//     }
// }

bool solve(int i, int b) {
    int r = d[i] + b;
    if (r >= D)
        return true;
    int j = i+1;
    while (j < N && d[j] <= r) {
        // cout << "solve " << j << ' ' << min(l[j], d[j]-d[i]) << endl;
        if (solve(j, min(l[j], d[j]-d[i])))
            return true;
        ++j;
    }
    return false;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        for (int n = 0; n < N; ++n) {
            cin >> d[n] >> l[n];
        }
        cin >> D;
        cout << "Case #" << t << ": ";
        if (solve(0, d[0]))
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
}