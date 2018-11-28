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
    int N;
    int i, j;
    long long ans;
    long long n, A, B, C, D, x0, y0, M;
    long long x, y;
    int a, b, c, d, e, f;
    int ab, cd, ef;

    cin >> N;

    for(i=1;i<=N;i++) {

        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;

        vector<int> vx(n), vy(n);

        vx[0] = x0;
        vy[0] = y0;
//         cout << vx[0] << "," << vy[0] << endl;
        for(j=1;j<n;j++) {
            vx[j] = (A*vx[j-1]+B) % M;
            vy[j] = (C*vy[j-1]+D) % M;
//             cout << vx[j] << "," << vy[j] << endl;
        }
        long long cnt[3][3];

        for(j=0;j<3;j++) {
            cnt[j][0] = 0;
            cnt[j][1] = 0;
            cnt[j][2] = 0;
        }
        for(j=0;j<n;j++) {
            cnt[vx[j] % 3][vy[j] % 3]++;
        }
        
        ans = 0;
        for(a=0;a<3;a++) {
            for(b=0;b<3;b++) {
                ab = a*10+b;
                for(c=0;c<3;c++) {
                    for(d=0;d<3;d++) {
                        cd = c*10+d;
                        for(e=0;e<3;e++) {
                            for(f=0;f<3;f++) {
                                ef = e*10+f;
                                if ((((a+c+e) % 3) != 0) || (((b+d+f) % 3) != 0))
                                    continue;
                                if (!((ab <= cd) && (cd <= ef)))
                                    continue;
                                if (ab == cd && cd == ef) {
                                    ans += (cnt[a][b]-0)*(cnt[c][d]-1)*(cnt[e][f]-2)/6;
                                } else if (ab == cd && cd != ef) {
                                    ans += (cnt[a][b]-0)*(cnt[c][d]-1)*(cnt[e][f]-0)/2;
                                } else if (ab != cd && cd == ef) {
                                    ans += (cnt[a][b]-0)*(cnt[c][d]-0)*(cnt[e][f]-1)/2;
                                } else {
                                    ans += (cnt[a][b]-0)*(cnt[c][d]-0)*(cnt[e][f]-0);
                                }
                            }
                        }
                    }
                }
            }
        }
            
        
        cout << "Case #" << i << ": " << ans << endl;
    }
    
    return 0;
}
