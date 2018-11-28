#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <tr1/unordered_map>

using namespace std;
using namespace tr1;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

typedef long long ll;

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        int n; scanf("%d", &n);

        int txor = 0;
        ll mn = 1ll << 60;
        ll sum = 0;

        rep(i, n) {
            ll x; cin >> x;
            txor ^= x;
            mn = min(mn, x);
            sum += x;
        }

        if(txor != 0) cout << "NO" << endl;
        else cout << sum - mn << endl;

    }
}
