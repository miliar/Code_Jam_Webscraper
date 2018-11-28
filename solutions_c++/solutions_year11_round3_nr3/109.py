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

using namespace std;

#define f(i, a, b) for(int i = a; i < b; i++)
#define rep(i, n)  f(i, 0, n)

int x[100];

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        int n, l, h; cin >> n >> l >> h;
        rep(i, n) cin >> x[i];

        int res = -1;
        for(int k = l; k <= h; k++) {
            int ok = 1;
            rep(i, n) if(k % x[i] != 0 && x[i] % k != 0) {
                ok = 0;
                break;
            }
            if(ok) {
                res = k;
                break;
            }
        }

        if(res == -1) cout << "NO" << endl;
        else cout << res << endl;

    }
}
