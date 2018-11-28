#include <iostream>
#include <algorithm>

#define STEP 100

using namespace std;

int N;
int peak[2005];

void solve() {
    int h[2005];
    h[N] = 5e8;
    h[N-1] = 5e8;
    int conv[2005];
    memset(conv, 0, sizeof(conv));
    conv[N] = 1;
    conv[N-1] = 1;
    for (int i = N-2; i > 0; --i) {
        int p = peak[i];
        if (!conv[p]) {
            cout << " Impossible" << endl;
            return;
        }
        conv[i] = true;
        double yl, yu;
        if (p != N) {
            int next = p+1;
            while(!conv[next]) ++next;
            double ml = (h[next]-h[p]) / (next-p);
            yu = ml * (i-p) + h[p];
        }
        if (p != i+1) {
            int prev = p - 1;
            while(!conv[prev]) --prev;
            double mu = (h[p]-h[prev]) / (p-prev);
            yl = int(mu * (i-p) + h[p]);
        }
        // cout << "p: " << p << endl;
        // cout << "i: " << i << endl;
        if (p == N)
            h[i] = (int)yl + STEP;
        else if (p == i+1)
            h[i] = (int)yu - STEP;
        else
            h[i] = int((yl + yu)/2);
        for (int j = i+1; j < p; ++j)
            conv[j] = 0;
    }
    for (int i = 1; i <= N; ++i)
        cout << ' ' << h[i];
    cout << endl;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        for (int n = 1; n < N; ++n) {
            cin >> peak[n];
        }
        cout << "Case #" << t << ":";
        solve();
    }
}