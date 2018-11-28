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
    int i,j,K,l,m,n,R,C,D;
    char c;
    //input
    cin >> R >> C >> D;
    vector<vector<int> > g(R,vector<int>(C,0));
    for (i=0; i<R; i++)
    for (j=0; j<C; j++) {
        cin >> c;
        g[i][j] = c-'0';
    }
    //process
    //try all values of K and see if any fits
    int ic,jc;
    long sumi, sumj;
    for (K=min<int>(R,C); K>=3; K--) {
        for (i=0; i+K<=R; i++)
        for (j=0; j+K<=C; j++) {    //remember to multiply by 2 all coords!
            ic = 2*i+K-1;
            jc = 2*j+K-1;
            sumi = sumj = 0;
            for (m=i; m<i+K; m++)
            for (l=j; l<j+K; l++) {
                if (m==i && l==j) continue;
                if (m==i+K-1 && l==j) continue;
                if (m==i && l==j+K-1) continue;
                if (m==i+K-1 && l==j+K-1) continue;
                sumi += g[m][l]*(2*m-ic);
                sumj += g[m][l]*(2*l-jc);
            }
            if (sumi==0 && sumj==0) {
                cout << "Case #" << ind << ": "<< K << endl;
                return;
            }
        }
    }
    //output
    cout << "Case #" << ind << ": IMPOSSIBLE" << endl;
}

int main() {
    int i,T;
    cin >> T;
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
