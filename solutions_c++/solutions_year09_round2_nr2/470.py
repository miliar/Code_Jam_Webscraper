#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int t; cin >> t;
    for (int c = 1; c <= t; c++) {
        string n; cin >> n;
        if (!next_permutation(n.begin(), n.end())) {
            //reverse(n.begin(), n.end());
            int pos = n.find_first_not_of('0');
            swap(n[0], n[pos]);
            n = n.substr(0, 1) + "0" + n.substr(1);
        }
        cout << "Case #" << c << ": " << n << '\n';
    }
    return 0;
}
