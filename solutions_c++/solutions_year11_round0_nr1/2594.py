#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <map>
#include <cmath>

#define mp make_pair

using namespace std;

vector<pair<char, int> > v;

int rec(int pos, int f, int s, int t) {
    int i, j;
    if (pos == v.size()) return 0;
    for(i=pos+1; i<v.size(); ++i) {
        if (v[i].first != v[i-1].first) break;
    }
    int r = abs(f - v[pos].second);
    r = max(0, r - t);
    ++r;
    for(j=pos+1; j<i; ++j) {
        r += abs(v[j].second - v[j-1].second) + 1;
    }
    return r + rec(i, s, v[i-1].second, r);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int nt, n, t;
    cin>>nt;
    int i, j;
    char c[4];
    int a;
    for(t=1; t<=nt; ++t) {
        v.clear();
        cin>>n;
        for(i=0; i<n; ++i) {
            cin>>c>>a;
            v.push_back(mp(c[0], a));
        }
        cout<<"Case #"<<t<<": "<<rec(0, 1, 1, 0)<<endl;
    }
    return 0;
}
