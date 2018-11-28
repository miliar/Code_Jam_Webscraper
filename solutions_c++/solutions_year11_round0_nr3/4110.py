#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int cases;
    cin >> cases;

    for (int i = 0; i < cases; ++i) {
        int n;
        cin >> n;
        
        vector<int> all;
        int t;
        int result = 0;
        int sum = 0;

        for (int j = 0; j < n; ++j) {
            cin >> t;
            result ^= t;
            sum += t;
            all.push_back(t);
        } 

        if (result == 0) {
            sort(all.begin(), all.end());
            cout << "Case #" << i+1 << ": " << sum-all[0] << endl;
        }
        else {
            cout << "Case #" << i+1 << ": NO" << endl;
        }
    }

    return 0;
}
