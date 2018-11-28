#include <iostream>
#include <map>
#include <vector>

using namespace std;

typedef long long int LLI;

main() {
    LLI nc;
    cin >> nc;
    for (LLI ic=1; ic<=nc; ic++) {
        LLI n, m, a;
        cin >> n >> m >> a;
        bool found=false;
        LLI jx, jy, kx, ky;
        for (jx=0; jx<=n; jx++) {
            for (jy=0; jy<=m; jy++) {
                for (kx=(jx-n)>?(-n); kx<=((jx+n)<?n); kx++) {
                    for (ky=(jy-m)>?(-m); ky<=((jy+m)<?m); ky++) {
                        LLI aa = llabs(jx*ky-jy*kx);
                        if (aa == a) {
                            found = true;
                            break;
                        }
                    }
                    if (found) break;
                }
                if (found) break;
            }
            if (found) break;
        }
        if (!found) {
            cout << "Case #" << ic << ": IMPOSSIBLE" << endl;
        } else {
            LLI minx = 0;
            LLI miny = 0;
            minx <?= jx;
            minx <?= kx;
            miny <?= jy;
            miny <?= ky;
            // cout <<  minx << " " << miny << " " << jx << " " << jy << " " << kx << " " << ky << endl;
            cout << "Case #" << ic << ": " << -minx << " " << -miny << " " << jx-minx << " " << jy-miny << " " << kx-minx << " " << ky-miny << endl;
        }
    }
}
