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
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
            --a[i];
        }
        int ans = 0;
        for (int i = 0; i < n; ++i)
            if (a[i] != i)
                ++ans;
        
        cout << "Case #" << test + 1 << ": " << ans  << ".000000" << endl;
        
    }
    return 0;
}
