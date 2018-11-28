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


int len[1001][1001];
int flg[1001];

int
main(void)
{
    int C, A, B, P;
    int i, j, k, n, m;
    int prime[1001];
    int ans;

    for(i=0;i<1001;i++) {
        prime[i] = 1;
    }
    prime[0] = prime[1] = 0;
    for(i=2;i<1001;i++) {
        if (prime[i]) {
//              cout << "i=" << i << endl;
            for(j=i+i;j<1001;j+=i) {
                prime[j] = 0;
            }
        }
    }
    
    cin >> C;

    for(i=1;i<=C;i++) {
        cin >> A >> B >> P;

        for(j=0;j<1001;j++) {
            for(k=0;k<1001;k++) {
                len[j][k] = 1000000;
            }
        }

        for(k=P;k<=B;k++) {
            if (!prime[k])
                continue;
            for(m=A;m<=B;m++) {
                for(n=m+1;n<=B;n++) {
                    if (((m % k) == 0) && ((n % k) == 0)) {
                        len[m][n] = len[n][m] = 1;
                    }
                }
            }
        }
        for(k=A;k<=B;k++) {
            for(m=A;m<=B;m++) {
                for(n=A;n<=B;n++) {
                    len[m][n] = min(len[m][n], len[m][k]+len[k][n]);
                }
            }
        }

        for(k=A;k<=B;k++) {
            flg[k] = 1;
        }

        ans = 0;
        for(k=A;k<=B;k++) {
            if (!flg[k]) {
                continue;
            }
            ans++;
            for(m=A+1;m<=B;m++) {
                if (len[k][m] != 1000000) {
                    flg[m] = 0;
                }
            }
        }
        
        
        cout << "Case #" << i << ": " << ans << endl;
    }
    
    return 0;
}
