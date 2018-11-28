#include <iostream>
#include <cstdio>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

struct node {
    int id, t, p;

    bool operator < (const node& other) const {
        int left = p * other.t;
        int right = other.p * t;
        if (left != right) return left > right;
        return id < other.id;
    }
};

void solve() {
    int n;
    cin >> n;
    vector<node> v(n);

    for (int i = 0; i < n; i++) {
        v[i].id = i;
        cin >> v[i].t;
    }
    for (int i = 0; i < n; i++)
        cin >> v[i].p;

    sort(v.begin(), v.end());

    static int test;
    cout << "Case #" << ++test << ":";
    for (int i = 0; i < n; i++)
        cout << ' ' << v[i].id;
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--)
        solve();
    return 0;
}
