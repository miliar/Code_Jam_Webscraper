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
    vector<vector<char> > combine(26, vector<char>(26,'-'));
    vector<vector<bool> > opposed(26, vector<bool>(26,false));
    int i,j,C,D,N;
    string t;
    //read
    cin >> C;
    for (i=0; i<C; i++) {
        cin >> t;
        combine[t[0]-'A'][t[1]-'A'] = combine[t[1]-'A'][t[0]-'A'] = t[2];
    }
    cin >> D;
    for (i=0; i<D; i++) {
        cin >> t;
        opposed[t[0]-'A'][t[1]-'A'] = opposed[t[1]-'A'][t[0]-'A'] = true;
    }
    cin >> N >> t;
    //simulate
    vector<char> list;
    for (i=0; i<N; i++) {
        if (list.size()==0) {
            list.push_back(t[i]);
            continue;
        }
        //try to combine
        if (combine[list[list.size()-1]-'A'][t[i]-'A'] != '-') {
            list[list.size()-1] = combine[list[list.size()-1]-'A'][t[i]-'A'];
            continue;
        }
        //try to oppose
        for (j=0; j<list.size(); j++)
            if (opposed[list[j]-'A'][t[i]-'A']) {
                list.resize(0);
                break;
            }
        //just push
        if (list.size()>0)
            list.push_back(t[i]);
    }
    //output
    cout << "Case #" << ind << ": [";
    for (i=0; i<list.size(); i++) {
        cout << list[i];
        if (i<(int)list.size()-1)
            cout << ", ";
    }
    cout << "]" << endl;
}

int main() {
    int i,T;
    cin >> T;
    for (i=1; i<=T; i++) {
        solve(i);
    }
}
