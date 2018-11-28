#include <iostream>
#include <math.h>

using namespace std;

int main() {
    unsigned int t;

    cin >> t;

    for(double tt = 0; tt < t; tt++) {
        unsigned long long int n, pd, pg;
        unsigned long long int d = 0, g = 0, ok = 0;
        cin >> n >> pd >> pg;

        for(d = 1; d <= n; d++) {
            if((d * pd) % 100 == 0) break;
        }
        if(d <= n) {
            if(pg == 0 && pd > 0) ok = -1;
            if(pg == 100 && pd != 100) ok = -1;
            for(g = d; ok != -1; g++) {
                if((g * pg) % 100 == 0 && g) {
                    ok = 1;
                    break;
                }
                //if((g * pg) / 100 < pg) break;
            }
            
        }

        //printf("n=%d pd=%d pg=%d d=%d g=%d\n", n, pd, pg, d, g);

        if(ok == 1) cout << "Case #" << tt+1 << ": " << "Possible" << "\n";
        else cout << "Case #" << tt+1 << ": " << "Broken" << "\n";
    }

    return 0;
}
