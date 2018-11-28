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

using namespace std;
typedef long long Int;

int main() {
    int t; cin >> t;
    for(int x = 1; x <= t; ++x) {
        vector<int> totals;
        
        int n; cin >> n;
        int s; cin >> s;
        int p; cin >> p;
        for(int i = 0; i < n; ++i) {
            int x; cin >> x;
            totals.push_back(x);
        }
        
        sort(begin(totals), end(totals), greater<int>());
        
        int y = 0;
        for(auto x: totals) {
            if(x >= 28) {
                if(10 >= p) ++y;
            } else if(x == 0) {
                if(0 >= p) ++y;
            } else if(x == 1) {
                if(1 >= p) ++y;
            } else {
                if((x + 2) / 3 >= p) { // non-surprising
                    ++y;
                } else if(s > 0 && (x + 2) / 3 + 1 >= p) { // surprising
                    ++y;
                    --s;
                }
            }
        }
        
        cout << "Case #" << x <<": " << y << endl;
    }
}
