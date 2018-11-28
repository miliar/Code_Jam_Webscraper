#include <iostream>
using namespace std;

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    
    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        int n;
        cin >> n;
        int o = 1, b = 1, to = 0, tb = 0;
        while (n--) {
            char ch;
            int x;
            cin >> ch >> x;
            if (ch == 'O') {
                to += abs(x - o) + 1;
                if (to <= tb) to = tb + 1;
                o = x;
            }else {
                tb += abs(x - b) + 1;
                if (tb <= to) tb = to + 1;
                b = x;
            }
        }
        cout << "Case #" << t2 << ": " << (tb > to ? tb : to) << endl;
    }
    
    return 0;
}
