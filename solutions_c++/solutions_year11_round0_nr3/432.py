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
    int i, j;
    int T, N;
    long long ret;
    long long c, x, sum;

    cin >> T;

    for(i=0;i<T;i++) {
        cin >> N;
        ret = 1000001;
        sum = 0;
        x = 0;
        for(j=0;j<N;j++) {
            cin >> c;
            sum += c;
            ret = min(ret, c);
            x ^= c;
        }
        if (x) {
            cout << "Case #" << (i+1) << ": " << "NO" << endl;
        } else {
            cout << "Case #" << (i+1) << ": " << (sum - ret) << endl;
        }
    }
    
    return 0;
}
