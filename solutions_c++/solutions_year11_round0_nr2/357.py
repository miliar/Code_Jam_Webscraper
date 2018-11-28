#include <iostream> 
#include <vector> 
#include <string> 
#include <math.h> 
#include <algorithm>
#include <set> 
#include <map> 

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
        int c;
        cin >> c;
        map<string, string> combine;
        for (int i = 0; i < c; ++i) {
            string s;
            cin >> s;
            combine[s.substr(0, 2)] = s.substr(2);
            swap(s[0], s[1]);
            combine[s.substr(0, 2)] = s.substr(2);
        }
        int d;
        cin >> d;
        set<string> opposed;
        for (int i = 0; i < d; ++i) {
            string s;
            cin >> s;
            opposed.insert(s);
            reverse(all(s));
            opposed.insert(s);
        }
        int n;
        cin >> n;
        string s;
        cin >> s;
        vector<string> ans;
        for (int i = 0; i < n; ++i) {
            if (sz(ans) == 0) {
                ans.pb(s.substr(i, 1));
                continue;
            }
            if (combine.find(ans[sz(ans) - 1] + s.substr(i, 1)) != combine.end()) {
                 ans[sz(ans) - 1] = combine[ans[sz(ans) - 1] + s.substr(i, 1)];
                 continue;
            }
            for (int j = 0; j < sz(ans); ++j)
                if (opposed.find(ans[j] + s.substr(i, 1)) != opposed.end()) {
                    ans.clear();
                    break;
                }
            if (sz(ans) > 0) {
                ans.pb(s.substr(i, 1));
            }
        }
        
        cout << "Case #" << test + 1 << ": [";
        if (sz(ans) > 0)
            cout << ans[0];
        for (int i = 1; i < sz(ans); ++i)
            cout << ", " << ans[i];
        cout << "]" << endl;
    }
    return 0;
}
