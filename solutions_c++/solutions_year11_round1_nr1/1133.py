#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int main()
{
    int nCase;
    cin >> nCase;

    for (int iCase = 1; iCase <= nCase; ++iCase) {

        unsigned long long N, Pd, Pg;
        cin >> N >> Pd >> Pg;

        bool f;
        if (Pg == 100) {
            f = Pd == 100;
        }
        else if (Pg == 0) {
            f = Pd == 0;
        }
        else {
            f = false;
            for (unsigned long long D = 1; D <= min((unsigned long long)100, N); ++D) {
                if ((D * Pd) % 100 == 0) {
                    f = true;
                    break;
                }
            }
        }
        
        string ans;
        if (f)
            ans = "Possible";
        else
            ans = "Broken";

        cout << "Case #" << iCase << ": " << ans << endl;
    }
}

