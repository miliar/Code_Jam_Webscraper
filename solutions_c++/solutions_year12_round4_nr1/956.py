#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <bitset>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <algorithm>
#include <complex>
#include <functional>
#include <limits>
#include <memory>
#include <numeric>
#include <utility>
#include <iomanip>

using namespace std;
typedef long long Int;

Int ff[10020];

int main() {
    int t; cin >> t;
    for(int x = 1; x <= t; ++x) {
        int n; cin >> n;
        vector<Int> dd(n), ll(n);
        for(auto i = 0; i < n; ++i) {
            cin >> dd[i] >> ll[i];
        }
        Int d;
        cin >> d;
        
        fill(begin(ff), end(ff), 0);
        ff[0] = dd[0];
        for(auto i = 0; i < n; ++i) {
            for(auto j = i + 1; j < n; ++j) {
                if(dd[j] - dd[i] <= ff[i]) {
                    ff[j] = max(ff[j], min(ll[j], dd[j] - dd[i]));
                } else break;
            }
        }
        
        bool y = false;
        for(auto i = 0; i < n; ++i) {
            y |= ff[i] >= d - dd[i];
        }
        cout << "Case #" << x <<": " << (y ? "YES" : "NO") << endl;
    }
}
