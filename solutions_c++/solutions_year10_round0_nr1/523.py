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
    int T, N, K;
    bool flag;
    int i, j;

    cin >> T;

    for(i=1;i<=T;i++) {
        cin >> N >> K;

        K = K % (1 << N);

        flag = true;
        for(j=0;j<N;j++) {
            if (((K >> j) & 0x1) == 0) {
                flag = false;
            }
        }
        
        cout << "Case #" << i << ": " << (flag ? "ON" : "OFF") << endl;
    }
    
    return 0;
}
