#include <iostream>
using namespace std;

int main()
{
    freopen("d2.in", "r", stdin);
    freopen("d2.out", "w", stdout);

    int t1;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        int n;
        cin >> n;
        int ret = 0;
        for (int i = 1; i <= n; ++i) {
            int x;
            cin >> x;
            if (x != i) ++ret;
        }
        cout << "Case #" << t2 << ": " << ret << ".000000" << endl;
    }
    
    return 0;
}
