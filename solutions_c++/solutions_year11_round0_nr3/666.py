#include <iostream>
using namespace std;

int main()
{
    freopen("c2.in", "r", stdin);
    freopen("c2.out", "w", stdout);
    
    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        int n;
        cin >> n;
        int s1 = 0, s2 = 0, min = int(1e9);
        while (n--) {
            int x;
            cin >> x;
            s1 ^= x;
            s2 += x;
            if (x < min) min = x;
        }
        cout << "Case #" << t2 << ": ";
        if (s1) cout << "NO" << endl;
        else cout << s2 - min << endl;
    }
    
    return 0;
}
