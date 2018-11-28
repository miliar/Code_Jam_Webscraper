#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
//     freopen("input.txt", "rt", stdin);
    freopen("B-small-attempt2.in", "rt", stdin);
//     freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int tt,d,n;
    int p[300];
    int v[300];
    int sum1, sum2, sum3;
    int res;
    
    cin >> tt;
    for (int ii = 1; ii <= tt; ii++) {
        cin >> n >> d;
        for (int i = 0; i < n; i++)
            cin >> p[i] >> v[i];
        
        res = 0;
        for (int lef = 0; lef < n; lef++)
            for (int rig = lef; rig < n; rig++) {
                
                sum1 = p[rig] - p[lef];
                sum2 = 0;
                for (int i = lef; i <= rig; i++)
                    sum2 += v[i];
                sum2 -= 1;
                sum2 *= d;
                
                sum3 = 0;
                for (int i = lef; i <= rig; i++)
                    sum3 = max(sum3, v[i]-1);
                sum3 *= d;
                
                res = max(res, max(sum2-sum1, sum3));
            }
        
//         cout << sum1 << endl;
//         cout << sum2 << endl;
//         cout << sum3 << endl;
//         cout << "Case #" << ii << ": " << max(1.0*(sum2-sum1)/2, 1.0*sum3/2) << endl;
        cout << "Case #" << ii << ": " << 1.0*res/2 << endl;
    }
    return 0;
}
