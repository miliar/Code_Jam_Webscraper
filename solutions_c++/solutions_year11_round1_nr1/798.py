#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <math.h>
using namespace std;

#define FOR(i,s,e) for (int i = int(s); i != int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
typedef pair<int, int> P;

string gcjMain() {
    long long int N_, pg, pd;
    scanf("%lld %lld %lld\n", &N_, &pd, &pg);

    if ((pd == 100 && pg == 100) || (pd == 0 && pg == 0))
        return "Possible";
    if (pg == 0 && pd != 0)
        return "Broken";
    if (pg == 100 && pd != 100)
        return "Broken";
    if (N_ >= 100)
        return "Possible";
    if (N_ >= 50) {
        if (pd % 2 == 0)
            return "Possible";
    }
    if (N_ >= 25) {
        if (pd % 4 == 0)
            return "Possible";
    }
    if (N_ >= 20) {
        if (pd % 5 == 0)
            return "Possible";
    }
    if (N_ >= 10) {
        if (pd % 10 == 0)
            return "Possible";
    }
    if (N_ >= 5) {
        if (pd % 20 == 0)
            return "Possible";
    }
    if (N_ >= 4) {
        if (pd % 25 == 0)
            return "Possible";
    }
    if (N_ >= 2) {
        if (pd % 50 == 0)
            return "Possible";
    }
    if (N_ >= 1) {
        if (pd % 100 == 0)
            return "Possible";
    }

    return "Broken";
}

int main(void) {
    int n;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; ++i) {
        printf("Case #%d: %s\n", i, gcjMain().c_str());
    }
}

