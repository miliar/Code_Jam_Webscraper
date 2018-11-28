#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <iomanip>
#include <sstream>
#include <stack>

using namespace std;

void solve() {
    long long n;
    cin >> n;
    vector<long long> x(n-1), r(n);
    stack<long long> st,height;
    for (int i=0; i<n-1; i++) {
        cin >> x[i];
        x[i]--;
    }
    long long a = 0;
    for (long long i=0; i<n-1; i++) {
        if (!st.empty() && st.top() == i) {
            r[i] = height.top();
            st.pop();
            height.pop();
            a--;
            if (st.empty()) {
                r[i] = 100000000;
                st.push(x[i]);
                height.push(100000000);
                a++;
            }
            continue;
        }
        if (st.empty()) {
            r[i] = 100000000;
            st.push(x[i]);
            height.push(100000000);
            a++;
        } else {
            if (st.top() < x[i]) {
                cout << "Impossible" << endl;
                return;
            } else if (st.top() > x[i]) {
                height.push(height.top() - (st.top() - x[i]) * a);
                st.push(x[i]);
                r[i] = height.top() - (x[i] - i) * a;
                a++;
            } else {
                r[i] = height.top() - (x[i] - 1) * (a - 1) - 1;
            }
        }
    }
    r[n-1] = height.top();
    for (int i=0; i<n; i++) cout << r[i] << " ";
    cout << endl;
}

int main() {
    int n;
    cin >> n;
    for (int i=0; i<n; i++) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}
