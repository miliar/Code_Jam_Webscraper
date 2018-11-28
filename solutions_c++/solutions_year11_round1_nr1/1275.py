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

typedef long long ll;

int main(){

    int T; scanf("%d", &T); for(int test = 1; test <= T; test++) {

        printf("Case #%d: ", test);

        ll n, pd, pg;
        cin >> n >> pd >> pg;

        int res = 0;

        if(pd == pg) res = 1;
        else if(pg == 0) res = 0;
        else if(pg == 100) res = 0;
        else {

            ll gcd = __gcd(pd, 100ll);
            ll d = 100 / gcd;

            if(d <= n && d > 0) res = 1;
        }

   
        printf("%s\n", res ? "Possible" : "Broken");

    }
}
