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

int val[500][500];
int dp[501][501][2];

int
main(void)
{
    int i, j, k, ret, a, b, cx, cy, px, py;
    int tc, TC;
    int R, C, D;
    string s;
    int width;

    cin >> TC;

    for(tc=1;tc<=TC;tc++) {
        cin >> R >> C >> D;
        for(i=0;i<R;i++) {
            cin >> s;
            for(j=0;j<C;j++) {
                val[i][j] = (s[j] - '0') + D;
            }
        }

        bool found = false;
        for(width=min(R,C);width>=3;width--) {
//             cout << "width="  << width << endl;
            found = false;
            for(i=0;i<(R-width+1);i++) {
                for(j=0;j<(C-width+1);j++) {
                    cx = j*2 + width;
                    cy = i*2 + width;
//                     cout << "cx,cy=" << cx << "," << cy << endl;
                    px = 0;
                    py = 0;
                    for(a=i;a<(i+width);a++) {
                        for(b=j;b<(j+width);b++) {
                            if ((a == i) && (b == j))
                                continue;
                            if ((a == i) && (b == (j+width-1)))
                                continue;
                            if ((a == (i+width-1)) && (b == j))
                                continue;
                            if ((a == (i+width-1)) && (b == (j+width-1)))
                                continue;
                            px += (b*2+1-cx)*val[a][b];
                            py += (a*2+1-cy)*val[a][b];
                        }
                    }
//                     cout << "px,py=" << px << "," << py << endl;
                    if ((px == 0) && (py == 0)) {
                        found = true;
                    }
                }
                if (found)
                    break;
            }
            if (found)
                break;
        }

        if (found) {
            cout << "Case #" << tc << ": " << width << endl;
        } else {
            cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;
        }
    }
    
    return 0;
}
