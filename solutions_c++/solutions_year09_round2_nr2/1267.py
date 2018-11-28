#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;
#define rep(i,n) for (int i = 0; i < n; i++)

int mn;

int main() {
    int T;
    cin >> T;
    rep(i,T) {
        long long n;
        vector<int> hoge;
        cin >> n;
        mn = 999;
        while (n > 0) {
            if (n % 10 > 0) mn = min(mn, (int)(n % 10));
            hoge.push_back(n % 10);
            n /= 10;
        }
        reverse(hoge.begin(), hoge.end());
        cout << "Case #" << i+1 << ": ";
        if (next_permutation(hoge.begin(), hoge.end())) {
            rep(i,hoge.size()) cout << hoge[i];
            cout << endl;
        } else {
            sort(hoge.begin(), hoge.end());
            cout << mn;
            cout << 0;
            bool fin = false;
            rep(i,hoge.size()) {
                if (!fin && hoge[i] == mn) {
                    fin = true;
                    continue;
                }
                cout << hoge[i];
            }
            cout << endl;
        }
    }
    return 0;
}