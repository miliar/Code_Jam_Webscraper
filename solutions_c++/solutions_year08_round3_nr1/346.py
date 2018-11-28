#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<long> vl;

int main() {
    int N;
    cin >> N;
    for (int i=1; i<=N; ++i) {
        long P, K, L;
        cin >> P >> K >> L;
        vl v(L);
        for (int j=0; j<L; ++j) {
            long f;
            cin >> f;
            v[j] = f;
        }
        if (P*K<L) {
            cout << "Impossible" << endl;
            continue;
        }
        sort(v.begin(), v.end(), greater<long>());
        long res = 0;
        for (int j=0; j<L; ++j) {
            res += v[j]*(1 + j/K);
        }
        cout << "Case #" << i << ": " << res << endl;
    }
}
