#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
 
using namespace std;

int cc;

int a, b;
int res;

int len(int k) {
    int l = 0;
    while (k > 0) {
        k /= 10;
        l++;
    }
    return l;
}

int foo(int k) {
    int l = len(k), t = 1, rk = k;
    set <int> r;
    for (int i = 1; i < l; i++) t *= 10;
    for (int i = 1; i < l; i++) {
        rk = (rk % 10) * t + (rk / 10);
        if (rk <= k) continue;
        if (rk > k && rk >= a && rk <= b) {
            r.insert(rk);
        }
    }
    return r.size();
}

int main() {
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
    scanf("%d\n", &cc);
    foo(12345);
    for (int cas = 1; cas <= cc; cas++) {
        res = 0;
        for (cin >> a >> b; a <= b; a++) {
            res += foo(a);
        }
        cout << "Case #" << cas << ": " << res << endl;
    }
	return 0;
}