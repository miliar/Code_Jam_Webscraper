#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define MAXN 15

int T, N, C[MAXN + 5];

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);
    
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;
        for (int i = 0; i < N; ++i) cin >> C[i];
        
        int maxSean = -1;
        for (int state = 1; state < (1 << N) - 1; ++state) {
            int sean = 0;
            int patrick = 0;
            int sum = 0;

            for (int i = 0; i < N; ++i) {
                if (((state >> i) & 1) == 0) {
                   sean ^= C[i];
                   sum += C[i];
                }
                else patrick ^= C[i];
            }
            
            if (state == 0) cout << sean << " " << patrick << endl;
            
            if (sean == patrick && maxSean < sum) {
               maxSean = sum;
            }
        }
        
        cout << "Case #" << t << ": ";
        if (maxSean == -1) cout << "NO" << endl;
        else cout << maxSean << endl;
    }
        
    return 0;
}
