#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <ctime>
using namespace std;

typedef pair<int, int> pii;

const int MAXN = 1000;

int r[MAXN];
int ind[MAXN];
int used[MAXN];
pii res[MAXN];

int n, W, L;

bool my_comp (const int& i, const int& j) {
    return r[i] > r[j];
}

void recurse(int x, int y, int X, int Y) {
    if (x >= X || y >= Y) return;
    int first = -1;
    for (int i = 0; i < n; ++i) {
        int j = ind[i];
        if (used[j]) continue;
        if (r[j] > X - x && x > 0) continue;
        if (r[j] > Y - y && y > 0) continue;
        first = i;
        break;
    }
    if (first == -1) return;
    int j = ind[first];
    used[j] = 1;
    int a, b;
    if (x == 0) a = x;
    else a = x + r[j] / 2;
    if (y == 0) b = y;
    else b = y + r[j] / 2;
    res[j] = pii(a, b);
    recurse(a + r[j] / 2, y, X, b + r[j] / 2);
    recurse(x, b + r[j] / 2, X, Y);
}

void solve(int test) {
    cin >> n >> W >> L;
    bool swaped = false;
    if (W > L) {
        swap(W, L);
        swaped = true;
    }
    for (int i = 0; i < n; ++i) {
        cin >> r[i];
        r[i] *= 2;
        ind[i] = i;
    }
    sort(ind, ind + n, my_comp);
    memset(used, 0, sizeof used);
    recurse(0, 0, W, L);
    cout << "Case #" << test << ":";
    for (int i = 0; i < n; ++i) {
        int a = res[i].first;
        int b = res[i].second;
        if (swaped) swap(a, b);
        cout << " " << a << " " << b;
    }
    cout << endl;
}

int main() {
    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; ++test) {
        solve(test);
    }
    return 0;
}
