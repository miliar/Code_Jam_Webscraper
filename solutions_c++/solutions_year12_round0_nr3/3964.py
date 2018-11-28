#include <iostream>
#include <cstdio>
#include <string>
#include <memory.h>
#include <set>
#include <algorithm>
#include <map>

using namespace std;

const int maxn = 2 * 1e6 + 15;


string str_to_int(int x) {
    string ans;
    while (x > 0) {
        ans.push_back(x % 10 + '0');
        x /= 10;
    }
    reverse(ans.begin(), ans.end());
    return ans;
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int tests;
    cin >> tests;
    for (int testnum = 1; testnum <= tests; ++testnum) {
        int l, r;
        cin >> l >> r;
        cerr << l << " " << r << endl;
        string sl = str_to_int(l);
        string sr = str_to_int(r);
        int ans = 0;
        for (int i = l; i <= r; ++i) {
            string si = str_to_int(i);
            string si0 = si;
            set<string> all;
            for (int j = 0; j < si.size(); ++j) {
                if (all.find(si) == all.end() && si[0] != '0' && si > si0 && si <= sr) {
                    ans++;
                }
                all.insert(si);
                rotate(si.begin(), si.begin() + 1, si.end());
            }
        }
//        if (testnum == 2)
//            break;
        cout << "Case #" << testnum << ": " << ans << endl;
    }
}
