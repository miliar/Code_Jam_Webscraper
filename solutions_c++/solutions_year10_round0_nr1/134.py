#include <iostream>
using namespace std;

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);

    int t1, n, k;
    cin >> t1;
    for (int t2 = 1; t2 <= t1; ++t2) {
        cin >> n >> k;
        printf("Case #%d: ", t2);
        n = 1 << n;
        cout << (k % n == n - 1 ? "ON" : "OFF") << endl;
    }
    
    return 0;
}
