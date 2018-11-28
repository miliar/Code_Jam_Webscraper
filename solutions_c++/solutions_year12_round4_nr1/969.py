#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> VI;

int main() {
    int casos;
    cin >> casos;
    for (int cas = 1; cas <= casos; ++cas) {
        int n;
        cin >> n;
        VI d(n), len(n);
        for (int i = 0; i < n; ++i) cin >> d[i] >> len[i];
        VI best(n, 0);
        best[0] = d[0];
        int dist;
        cin >> dist;
        bool ok = false;
        if (dist - d[0] <= best[0]) ok = true;
        for (int i = 1; i < n; ++i) {
            for (int j = 0; j < i; ++j) {
                if (d[i] - d[j] <= best[j]) best[i] = max(best[i], min(len[i], d[i] - d[j]));
            }
            if (dist - d[i] <= best[i]) ok = true;
        }
        cout << "Case #" << cas << ": " << (ok?"YES":"NO") << endl;
    }
}