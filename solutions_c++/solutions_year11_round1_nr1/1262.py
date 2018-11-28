#include <iostream>
using namespace std;

int gcd(int a, int b)
{
    if (a == 0)
        return b;
    return gcd(b % a, a);
}

int main(void)
{
    int T;
    cin >> T;
    for (int loop = 1; loop <= T; loop++) {
        int n, pd, pg;
        cin >> n >> pd >> pg;
        cout << "Case #" << loop << ": ";
        if (pg == 0 && pd || pg == 100 && pd < 100)
            cout << "Broken" << endl;
        else {
            int k = gcd(pd, 100);
            k = 100 / k;
            if (k <= n)
                cout << "Possible" << endl;
            else
                cout << "Broken" << endl;
        }
    }
    return 0;
}
