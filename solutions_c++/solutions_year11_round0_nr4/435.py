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

double calc(int n)
{
    if (n == 1)
        return 0.0;
    
}

int
main(void)
{
    int i, j, k, c, v, p;
    int T, N;
    int pos[1001];
    int flg[1001];
    int cnt[1001];

    cin >> T;

    for(i=0;i<T;i++) {
        cin >> N;
        for(j=1;j<=N;j++) {
            cin >> v;
            pos[v] = j;
        }
        memset(flg, 0, sizeof(flg));
        memset(cnt, 0, sizeof(cnt));
        for(j=1;j<=N;j++) {
            if (flg[j])
                continue;
            c = 1;
            flg[j] = 1;
            v = pos[j];
            while (!flg[v]) {
                c++;
                flg[v] = 1;
                v = pos[v];
            }
            cnt[c]++;
        }
        long long ret = 0;
        for(j=2;j<=N;j++) {
            if (cnt[j]) {
//                 cout << j << "," << cnt[j] << endl;
                ret += j*(long long)cnt[j];
            }
        }
        cout << "Case #" << (i+1) << ": " << (double)ret << endl;
    }
    
    return 0;
}
