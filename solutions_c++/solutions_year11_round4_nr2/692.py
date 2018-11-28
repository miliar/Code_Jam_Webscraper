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
    freopen("B-small-attempt0.in", "rt", stdin);
//     freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int tt;
    int r, s, d;
    
    int w[20][20];
    char c;
    cin >> tt;
    double pres = 1e-6;
    for (int ii = 1; ii <= tt; ii++) {
        cin >> r >> s >> d;
        for (int i = 0; i < r; i++)
            for (int j = 0; j < s; j++) {
                cin >> c;
                w[i][j] = c - '0';
            }
            
        int maxlen = min(r,s);
        int res = 0;
        cout.precision(10);
//         cout << d << endl;
        for (int len = maxlen; len > 2; len--) if (res == 0) {
            
            double ic, jc, ir, jr;
            
            for (int i1 = 0; i1 <= r - len; i1++)
                for (int j1 = 0; j1 <= s - len; j1++) if (res == 0) {
                    
                    ic = 1.0*(i1 + i1 + len-1)/2;
                    jc = 1.0*(j1 + j1 + len-1)/2;
                    
                    ir = 0.0;
                    jr = 0.0;
                    
                    for (int i2 = 0; i2 < len; i2++)
                        for (int j2 = 0; j2 < len; j2++) {
                            ir += 1.0*(d + w[i1+i2][j1+j2]) * (i1+i2 - ic);
                            jr += 1.0*(d + w[i1+i2][j1+j2]) * (j1+j2 - jc);
                        }
                        
                    int i2;
                    int j2;
                    i2 = 0;
                    j2 = 0;
                    ir -= 1.0*(d + w[i1+i2][j1+j2]) * (i1+i2 - ic);
                    jr -= 1.0*(d + w[i1+i2][j1+j2]) * (j1+j2 - jc);
                    
                    i2 = 0;
                    j2 = len-1;
                    ir -= 1.0*(d + w[i1+i2][j1+j2]) * (i1+i2 - ic);
                    jr -= 1.0*(d + w[i1+i2][j1+j2]) * (j1+j2 - jc);
                    
                    i2 = len-1;
                    j2 = 0;
                    ir -= 1.0*(d + w[i1+i2][j1+j2]) * (i1+i2 - ic);
                    jr -= 1.0*(d + w[i1+i2][j1+j2]) * (j1+j2 - jc);
                    
                    i2 = len-1;
                    j2 = len-1;
                    ir -= 1.0*(d + w[i1+i2][j1+j2]) * (i1+i2 - ic);
                    jr -= 1.0*(d + w[i1+i2][j1+j2]) * (j1+j2 - jc);
                    
                    if ((abs(ir) < pres) && (abs(jr) < pres))
                        res = len;
                    
//                     if (len == 5) {
//                         cout << i1 << " " << j1 << " " << ir << " " << jr << endl;
//                     }
                }
        }
        
        if (res == 0)
            cout << "Case #" << ii << ": " << "IMPOSSIBLE" << endl;
        else
            cout << "Case #" << ii << ": " << res << endl;
        
    }
    return 0;
}
