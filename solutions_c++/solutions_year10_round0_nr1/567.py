#include <iostream>
using namespace std;

int main(void)
{
    int no_cases = 0;
    cin >> no_cases;

    for (int c=1; c<= no_cases; ++c) {
        int no_devs = 0;
        long long no_snaps = 0;
        cin >> no_devs;
        cin >> no_snaps;
        /*
        cerr << no_devs << " " << 
            no_snaps << " " << 
            (1 << no_devs) << " " <<
            "comparing " << (no_snaps % (1 << no_devs)) << " == " << (1 << no_devs - 1)<< endl;
        */
        long long pow = 1 << no_devs;

        bool on = false;
        if (no_devs == 0)
            on = true;
        else if (no_snaps > 0 && (no_snaps % pow) == pow - 1)
            on = true;

        cout << "Case #" << c << ": " << (on ? "ON" : "OFF") << endl;
    }
    return 0;
}
