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

int main() {
    int t; cin >> t;
    for(int x = 1; x <= t; ++x) {
        int n; cin >> n;
        
        auto ss = vector<int>(n);
        for(auto i = 0; i < n; ++i) {
            cin >> ss[i];
        }
        sort(begin(ss), end(ss));
        
        auto pp = map<int, pair<vector<int>, vector<int> > >();
        pp[0] = make_pair(vector<int>{}, vector<int>{});
        for(auto i = 0; i < n; ++i) {
            auto s = ss[i];
            auto pp_ = pp;
            for(auto const &p: pp) {
                auto px = p.first;
                auto pl1 = p.second.first; pl1.push_back(s);
                auto pl2 = p.second.second; pl2.push_back(s);
                
                pp_[px - s] = make_pair(pl1, p.second.second);
                pp_[px + s] = make_pair(p.second.first, pl2);
                
                if(px - s == 0 || px + s == 0) break;
            }
            pp = pp_;
        }
                       
        cout << "Case #" << x <<":" << endl;
        auto p0 = pp[0];
        if(p0.first.size() == 0 || p0.second.size() == 0) {
            cout << "Impossible";
        } else {
            for(auto const x: p0.first) cout << x << ' ';
            cout << endl;
            for(auto const x: p0.second) cout << x << ' ';
            cout << endl;
        }
    }
}
