#include <iostream>

using namespace std;

typedef long long ll;

int main(int argc, char* argv[]) {
    int T;
    int N;
    ll k;
    ll R;
    ll* a;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cin >> R >> k >> N;
        a = new ll[N];
        for (int j = 0; j < N; ++j) {
            cin >> a[j];
        }
        int n = 0;
        ll sub = 0;
        for (ll r = 0; r < R; ++r) {
            ll sum = 0;
            int start = n;
            while (sum + a[n] <= k) {
                sum += a[n];
                n = (n + 1) % N;
                if (n == start) break;
            }
            sub += k - sum;
            //cout << "n = " << n << ", k - sum = " << k - sum << endl;
        }
        cout << "Case #" << i << ": " << R * k - sub << endl;
    }
    return 0;
}

