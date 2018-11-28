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
    int i,j,X,S,R,T,N;
    //input
    cin >> X >> S >> R >> T >> N;
    vector<int> beg(N), end(N), w(N);
    for (i=0; i<N; i++)
        cin >> beg[i] >> end[i] >> w[i];
    //process
    //figure out where the walkways are
    //i.e., get an array of pairs "speed of the floor - length"
    map<int, int> lsp;
    for (i=0; i<N; i++) {
        lsp[w[i]] += end[i]-beg[i];
        X -= (end[i]-beg[i]);
    }
    lsp[0] = X;
    //iterate in counter-order; start with fastest piece, see how long it takes, add the time
    double total = 0, canrun = T, dist, speed;
    map<int,int>::iterator it;
//    cout << S << " " << R << endl;
    for (it=lsp.begin(); it!=lsp.end(); it++) {
        //how long will it take if running all the time
        speed = it->first;
        dist = it->second;
//        cout << dist << " " << speed << " " << canrun << endl;
        if (dist/(speed+R)<=canrun) {
            //run all this time
            canrun -= dist/(speed+R);
            total += dist/(speed+R);
        } else {
            //can run part of the time?
            dist -= canrun * (speed+R);
            total += canrun;
            canrun = 0;
            //walk the rest of it
            total += dist/(speed+S);
        }
    }
    //output
    cout << "Case #" << ind << ": " << fixed << setprecision(7) << total << endl;
/*    cout << lsp.size() << endl;
    for (it=lsp.begin(); it!=lsp.end(); it++)
        cout << it->first << " " << it->second << endl;
    cout << endl;*/
}

int main() {
    int i,T;
    cin >> T;
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
