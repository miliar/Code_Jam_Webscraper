#include <iostream>
using namespace std;
const long maxN = 30 + 5, maxM = 100 + 10;

long n, m;
long ans[maxN];

int main(void)
{
              freopen("a2.in", "r", stdin);
              freopen("a2.out", "w", stdout);
        ans[0] = 0;
        for (long i = 1; i <= 30; i++)
                ans[i] = ans[i - 1] + (1 << (i - 1));
        long T;
        cin >> T;
        for (long i = 1; i <= T; i++) {
                cin >> n >> m;
                cout << "Case #" << i << ": " << ((m % (ans[n] + 1) == ans[n]) ? "ON" : "OFF") << endl;
        }
        return 0;
}
