#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

void solve(int test) {
    int n;
    cin >> n;
    vector<int> vec(n);
    int minn = -1;
    int sum = 0;
    int x = 0;
    for (int i=0; i < n; ++i) {
        cin >> vec[i];
        if (minn == -1 || minn > vec[i]) {
            minn = vec[i];
        }
        sum += vec[i];
        x = x ^ vec[i];
    }
    if (x != 0) {
        cout << "Case #" << test << ": NO" << endl;
        return;
    }
    cout << "Case #" << test << ": " << sum - minn << endl;
}

int main() {
    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; ++test) {
        solve(test);
    }
    return 0;
}
