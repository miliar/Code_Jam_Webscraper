#include <iostream>
#include <limits>
using namespace std;

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        int n;
        cin >> n;
        int m = numeric_limits<int>::max(), s = 0, x = 0, t;
        for (int i = 0; i < n; ++i) {
            cin >> t;
            m = min(m, t);
            s += t;
            x ^= t;
        }
        if (x != 0) {
            cout << "Case #" << (test + 1) << ": NO" << endl;
        } else {
            cout << "Case #" << (test + 1) << ": " << (s - m) << endl;
        }
    }
}
