#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;
    for (int times = 1; times <= n; ++times) {
        int R, k, N;
        cin >> R >> k >> N;
        vector<int> v(N, 0);
        for (int i = 0; i < N; ++i) { cin >> v[i]; }

        int euros = 0, next = 0, cur = 0;
        for (int run = 0; run < R; ++run) {
            int ride = 0;
            do {
                ride += v[cur];
                if (ride > k) break;
                euros += v[cur];
                cur = (cur + 1) % N;
            }while (next != cur);
            next = cur;
        }
        cout << "Case #" << times << ": " << euros << '\r' << endl;
    }
    return 0;
}
