#include <iostream> 
#include <vector> 
#include <string> 
#include <math.h> 
#include <algorithm> 

#define sz(x) ((int)x.size()) 
#define all(x) (x).begin(), (x).end() 
#define pb(x) push_back(x) 
#define mp(x, y) make_pair(x, y) 

typedef long long int64; 

using namespace std;

int _abs(int x) {
    if (x < 0)
        return -x;
    return x;
}

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        int n;
        cin >> n;
        vector<int> a;
        vector<int> b1, b2;
        for (int i = 0; i < n; ++i) {
            string s;
            cin >> s;
            int x;
            cin >> x;
            if (s == "O") {
                b1.pb(x);
                a.pb(1);
            } else {
                b2.pb(x);
                a.pb(2);
            }    
        }
        vector <int> times1(sz(b1), 0), times2(sz(b2), 0);
        if (sz(b1) > 0)
            times1[0] = b1[0] - 1;
        for (int i = 1; i < sz(b1); ++i)
            times1[i] = _abs(b1[i] - b1[i - 1]);
        if (sz(b2) > 0)
            times2[0] = b2[0] - 1;
        for (int i = 1; i < sz(b2); ++i)
            times2[i] = _abs(b2[i] - b2[i - 1]);
        int ans = 0;
        int gap1 = 0;
        int gap2 = 0;
        int pos1 = 0;
        int pos2 = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] == 1) {
                ans += max(0, times1[pos1] - gap1) + 1;
                gap2 += max(0, times1[pos1] - gap1) + 1;
                gap1 = 0;
                ++pos1;
                continue;
            } 
            ans += max(0, times2[pos2] - gap2) + 1;
            gap1 += max(0, times2[pos2] - gap2) + 1;
            gap2 = 0;
            ++pos2;
        }
        cout << "Case #" << test + 1 << ": " << ans << endl;
    }
    return 0;
}
