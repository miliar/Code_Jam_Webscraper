#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <stack>
#include <string.h>
#include <algorithm>
#include <iomanip>
#define FOREACH(it, C) for(typeof((C).begin()) it = (C).begin(); it != (C).end(); ++it)
using namespace std;
const int ASCII_SIZE = 256;
const double EPS = 1e-7;
typedef long long int LL;
typedef long double LD;

bool tryit(const LD m, const vector<pair<LD,LD> > &v, const LD d) {
    LD last = v[0].first - m + (v[0].second - 1.0) * d;
    if(last - v[0].first > m) {
   //     cout << 0 << " " << last << " " << m << endl;
        return false;
    }
    for(int i = 1; i < v.size(); ++i) {
        last = max(last + d, v[i].first - m) + (v[i].second - 1.0) * d;
        if(last - v[i].first > m) {
      //      cout << i << " " << last << " " << m << endl;
            return false;
        }
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    int t;
	cin >> t;
	for(int testCase = 1; testCase <= t; ++testCase) {
        int c;
        LD d;
        cin >> c >> d;
        vector<pair<LD,LD> > v(c);
        for(int i = 0;  i < c; ++i) {
            cin >> v[i].first >> v[i].second;
        }
        LD L = 0.0, R = 1e14;
        while(R - L > EPS) {
            LD M = (R + L) / LD(2.0);
            if(tryit(M, v, d)) {
                R = M ;
            } else {
                L = M;
            }
        }
        cout << "Case #" << fixed << setprecision(9) << testCase << ": " << L << endl;
    }
}
