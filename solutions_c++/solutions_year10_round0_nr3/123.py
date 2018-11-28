#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
using namespace std;

typedef long long ll;

struct Arc {
    int next;
    ll sum;
};

int R, K, N, g[1000];
ll sg[2001];
Arc a[1000];

ll solve() {
    cin >> R >> K >> N;
    for (int i = 0; i < N; ++i)
        cin >> g[i];
    sg[0] = 0;
    for (int i = 0; i < N * 2; ++i)
        sg[i + 1] = sg[i] + g[i % N];
    if (sg[N] <= K)
        return sg[N] * R;
    for (int i = 0; i < N; ++i) {
        a[i].next = upper_bound(sg + i, sg + i + N, sg[i] + K) - sg - 1;
        a[i].sum = sg[a[i].next] - sg[i];
        a[i].next %= N;
    }
    int p1 = 0, p2 = 0, step = 0;
    ll sum = 0;
    do {
        sum += a[p1].sum;
        p1 = a[p1].next;
        ++step;
        if (step == R)
            return sum;
        p2 = a[a[p2].next].next;
    } while (p1 != p2);
    R -= step;
    int T = 0;
    ll delta = 0;
    do {
        delta += a[p2].sum;
        p2 = a[p2].next;
        ++T;
    } while (p2 != p1);
    sum += delta * (R / T);
    R %= T;
    while (R > 0) {
        sum += a[p1].sum;
        p1 = a[p1].next;
        --R;
    }
    return sum;
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        char* file_name = argv[1];
        int len = strlen(file_name);
        if (strcmp(file_name + len - 3, ".in") == 0)
            file_name[len - 3] = 0;
        freopen((string(file_name) + ".in").c_str(), "r", stdin);
        freopen((string(file_name) + ".out").c_str(), "w", stdout);
    }
    int cc = 0, ccc = 0;
    for (cin >> ccc; cc < ccc; ++cc)
            cout << "Case #" << cc + 1 << ": " << solve() << endl;
    return 0;
}
