#include <iostream>
#include <string>
using namespace std;

int gcd(int pd, int pg)
{
    while (pd && pg) {
        if (pd > pg) {
            pd %= pg;
        } else {
            pg %= pd;
        }
    }
    return pd + pg;
}

bool solve(long long n, int pd, int pg)
{
    if (pd != 0 && pg == 0) {
        return false;
    } else if (pd == 0 && pg == 0) {
        return true;
    } else if (pd != 100 && pg == 100) {
        return false;
    }
    int t = pd / gcd(pd, 100);
    return 100 * t / pd <= n;
}

int main()
{
    int tests;
    cin >> tests;
    for (int test = 0; test < tests; ++test) {
        long long n;
        int pd, pg;
        cin >> n >> pd >> pg;
        cout << "Case #" << (test + 1) << ": " << (solve(n, pd, pg) ? "Possible" : "Broken") << endl;
    }
}
