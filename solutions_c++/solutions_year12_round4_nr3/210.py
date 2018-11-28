#include<iostream>
#include<cassert>
#include<vector>
#include<cstdio>
using namespace std;

//const int maxl = 100;
const int maxl = 1e9 - 1;

int x[2010], n;

void input() {
    cin >> n;
    x[0] = n + 1;
    x[n] = n + 1;
    for (int i = 1; i < n; i++)
        cin >> x[i];
}

int ans[2010];
bool failed;

void calc_max(int i, int j, int k) {
    int x1 = i, x2 = j;
    int y1 = ans[i], y2 = ans[j];
    int x = k;
    assert(x1 != x2);
    ans[k] = (y2 - y1) * (x - x1) / (x2 - x1) + y1 - 1;
    //cout << i <<' ' <<j<<' ' << k << endl;
    //cout << ans[i] <<' ' <<ans[j]<<' ' << ans[k] << endl;
}

//#include"sbl/utility/stl_print.hpp"
//using namespace sbl;
void calc(int i, int j) {
    if (j - i == 1) return;
    vector<int> l(1, i + 1);
    while (x[l.back()] < j)
        l.push_back(x[l.back()]);
    if (x[l.back()] > j) {
        failed = true;
        return;
    }
    //cout << i << ' ' << j << ' ' << l << endl;
    calc_max(i, j, l.back());
    for (int i = (int)l.size() - 2; i >= 0; i--) {
        int next = j;
        if(i+2 < (int)l.size()) next = l[i+2];
        calc_max(l[i + 1], next, l[i]);
    }
    calc(l.back(), j);
    for (int i = (int)l.size() - 2; i >= 0; i--)
        calc(l[i], l[i + 1]);
}

void work() {
    ans[0] = maxl, ans[n + 1] = maxl;
    failed = false;
    calc(0, n + 1);
    if (failed) {
        cout << "Impossible";
    } else {
        for (int i = 1; i <= n; i++)
            cout << ans[i] << " ";
    }
}


int main() {
    freopen("C-large.in", "r", stdin);
    freopen("cccc.out", "w", stdout);
    int kase;
    cin >> kase;
    for (int i = 1; i <= kase; i++) {
        cout << "Case #" << i << ": ";
        input();
        work();
        cout << endl;
    }
}
