#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
using namespace std;

int main() {
    int T,N;

    cin >> T;
    for(int tc=1;tc<=T;tc++) {
        char c;
        int n;

        cin >> N;

        int o,b;
        int t = 0;
        int tt = 0;
        o=b=1;
        char old = 0;
        for(int i=0;i<N;i++) {
            cin >> c >> n;

            if(c==old) {
                if(c=='O') {
                    tt += abs(n-o)+1;
                    t += abs(n-o)+1;
                    o = n;
                } else {
                    tt += abs(n-b)+1;
                    t += abs(n-b)+1;
                    b = n;
                }
            } else {
                if(c=='O') {
                    if(tt < abs(n-o)) {
                        tt = abs(n-o) - tt + 1;
                        t += tt;
                    } else {
                        tt = 1;
                        t += tt;
                    }

                    o = n;
                } else {
                    if(tt < abs(n-b)) {
                        tt = abs(n-b) - tt + 1;
                        t += tt;
                    } else {
                        tt = 1;
                        t += tt;
                    }

                    b = n;
                }
            }

            old = c;
        }

        printf("Case #%d: %d\n", tc,t);
    }

    return 0;
}
