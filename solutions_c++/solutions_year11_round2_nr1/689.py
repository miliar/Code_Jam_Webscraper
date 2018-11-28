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
//     freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    
    int tt,n;
    char a[200][200];
    double res[200];
    double wp[200];
    double newp[200];
    double owp[200];
    double oowp[200];
    int kol[200];
    int sum[200];
    cin >> tt;
    for (int ii = 1; ii <= tt; ii++) {
        cin >> n;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                cin >> a[i][j];
        for (int i = 0; i < n; i++) {
            kol[i] = 0;
            for (int j = 0; j < n; j++)
                if (a[i][j] != '.')
                    kol[i]++;
        }
        
        for (int i = 0; i < n; i++) {
            sum[i] = 0;
            for (int j = 0; j < n; j++)
                if (a[i][j] == '1')
                    sum[i]++;
        }
        
        for (int i = 0; i < n; i++)
            wp[i] = 1.0 * sum[i] / kol[i];
        
        
        for (int i = 0; i < n; i++)
            newp[i] = 0;
            
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (a[j][i] == '1')
                    newp[i] += 1.0 * (sum[j]-1) / (kol[j]-1);
                else if (a[j][i] == '0')
                    newp[i] += 1.0 * sum[j] / (kol[j]-1);

        for (int i = 0; i < n; i++)
            owp[i] = newp[i] / kol[i];
        
        for (int i = 0; i < n; i++) {
            oowp[i] = 0;
            for (int j = 0; j < n; j++)
                if (a[j][i] != '.')
                    oowp[i] += owp[j];
            oowp[i] /= kol[i];
        }
        
        for (int i = 0; i < n; i++)
            res[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i];
        
        cout << "Case #" << ii << ": " << endl;
        
//         for (int i = 0; i < n; i++)
//            cout << wp[i] << endl;
//         cout << " - " << endl;
//         
//         for (int i = 0; i < n; i++)
//            cout << owp[i] << endl;
//         cout << " - " << endl;
//         
        cout.precision(10);
        
        for (int i = 0; i < n; i++)
           cout << res[i] << endl;
    }
    return 0;
}
