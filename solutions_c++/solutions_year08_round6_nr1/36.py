#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())

struct P {
    int x, y;
};

bool valid(int left, int right, int bottom, int top, const vector<P>& animals) {
    REP(i, animals.size()) {
        P p = animals[i];
        if (left <= p.x && p.x <= right && bottom <= p.y && p.y <= top) {
            return false;
        }
    }
    return true;
}

void solve() {

    int nReferences;
    cin >> nReferences;

    int left = INT_MAX, bottom = INT_MAX, right = INT_MIN, top = INT_MIN;
    vector<P> animals;
    REP(i, nReferences) {
        P p;
        cin >> p.x >> p.y;
        string s;
        cin >> s;
        bool type = (s == "BIRD");
        if (!type)
            cin >> s;
        if (type) {
            left = min(left, p.x);
            right = max(right, p.x);
            bottom = min(bottom, p.y);
            top = max(top, p.y);
        }
        else {
            animals.push_back(p);
        }
    }

    int nQueries;
    cin >> nQueries;
    REP(i, nQueries) {
        P p;
        cin >> p.x >> p.y;
        if (left <= p.x && p.x <= right && bottom <= p.y && p.y <= top) {
            cout << "BIRD" << endl;
        }
        else if (valid(min(left, p.x),
                       max(right, p.x),
                       min(bottom, p.y),
                       max(top, p.y),
                       animals)) {
            cout << "UNKNOWN" << endl;
        }
        else {
            cout << "NOT BIRD" << endl;
        }
    }

}



int main() {


    int nCases;
    cin >> nCases >> ws;

    REP(iCase, nCases) {

        cout << "Case #" << iCase+1 << ":" << endl;
        solve();

    }

    return 0;
}

