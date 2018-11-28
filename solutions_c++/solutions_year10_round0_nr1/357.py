#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <map>
#include <vector>
#include <set>
#include <queue>
using namespace std;

#define MP make_pair
#define PB push_back
#define SS size()
#define all(x) (x).begin(), (x).end()
#define for0(a,b) for (int a = 0; a < (b); ++a)
#define for1(a,b) for (int a = 1; a < (b); ++a)

typedef long long LL;

#define EPS 1e-7


int main() {
    int t;
    cin >> t;

    for (int icase = 1; icase <= t; icase++) {
        int n, k;
        cin >> n >> k;

        printf("Case #%d: ", icase);
        int mask = (1 << n) - 1;
        if ((mask & k) == mask)
            printf("ON\n");
        else
            printf("OFF\n");
    }

    return 0;
}
