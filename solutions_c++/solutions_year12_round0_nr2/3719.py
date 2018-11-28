#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <cstring>
#include <cassert>
#include <cctype>

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int c=1; c<=T; ++c) {
        int cnt=0;
        int N, S, p;
        cin >> N >> S >> p;
        for (int i=0; i<N; ++i) {
            int t;
            cin >> t;
            int to3 = t/3;
            int tm3 = t%3;
            int d = p-to3;
            // cerr << "t=" << t << ": to3=" << to3 << "; tm3=" << tm3 << "; d=" << d << "\n";
            if (d<=0) {
                ++cnt;
                // cerr << "0: " << cnt << "\n";
                continue;
            }
            if (d>2) continue;
            if (d==2) {
                if (tm3==2 && S>0) {
                    ++cnt;
                    // cerr << "1: " << cnt << "\n";
                    --S;
                }
            }
            if (d==1) {
                if (tm3==0 && t>0 && S>0) {
                    ++cnt;
                    // cerr << "2: " << cnt << "\n";
                    --S;
                } else if (tm3>0) {
                    // cerr << "3: " << cnt << "\n";
                    ++cnt;
                }
            }
        }
        cout << "Case #" << c << ": " << cnt << "\n";
    }
}
