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
    //input
    cin >> N;
    vector<int> pieces(N);
    for (i=0; i<N; i++)
        cin >> pieces[i];
    //output
    cout << "Case #" << ind << ": ";
    //process
    //check whether it's possible at all
    int X = 0, S = 0;
    for (i=0; i<N; i++) {
        X ^= pieces[i];
        S += pieces[i];
    }
    if (X != 0) {
        cout << "NO" << endl;
        return;
    }
    S -= *(min_element(pieces.begin(), pieces.end()));
    cout << S << endl;
}

int main() {
    int i,T;
    cin >> T;
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
