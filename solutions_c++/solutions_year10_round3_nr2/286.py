#include <iostream>
#include <cstring>
#include <cmath>

using namespace std;


int main() {
    int T, i, j, k;
    cin >> T;
    for(i= 1; i <= T; i++) {
        int L, P, C;
        cin >> L >> P >> C;
        int res= 0;
        while((long double)P / L > C) {
            long double d= sqrtl((long double)(P)/L);
            d*= L;
            long double f= floorl(d);
            long double c= ceill(d);
            if( P/f > c/L)
                P= (int)c;
            else
                L= (int)f;
            // cout << "L" << L << " P" << P << endl;
            res++;
        }
        cout << "Case #" << i << ": " << res << endl;
    }
    return 0;
}
