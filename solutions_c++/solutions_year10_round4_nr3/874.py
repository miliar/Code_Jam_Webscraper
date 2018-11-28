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
    int C, R;
    int x, y, x0, y0, x1, y1, xx, yy;
    int n;

    int tbl[101][101][2];
    int i, j;

    cin >> C;

    for(i=1;i<=C;i++) {
        cin >> R;

        memset(tbl, 0, sizeof(tbl));
        for(j=0;j<R;j++) {
            cin >> x0 >> y0 >> x1 >> y1;
            for(x=x0;x<=x1;x++) {
                for(y=y0;y<=y1;y++) {
                    tbl[y][x][0] = 1;
                }
            }
        }

//         for(y=1;y<=20;y++) {
//             for(x=1;x<=20;x++) {
//                 cout << tbl[y][x][0];
//             }
//             cout << endl;
//         }
        for(n=1;;n++) {
            bool flg = true;
            for(x=1;x<=100;x++) {
                for(y=1;y<=100;y++) {
                    if (tbl[y][x][(n+1) % 2] == 0) {
                        if (tbl[y-1][x][(n+1) % 2] && tbl[y][x-1][(n+1) % 2]) {
                            tbl[x][y][n % 2] = 1;
                            flg = false;
                        } else {
                            tbl[x][y][n % 2] = 0;
                        }
                    } else {
                        if (!tbl[y-1][x][(n+1) % 2] && !tbl[y][x-1][(n+1) % 2]) {
                            tbl[x][y][n % 2] = 0;
                        } else {
                            tbl[x][y][n % 2] = 1;
                            flg = false;
                        }
                    }
                }
            }
            if (flg) {
                break;
            }
        }

        cout << "Case #" << i << ": " << n << endl;
    }
    
    return 0;
}
