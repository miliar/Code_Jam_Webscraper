#include<iostream>
#include<cmath>
#include<algorithm>
using namespace std;

const int maxn = 2000;
int T, n, d;
int x[maxn], h[maxn];
bool flag;

void init() {
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        cin >> x[i];
        x[i]--;
    }
}

bool check() {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < i; j++)
            if (x[j] > i && x[j] < x[i]) {
                return false;
            }
    }
    return true;
}

void solve() {
    if (!check()) {
        cout << "Impossible" << endl;
        return;
    }
    int k;
    h[n - 1] = 100000;
    h[n - 2] = 70000;
    double tmp;
    for (int i = n - 3; i >= 0; i--) {
        if (x[i] == i + 1) {
            tmp = double(h[x[i + 1]] - h[i + 1]) / (x[i + 1]-(i + 1)) * (x[i + 1] - i);
            h[i] = h[x[i + 1]]-(tmp + 20);
            continue;
        }
        for (int j = i + 1; j < n - 1; j++)
            if (x[i] == x[j]) {
                k = j;
                break;
            }
        tmp = double(h[x[i]] - h[k]) / (x[i] - k) * (x[i] - i);
        h[i] = h[x[i]]-(tmp - 10);
    }
    tmp = 0;
    for (int i = 0; i < n; i++)
        if (h[i] < 0 && tmp > h[i]) tmp = h[i];
    for (int i = 0; i < n; i++) h[i] += -tmp + 20;
    for (int i = 0; i < n; i++)
        cout << h[i] << ' ';
    cout << endl;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    cin >> T;
    for (int test = 1; test <= T; test++) {
        cout << "Case #" << test << ": ";
        init();
        solve();
    }
    return 0;
}