#include <iostream>

using namespace std;

int main()
{
    int nCase;
    cin >> nCase;

    for (int iCase = 1; iCase <= nCase; ++iCase) {

        unsigned N;
        cin >> N;

        unsigned long long ss = 0, ps = 0, m = 0xffffffffffffffffull;
        for (unsigned i = 0; i < N; ++i) {
            unsigned long long Ci;
            cin >> Ci;
            ss += Ci;
            ps ^= Ci;
            m = min(m, Ci);
        }

        cout << "Case #" << iCase << ": ";
        if (ps == 0)
            cout << (ss - m) << endl;
        else
            cout << "NO" << endl;
    }
}

