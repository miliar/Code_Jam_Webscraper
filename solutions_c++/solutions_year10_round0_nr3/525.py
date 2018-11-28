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
    int T, R, N, k;
    long long earned, n;
    int i, j, a, b;
    int loop_start;
    int loop_cnt;
    long long loop_sum;
    int g[1000];
    int nxt[1000];
    long long sum[1000];
    int flg[1000];

    cin >> T;

    for(i=1;i<=T;i++) {
        cin >> R >> k >> N;

        for(j=0;j<N;j++) {
            cin >> g[j];
        }
        for(a=0;a<N;a++) {
            sum[a] = 0;
            for(b=0;b<N;b++) {
                if ((sum[a]+g[(a+b) % N]) > k) {
                    break;
                }
                sum[a] += g[(a+b) % N];
            }
            nxt[a] = (a+b) % N;
//             cout << "sum[" << a << "]=" << sum[a] << endl;
//             cout << "nxt[" << a << "]=" << nxt[a] << endl;
        }

        memset(flg, 0, sizeof(flg));
        a = 0;
        while (!flg[a]) {
            flg[a] = 1;
            a = nxt[a];
        }
        loop_start = a;
//         cout << "loop_start = " << loop_start << endl;
        
        loop_sum = 0;
        a = loop_start;
        loop_sum += sum[a];
        loop_cnt = 1;
        a = nxt[a];
        while (a != loop_start) {
            loop_sum += sum[a];
            a = nxt[a];
            loop_cnt++;
        }
//         cout << "loop_cnt = " << loop_cnt << endl;
//         cout << "loop_sum = " << loop_sum << endl;

        earned = 0;
        a = 0;
        while (a != loop_start && 0 < R) {
            earned += sum[a];
            a = nxt[a];
            R--;
        }
//         cout << "earned = " << earned << endl;
        while (R > loop_cnt) {
            n = R/loop_cnt;
            R -= (loop_cnt*n);
            earned += (loop_sum*n);
        }
//         cout << "earned = " << earned << endl;
        while (0 < R) {
            earned += sum[a];
            a = nxt[a];
            R--;
        }
//         cout << "earned = " << earned << endl;

        cout << "Case #" << i << ": " << earned << endl;
    }
    
    return 0;
}
