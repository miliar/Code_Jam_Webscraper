#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <stack>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#define INF 1000000
typedef long long ll;
typedef unsigned long long llu;
using namespace std;

vector<pair<ll, ll> >::iterator seek(vector<pair<ll, ll> >::iterator first,
                                     vector<pair<ll, ll> >::iterator last,
                                     ll type) {
    for( ; first != last; ++first) {
        if((*first).second == type) break;
    }
    return first;
}

ll ans;

void solve(vector<pair<ll, ll> >::iterator a,
           vector<pair<ll, ll> >::iterator aend,
           vector<pair<ll, ll> >::iterator b,
           vector<pair<ll, ll> >::iterator bend,
           ll cur) {
    if(a == aend) return;

    ll used = 0;
    if((*a).second == (*b).second) {
        if((*a).first >= (*b).first && (*b).first >= 0) used = (*b).first;
        else used = (*a).first;
        cur += used;
        ans = max(ans, cur);
    }

//  cout << (*a).second << ", " << cur << ", " << used << endl;
    vector<pair<ll, ll> >::iterator anext, bnext;
    anext = seek(a+1, aend, (*b).second);
    bnext = seek(b+1, bend, (*a).second);

    (*a).first -= used;
    (*b).first -= used;
    // a をいっこすすめるパターン
    solve(a+1, aend, b, bend, cur);

    // a を捨てて seek するパターン
    solve(anext, aend, b, bend, cur);
    if(bnext != bend) {
        // b を捨てて seek するパターン
        solve(a, aend, bnext, bend, cur);
    }
    (*a).first += used;
    (*b).first += used;
}

int main(void) {
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        int n, m;
        cin >> n >> m;

        vector<pair<ll, ll> > a(n), b(m);
        for(int j = 0; j < n; ++j) {
            cin >> a[j].first >> a[j].second;
        }
        for(int j = 0; j < m; ++j) {
            cin >> b[j].first >> b[j].second;
        }

        ans = 0;
        solve(a.begin(), a.end(), b.begin(), b.end(), 0);
        printf("Case #%d: %llu\n", i, ans);
    }
    return 0;
}
