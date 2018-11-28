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
        int a, b; cin >> a >> b;

        int y = 0;
        
        int r = 1;
        while(a >= r * 10) r *= 10;
        for(int i = a; i <= b; ++i) {
            if(i >= r * 10) r *= 10;
            int c = i;
            vector<int> q;
            for(int j = r / 10; j; j /= 10) {
                c = c / 10 + (c % 10) * r;
                if(i < c && c <= b) {
                    q.push_back(c);
                }
            }
            y += distance(begin(q), unique(begin(q), end(q)));
        }
        
        cout << "Case #" << x <<": " << y << endl;
    }
}
