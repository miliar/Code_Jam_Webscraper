#include <iostream.h>
#include <math.h>

int main() {
    unsigned int n, k, t, r, res, first, sits;
    unsigned int g[1001];

    cin >> t;

    for(unsigned int i = 0; i < t; i++) {
        res = 0;
        first = 0;
        cin >> r >> k >> n;
        for(int j = 0; j < n; j++) {
            cin >> g[j];
        }
        for(int run = 0; run < r; run++) {
            sits = k;
            for(int j = 0; sits >= g[first % n] && j < n; sits -= g[first++ % n], j++);
            res += k - sits;
        }

        cout << "Case #" << i+1 << ": " << res << "\n";
    }

    return 0;
}
