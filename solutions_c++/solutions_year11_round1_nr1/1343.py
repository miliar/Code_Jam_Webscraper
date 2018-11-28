#include <iostream>
#include <cassert>

using namespace std;

int maxfactor(int a, int b) {
    if (a == b) {
        return a;
    }

    // a >= b
    if (a < b) {
        int c = a;
        a = b;
        b = c;
    }
    assert(b > 0);
    if (b == 1) {
        return 1;
    }
    if (b % a == 0) {
        return b;
    }

    return maxfactor(a-b, b);
}

int main()
{
    int coden, t;
    cin >> t;
    //cerr << t << endl;
    // define vars
    int n, pd, pg;
    int maxfac;

    for (coden = 1; coden <= t; coden++)
    {
        cerr << coden << '-' << t << endl;
        cin >> n >> pd >> pg;

        // output result
        cout << "Case #" << coden << ": ";
        if (pd < 100 && pg == 100) {
            cout << "Broken";
        } else if (pd > 0 && pg == 0) {
            cout << "Broken";
        } else if (pd == 0) {
            cout << "Possible";
        } else {
            maxfac = maxfactor(pd, 100);
            cerr << "maxfactor of " << pd << " and 100 is:" << maxfac << endl;

            // if n < (100 / maxfac) then impossible
            if (n < (100 / maxfac)) {
            cout << "Broken";
            } else  {
            cout << "Possible";
            }
        }
        cout << endl;
    }
    return 0;
}

