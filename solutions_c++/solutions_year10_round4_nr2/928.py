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

int ticket[1024][1024];
int tic_need[1024][1024];
int M[1024];

int
main(void)
{
    int T, P;
    int i, j, k, cnt, a;

    cin >> T;

    for(i=1;i<=T;i++) {
        cin >> P;
        for(j=0;j<(1 << P);j++) {
            cin >> M[j];
//             cout << M[j] << " ";
            M[j] = P-M[j];
        }
//         cout << endl;
        for(j=0;j<P;j++) {
            for(k=0;k<(1 << (P-j-1));k++) {
                cin >> ticket[j][k];
//                 cout << ticket[j][k] << " ";
            }
//             cout << endl;
        }

        cnt = 0;
        for(j=P-1;j>=0;j--) {
            for(k=0;k<(1 << (P-j-1));k++) {
                bool flg = false;
                for(a=(1 << (j+1))*k;a<((1 << (j+1))*(k+1));a++) {
                    if (M[a] > 0) {
                        flg = true;
                        break;
                    }
                }
                if (!flg) {
                    continue;
                }
                cnt += ticket[j][k];
                for(a=(1 << (j+1))*k;a<((1 << (j+1))*(k+1));a++) {
                    M[a]--;
                }
            }
        }

        cout << "Case #" << i << ": " << cnt << endl;
    }
    
    return 0;
}
