#include <algorithm>
#include <iostream>
using namespace std;

int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        string n;
        cin >> n;
        n = '0' + n;
        next_permutation(n.begin(), n.end());
        if (n[0] == '0')
            cout << n.c_str()+1 << '\n';
        else
            cout << n << '\n';
    }
}
