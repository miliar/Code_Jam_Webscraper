#include <vector>
#include <list>
#include <map>
#include <queue>
#include <iostream>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <ctime>
using namespace std;

typedef long long ll;
inline ll get(void) {
    ll  a;
    scanf("%lld", &a);
    return a;
}

void solve() {
    ll l = get();
    ll t = get();
    ll n = get();
    ll c = get();
    vector<ll> distToNext(n, 0);
    for (int i = 0; i < c; i++) {
        ll a = get();
        for (int k = 0; k*c+i+1 <= n; k++) {
            distToNext[k*c+i] = a;
        }
    }
    vector<ll> improve(n, 0);
    vector<bool> boost(n, 0);
    vector< pair<ll, ll> > candy;
    ll x = 0;
    bool canBoost = false;
    for (int i = 0; i < n; i++) {
        if (!canBoost) {
            x += distToNext[i];
            if (x >= t/2) {
                canBoost = true;
                ll nonBoosted = distToNext[i]*2;
                ll boostAmount = x - t/2;
                ll increase = nonBoosted - boostAmount;
                candy.push_back(make_pair(boostAmount, i));
                improve[i] = boostAmount;
            }
        } else {
            candy.push_back(make_pair(distToNext[i], i));
            improve[i] = distToNext[i];
        }
    }
    sort(candy.begin(), candy.end(), greater< pair<ll, ll> >());
    for (int i = 0; i < l; i++) {
        boost[candy[i].second] = true;
    }
    ll res = 0;
    for (int i = 0; i < n ; i++) {
        res += distToNext[i]*2;
        if (boost[i]) {
            res -= improve[i];
        }
    }
    printf("%lld\n", res);

}

int main(void) {
    int tests = get();
    for (int t = 1; t <= tests; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}
