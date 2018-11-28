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

int dp[100][1001];

int
main(void)
{
    int N, S, Q;
    int i, j, k, m, ans;
    char str[128];
    vector<string> v_e;
    vector<string> v_q;

    cin >> N;

    for(i=1;i<=N;i++) {
        v_e.clear();
        v_q.clear();

        cin >> S;
        cin.getline(str, 128);
        for(j=0;j<S;j++) {
            cin.getline(str, 128);
            v_e.push_back(string(str));
        }

//         cout << "S=" << S << endl;

        cin >> Q;
        cin.getline(str, 128);
        for(j=0;j<Q;j++) {
            cin.getline(str, 128);
            v_q.push_back(string(str));
        }
        
        for(j=0;j<100;j++) {
            for(k=0;k<1001;k++) {
                dp[j][k] = 100000;
            }
        }

        if (Q == 0) {
            cout << "Case #" << i << ": " << 0 << endl;
            continue;
        }
        
        
        for(j=0;j<S;j++) {
            if (v_q[0] != v_e[j]) {
                dp[j][0] = 0;
            }
        }

        for(k=1;k<Q;k++) {
            for(j=0;j<S;j++) {
                for(m=0;m<S;m++) {
                    if (v_q[k] != v_e[m]) {
                        dp[m][k] = min(dp[j][k-1] + ((m == j) ? 0 : 1), dp[m][k]);
                    }
                }
            }
        }
        
        ans = 100000;
        for(j=0;j<S;j++) {
            ans = min(ans, dp[j][Q-1]);
        }
        cout << "Case #" << i << ": " << ans << endl;
    }
    
    return 0;
}
