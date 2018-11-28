#include <algorithm>
#include <vector>
#include <iostream>
#include <iterator>
#include <functional>
#include <numeric>
using namespace std;

template<typename _T>
struct f : public binary_function<pair<_T, _T>, pair<_T, _T>, _T> {
    pair<_T, _T> operator() (pair<_T, _T> const& a, _T const& b) {
        return pair<_T, _T>(a.first + b, a.second ^ b);
    }
};

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        vector<int> values;
        int n;

        cin >> n;
        values.reserve(n);

        while (n--) {
            int x; 
            cin >> x;

            values.push_back(x);
        }

        sort(values.begin(), values.end());

        pair<int, int> sx =
            accumulate(values.begin()+1, values.end(), pair<int, int>(0, 0), 
                       f<int>());

        cout << "Case #" << i << ": ";

        if (sx.second == values[0])
            cout << sx.first;
        else
            cout << "NO";

        cout << '\n';
    }

    return 0;
}
