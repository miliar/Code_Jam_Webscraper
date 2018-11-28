#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

using namespace std;

int main() {
    int t, n, k;
    scanf("%d", &t);

    for(int z = 1; z <= t; z++) {
        scanf("%d %d", &n, &k);
        int mask = (1<<n) - 1;
        if((k & mask) == mask)
            printf("Case #%d: ON\n", z);
        else
            printf("Case #%d: OFF\n", z);
    }

    return 0;
}

