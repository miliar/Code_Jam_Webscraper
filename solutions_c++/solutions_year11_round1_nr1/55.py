#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <iterator>
#include <utility>

using namespace std;

typedef __int64 Int;

Int gcd(Int a, Int b) {
    return !b ? a : gcd(b, a % b);
}

bool solve(Int n, Int pd, Int pg) {
    if (pg == 0) {
        if (pd == 0) {
            return true;
        } else {
            return false;
        }
    }

    if (pg == 100) {
        if (pd == 100) {
            return true;
        } else {
            return false;
        }
    }

    if (pd == 0) {
        return true;
    }

    if (pd == 100) {
        return true;
    }

    Int q = gcd(pd, 100);
    if ((100 / q) > n) {
        return false;
    } else {
        return true;
    }
}

int main() {
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int numTests;
    cin >> numTests;
    for (int t = 1; t <= numTests; ++t) {
        Int n, pd, pg;
        cin >> n >> pd >> pg;
        cout << "Case #" << t << ": " << (solve(n, pd, pg) ? "Possible" : "Broken") << endl;
    }
    
    return 0;
}