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
    int i, j, p, c, pre;
    int T, K, n, d;
    int nxt[5000];

    cin >> T; 

    for(i=1;i<=T;i++) {
        cin >> K;
        cin >> n;

        vector<int> vd(n);

        for(j=0;j<n;j++) {
            cin >> d;
            vd[j] = d;
        }

        vector<int> val(K);

        for(j=0;j<K;j++) {
            nxt[j] = (j+1) % K;
        }
        for(j=0;j<K;j++) {
            val[j] = 0;
        }
        val[0] = 1;
        nxt[K-1] = 1;
        p = 0;
        pre = 0;
        for(j=2;j<=K;j++) {
            c = 0;
            while (c < j) {
                pre = p;
                p = nxt[p];
                c++;
            }
            val[p] = j;
            nxt[pre] = nxt[p];
//            cout << p << "=" << j << endl;
        }
        
        cout << "Case #" << i << ":";
        for(j=0;j<n;j++) {
            cout << " " << val[vd[j]-1];
        }
        cout << endl;
    }
    
    return 0;
}
