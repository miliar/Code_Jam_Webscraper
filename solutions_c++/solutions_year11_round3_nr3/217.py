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

inline int get(void) {
    int a;
    scanf("%d", &a);
    return a;
}

void solve() {
    int n = get();
    int l = get();
    int h = get();
    vector<int> notes;
    for (int i = 0; i < n; i++) {
        int x = get();
        notes.push_back(x);
    }
    for (int x = l; x <= h; x++) {
        bool fail = false;
        for (int i = 0; i < n; i++) {
            if (notes[i] % x != 0 && x % notes[i] != 0) {
                fail = true;
                break;
            }
        }
        if (!fail) {
            printf("%d\n", x);
            return;
        }
    }
    printf("NO\n");
}

int main(void) {
    int tests = get();
    for (int t = 1; t <= tests; t++) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}
