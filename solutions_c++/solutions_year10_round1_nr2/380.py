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

int D, I, M, N;

int fill(int diff)
{
    if (M == 0) {
        return ((diff == 0) ? 0 : 1000000);
    }
    return max(0, (diff-1)/M*I);
}

int cost2(int x, int y)
{
    int diff;
    int ret;
    int i;

    diff = abs(x-y);

    ret = max(0, diff-M);

    for(i=0;i<=diff;i++) {
        ret = min(ret, fill(diff-i)+i);
    }

    return ret;
}

int
main(void)
{
    int i, j;
    int x, y, z;
    int T;
    int a[100];
    int cost, min_cost;

    cin >> T;

    for(i=1;i<=T;i++) {
        cin >> D >> I >> M >> N;
        for(j=0;j<N;j++) {
            cin >> a[j];
        }

        if (N == 1) {
            min_cost = 0;
        } else if (N == 2) {
            min_cost = D;
            min_cost = min(min_cost, cost2(a[0], a[1]));
        } else {
            min_cost = D*2;
            min_cost = min(min_cost, cost2(a[0], a[1]) + D);
            min_cost = min(min_cost, cost2(a[0], a[2]) + D);
            min_cost = min(min_cost, cost2(a[1], a[2]) + D);

//             cout << "min_cost=" << min_cost << endl;

            for(x=0;x<256;x++) {
                for(y=0;y<256;y++) {
                    for(z=0;z<256;z++) {
                        cost = abs(a[0]-x) + abs(a[1]-y) + abs(a[2]-z);
                        if (cost > min_cost)
                            continue;
                        cost += fill(abs(x-y));
                        cost += fill(abs(z-y));
                        min_cost = min(min_cost, cost);
                    }
                }
            }
        }

        cout << "Case #" << i << ": " << min_cost << endl;
    }
    
    return 0;
}
