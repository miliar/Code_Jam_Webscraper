#include <iostream>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;

ll area2(int a1, int b1, int a2, int b2, int a3, int b3) {
    //returns A^2
    int len1 = (a2-a1)*(a2-a1) + (b2-b1)*(b2-b1);
    int len2 = (a3-a1)*(a3-a1) + (b3-b1)*(b3-b1);
    int len3 = (a2-a3)*(a2-a3) + (b2-b3)*(b2-b3);
    ll sqr1 = len1*len1;
    ll sqr2 = len2*len2;
    ll sqr3 = len3*len3;
    ll ar = len1+len2+len3;
    ar *= ar;
    ar -= 2*(sqr1+sqr2+sqr3);
    if (ar % 4 != 0) cout << "failed!" << endl;
    ar >>= 2;
    return ar;
}

int main () {
    int C, N, M, cs=0;
    ll A;
    cin >> C;
    int i, j, k, x, y, z;
    while (C--) {
        cin >> N >> M >> A;
        bool fnd = 0;
        int a2, b2, a3, b3;
        for (i=0; i<=N; i++) {
            for (j=0; j<=M; j++) {
                for (k=0; k<=N; k++) {
                    for (x=0; x<=M; x++) {
                        if (area2(0, 0, i, j, k, x) == A*A) {
                            fnd = 1;
                            a2 = i;
                            b2 = j;
                            a3 = k;
                            b3 = x;
                            break;
                        }
                    }
                    if (fnd) break;
                }
                if (fnd) break;
            }
            if (fnd) break;
        }
        if (fnd) {
            cout << "Case #" << ++cs << ": 0 0 " << a2 << " " << b2 << " " << a3 << " " << b3 << endl;
        }
        else cout << "Case #" << ++cs << ": IMPOSSIBLE" << endl;
    }
    return 0;
}
