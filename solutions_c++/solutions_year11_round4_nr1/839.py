#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <vector>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

int main() {
//     freopen("input.txt", "rt", stdin);
//     freopen("A-small-attempt2.in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int tt;
    double x,s,r,trun;
    int n;
    double w[2000];
    double b[2000];
    double e[2000];
    double cursp;
    int curnom;
    double pres = 1e-9;
    
    cin >> tt;
    for (int ii = 1; ii <= tt; ii++) {
        cin >> x >> s >> r >> trun >> n;
        double summa = 0;
        double len;
        for (int i = 0; i < n; i++) {
            cin >> b[i] >> e[i] >> w[i];
            summa += e[i] - b[i];
        }
        double res = 0.0;
        summa = x-summa;
        if (summa/r > trun) {
            res += trun;
            summa -= r*trun;
            trun = 0;
            
            res += summa/s;
            summa = 0;
        } else {
            trun -= summa/r;
            res += summa/r;
            summa = 0;
        }
//         cout << res << " asdfasdf " << trun << endl;
        for (int j = 0; j < n; j++) {
            cursp = 200;
            for (int i = 0; i < n; i++) {
                if (abs(e[i]-b[i]) > pres)
                    if (w[i] < cursp) {
                        curnom = i;
                        cursp = w[i];
                    }
            }
                    
            int i = curnom;
            len = e[i] - b[i];
            
            if (len/(w[i] + r) > trun) {
                res += trun;
                len -= (w[i] + r)*trun;
                trun = 0;
                
                res += len/(s+w[i]);
                len = 0;
            } else {
                trun -= len/(r+w[i]);
                res += len/(r+w[i]);
                len = 0;
            }
            if (abs(trun) < pres)
                trun = 0;
            
            e[i] = b[i];
        }
        
        cout.precision(15);
        cout << "Case #" << ii << ": " << res << endl;
    }
    return 0;
}
