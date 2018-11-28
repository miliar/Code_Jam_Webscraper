#include <iostream>
#include <set>
using namespace std;

set <pair <int, int> > st;

int shift(int x, int ten) {
    return ten * (x % 10) + x / 10;
}

int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        st.clear();
        cerr << tt << '\n';

        int a, b;
        cin >> a >> b;

        long long ans = 0;

        int ten = 1, len = 0;
        for (int aa = a; aa >= 10; aa /= 10, ten *= 10, ++len) ;
        for (int i = a; i < b; ++i) {
            int x = i;
            for (int j = 0; j < len; ++j) {
                x = shift(x, ten);
                if (x > i && x <= b && st.find(make_pair(i, x)) == st.end()) {
                    ++ans;
                    st.insert(make_pair(i, x));
                }
            }
        }

        cout << "Case #" << tt << ": " << ans << '\n';
    }

    return 0;
}
