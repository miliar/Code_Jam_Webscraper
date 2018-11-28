#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>

#define mp make_pair

using namespace std;

typedef long long ll;

ll n, w, h;
pair<int, int> a[1024];
ll rx[1024], ry[1024];

int fit(int from, int l, int t, int r, int b) {
    if (from == n) return from;
    int d = a[from].first;
    int nl = l - d * (l == 0);
    int nr = r + d * (r == w);
    int nt = t - d * (t == 0);
    int nb = b + d * (b == h);
    int nw, nh;
    nw = nr - nl;
    nh = nb - nt;
    if (2*d > nw || 2*d > nh) return from;
    int x, y;
    x = nl + d;
    y = nt + d;
    int num = a[from].second;
    rx[num] = x;
    ry[num] = y;
    int res = from+1;
    if (2*d < nw) {
        res = fit(res, x+d, y, r, min(b, y+d));
    }
    if (2*d < nh) {
        res = fit(res, l, y+d, r, b);
    }
    return res;
}

int main() {
    int i, j;
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int NT, T;
    cin>>NT;
    for(T=1; T<=NT; ++T) {
        cin>>n>>w>>h;
        for(i=0; i<n; ++i) {
            cin>>a[i].first;
            a[i].second = i;
        }
        sort(a, a+n);
        reverse(a, a+n);
        if (fit(0, 0, 0, w, h) < n) {
            cout<<"ERROR!"<<endl;
            return 0;
        }
        cout<<"Case #"<<T<<": "<<rx[0]<<" "<<ry[0];
        for(i=1; i<n; ++i) {
            cout<<" "<<rx[i]<<" "<<ry[i];
        }
        cout<<endl;
    }
    return 0;
}


