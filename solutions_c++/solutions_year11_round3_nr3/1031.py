#include <iostream>
#include <math.h>

using namespace std;

int main() {
    unsigned int t;

    cin >> t;

    for(double tt = 0; tt < t; tt++) {
        int n, l, h;
        cin >> n >> l >> h;
        int f[n];
        for(int i = 0; i < n; i++) 
            cin >> f[i];

        int res = 0;
        for(int i = l; i <= h; i++) {
            int ok = 1;
            for(int j = 0; j < n; j++) {
                if(!(i % f[j] == 0 || f[j] % i == 0)) {
                    ok = 0;
                    break;
                }
            }
            if(ok) {
                res = i;
                break;
            }
        }
        if(res)
            cout << "Case #" << tt+1 << ": " << res << "\n";
        else
            cout << "Case #" << tt+1 << ": NO\n";
    }

    return 0;
}
