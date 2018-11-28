#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int T;

int main()
{
    scanf("%d", &T);
    for (int tt = 0; tt < T; tt++)  {
        long long N, PD, PG;
        cin>>N>>PD>>PG;
        bool ok = 0;
        for (int D = 1; D <= min(N, 100LL); D++) {
            if (PD * D % 100 == 0) {
                   ok = 1; break;
            }
        }
        if (PG == 0 && PD != 0) {
               ok = 0;
           }
        if (PG == 100 && PD != 100) {
               ok = 0;
           }
        if (ok)
           cout<<"Case #"<<tt+1<<": Possible\n";
        else
            cout<<"Case #"<<tt+1<<": Broken\n";
    }
    return 0;
}
