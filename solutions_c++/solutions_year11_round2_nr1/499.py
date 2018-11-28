#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <utility>
#include <bitset>
#include <functional>
#include <stdio.h>
#include <stdarg.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

void solve(int ind) {
    int i,j,N;
    string t;
    //input
    cin >> N;
    vector<string> games(N);
    for (i=0; i<N; i++)
        cin >> games[i];
    //process
    vector<double> WP(N,0), OWP(N,0), OOWP(N,0), ng(N,0);
    //calc WP
    for (i=0; i<N; i++) {
        for (j=0; j<N; j++)
            if (games[i][j] != '.') {
                ng[i]++;
                if (games[i][j] == '1')
                    WP[i]++;
            }
    }
    //calc OWP
    for (i=0; i<N; i++) {
        for (j=0; j<N; j++)
            if (games[i][j] != '.') {
                OWP[i] += (WP[j] - (games[j][i]=='1'?1:0))/(ng[j]-1);
            }
        OWP[i] /= ng[i];
        
    }    
    //calc OOWP
    for (i=0; i<N; i++) {
        for (j=0; j<N; j++)
            if (games[i][j] != '.')
                OOWP[i] += OWP[j];
        OOWP[i] /= ng[i];
    }    
    //output
    cout << "Case #" << ind << ":" << endl;
/*    for (i=0; i<N; i++)
        cout << (WP[i]/ng[i]) << endl;
    for (i=0; i<N; i++)
        cout << (OWP[i]) << endl;*/
    for (i=0; i<N; i++)
        cout << (0.25 * WP[i]/ng[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]) << endl;
}

int main() {
    int i,T;
    cin >> T;
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
