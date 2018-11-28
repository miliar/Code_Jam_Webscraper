#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

using namespace std;

int
main(void)
{
    int i, j, k, ret;
    long long N, PD, PG, D;
    long long WD, WG, NG, ND, R;
    int tc, TC;
    bool flg;

    cin >> TC;

    for(tc=1;tc<=TC;tc++) {
        cin >> N >> PD >> PG;
        if ((PD == 0) && (PG == 0)) {
            cout << "Case #" << tc << ": " << "Possible" << endl;
            continue;
        }
        if (((PD != 0) && (PG == 0))
            || ((PD != 100) && (PG == 100))) {
            cout << "Case #" << tc << ": " << "Broken" << endl;
            continue;
        }
        R = 100;
        if ((PD % 2) == 0) {
            PD /= 2;
            R /= 2;
        }
        if ((PD % 2) == 0) {
            PD /= 2;
            R /= 2;
        }
        if ((PD % 5) == 0) {
            PD /= 5;
            R /= 5;
        }
        if ((PD % 5) == 0) {
            PD /= 5;
            R /= 5;
        }
        cout << "Case #" << tc << ": " << ((R <= N) ? "Possible" : "Broken") << endl;
    }
    
    return 0;
}
