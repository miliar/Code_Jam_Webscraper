#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

int dig(int x) {
    int res = 0;
    do {
        ++res;
        x /= 10;
    } while (x > 0);
    return res;
}

int main() {
    int casos;
    cin >> casos;
    vector<int> pot10(9);
    pot10[0] = 1;
    for (int i = 1; i <= 8; ++i) pot10[i] = pot10[i - 1]*10;
    for (int cas = 1; cas <= casos; ++cas) {
        int a, b, res = 0;
        cin >> a >> b;
        int len = dig(b);
        for (int i = a; i <= b; ++i) {
            set<int> v;
            for (int shift = 1; shift < len; ++shift) {
                int x = i/pot10[shift] + i%pot10[shift]*pot10[len - shift];
                if (x < i and x >= a and x <= b) v.insert(x);
            }
            res += v.size();
        }
        cout << "Case #" << cas << ": " << res << endl;
    }
}