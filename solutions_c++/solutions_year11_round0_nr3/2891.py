#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    cin >> n;
    for(int tcs = 1; tcs <= n; ++tcs) {
        cout << "Case #" << tcs << ": ";
        int m, num, p = 0, t = 0;
        vector<int> E;
        cin >> m;
        for(int i = 0; i < m; ++i) {
            cin >> num;
            E.push_back(num);
            p ^= num;
            t += num;
        }
        if(p) {
            cout << "NO" << endl;
        } else {
            sort(E.begin(), E.end());
            cout << t - E[0] << endl;
        }
    }
    return 0;
}
