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
    vector<int> button(N), hall(N), pos(2,1), time(2,0);
    for (i=0; i<N; i++) {
        cin >> t >> button[i];
        hall[i] = (t=="B"?0:1);
    }
    //process
    for (i=0; i<N; i++) {
        //get the necessary robot to this position-time from his last position-time as soon as possible
        time[hall[i]] = max<int>(time[hall[i]] + abs(pos[hall[i]] - button[i]), time[1-hall[i]]) + 1;
        pos[hall[i]] = button[i];
    }
    
    //output
    cout << "Case #" << ind << ": " << max<int>(time[0], time[1]) << endl;
}

int main() {
    int i,T;
    cin >> T;
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
