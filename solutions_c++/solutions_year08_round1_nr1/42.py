#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int main () {
    int i, j;
    int T, cse=0;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<int> v1, v2;
        int t;
        for (i=0; i<n; i++) {
            cin >> t;
            v1.push_back(t);
        }
        for (i=0; i<n; i++) {
            cin >> t;
            v2.push_back(t);
        }
        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        ll res = 0;
        for (i=0; i<n; i++) {
            res += v1[i]*v2[n-i-1];
        }
        cout << "Case #" << ++cse << ": " << res << endl;
    }

    return 0;
}
