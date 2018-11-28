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

int main() {
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int t;
    cin >> t;
    for (int test = 0; test < t; ++test) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i)
            cin >> a[i];
        int res = 0;
        for (int i = 0; i < n; ++i)
            res ^= a[i];
        if (res != 0) {
            cout << "Case #" << test + 1 << ": NO" << endl;
            continue;
        }
        int sum = 0;
        for (int i = 0; i < n; ++i)
            sum += a[i];
        int j = 0;
        for (int i = 1; i < n; ++i)
            if (a[j] > a[i])
                j = i;
        cout << "Case #" << test + 1 << ": " << sum - a[j] << endl;
    }
    return 0;
}
