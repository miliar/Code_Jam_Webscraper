#include <stdio.h>
#include <iostream>

using namespace std;

void open_file() {
    freopen("c-large.in", "r",stdin);
    freopen("c.outs", "w", stdout);    
}

int main () {
    int ntest, lntest, n, x, minx, y, sum;
    open_file();
    cin >> ntest;
    lntest = ntest;
    while (ntest--) {
        cin >> n;
        cin >> x;
        minx = x;
        sum = x;
        for (int i = 1; i < n; i++) {
            cin >> y;
            x = x ^ y;
            minx = min(minx, y);
            sum += y;
        }
        if (x != 0) 
            cout << "Case #" << lntest - ntest << ": NO" << endl;   
        else cout << "Case #" << lntest - ntest << ": " << sum - minx << endl;       
    }
    return 0;   
}
