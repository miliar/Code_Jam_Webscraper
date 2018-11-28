#include<iostream>
#include<cstdio>
using namespace std;

int n, dis, d[10010], l[10010], f[10010];

void input() {
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> d[i] >> l[i];
    cin >> dis;
}

bool getans() {
    fill_n(f, n, dis);
    f[0] = 0;
    for (int i = 0; i < n; i++) {
        int mx = min(2 * d[i] - f[i], d[i] + l[i]);
        if (mx >= dis) return true;
        for (int j = i + 1; j < n and d[j] <= mx; j++)
            f[j] = min(f[j], d[i]);
    }
    //for (int i = 0; i < n; i++)
    //    cout << f[i] << " ";
    //cout << endl;
    return false;
}

void work() {
    bool answer = getans();
    if (answer) cout << "YES";
    else        cout << "NO";
}


int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int kase;
    cin >> kase;
    for (int i = 1; i <= kase; i++) {
        cout << "Case #" << i << ": ";
        input();
        work();
        cout << endl;
    }
}
