#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <fstream>
#include <cassert>
#include <limits>
#include <numeric>
#include <map>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
typedef long long int ll;
typedef long double ld;

struct circle {
    int index;
    int r;
};

vector<int> x_result;
vector<int> y_result;
vector<bool> fitted;

bool operator<(const circle &lhs, const circle &rhs) {
    return lhs.r > rhs.r;
}

void fit(int w, int l, int dx, int dy, multiset<circle> &s, bool z) {
    if(w < 0 || l < 0 || s.empty()) {
        return;
    }
    
    /*
    cerr << "FITING" << endl;
    cerr << w << " " << l << " " << dx << " " << dy << endl;
    FOREACH(it, s) {
        cerr << it->index << " " << it->r << " ";
    }
    cerr << endl;
    //*/
    multiset<circle>::iterator it;
    it = s.begin();
    int index = it->index;
    int r = it->r;
    s.erase(it);
    x_result[index] = dx;
    y_result[index] = dy;
    fitted[index] = true;
    fit(w - 2 * r, l, 2 * r + dx, dy, s, z);
    fit(0, l - 2 * r, dx, dy + 2 * r, s, false);
}

void solve(int n, int w, int l, vector<int> r) {
    vector<circle> c(n);
    for(int i = 0; i < n; ++i) {
        c[i].index = i;
        c[i].r = r[i];
    }
    multiset<circle> s(c.begin(), c.end());
    //cerr << "FITING" << endl;
    fit(w, l, 0, 0, s, true);
}

int main() {
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        int n, w, l;
        x_result.clear();
        y_result.clear();
        fitted.clear();
        cin >> n >> w >> l;
        vector<int> r(n);
        x_result.resize(n, 0);
        y_result.resize(n, 0);
        fitted.resize(n, false);

        for(int i = 0; i < n; ++i) {
            cin >> r[i];
        }
        solve(n, w, l, r);
		cout << "Case #" << testCase << ": ";
        for(int i = 0; i < n; ++i) {
            if(!fitted[i]) {
                //cerr << "Unfitted stuff" << endl << endl << endl;
            }
            cout << x_result[i] << " " << y_result[i];
            if(i != n - 1) {
                cout << " ";
            }
        }
        cout << endl;
	}
}
