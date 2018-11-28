#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        vector<int> b = a;
        sort(a.begin(), a.end());
        int result = 0;
        for (int i = 0; i < n; ++i) {
            if (a[i] != b[i]) {
                ++result;
            }
        }
        cout << "Case #" << (test + 1) << ": " << result << endl;
    }
}
