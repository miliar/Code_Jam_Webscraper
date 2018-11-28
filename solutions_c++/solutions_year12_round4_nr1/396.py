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

string solve(int n, int D, vector<int>& d, vector<int> l) {
    int x = d[0] * 2;
    n++;
    d.push_back(D);
    l.push_back(0);
    vector<int> m(n, 0);
    m[0] = d[0];
    for (int i = 0; i < n; ++i) {
        if (x < d[i]) {
            return "NO";
        }
        //m[i] = max(m[i], d[i] - *lower_bound(d.begin(), d.end(), d[i] - l[i]));
        for(int j = i + 1; j < n && d[j] - d[i] <= m[i]; ++j) {
            m[j] = max(m[j], min(l[j], d[j] - d[i]));
        }
        int xi = d[i] + m[i];
        //cerr << i << " " << xi << " " << x << endl;
        x = max(x, xi);
    }
    return "YES";
}

int main() {
    int numberOfCases;
	cin >> numberOfCases;
	for(int testCase = 1; testCase <= numberOfCases; ++testCase) {
        int n;
        cin >> n;
        vector<int> d(n);
        vector<int> l(n);
        for(int i = 0; i < n; ++i) {
            cin >> d[i] >> l[i];
        }
        int D;
        cin >> D;
		cout << "Case #" << testCase << ": " << solve(n, D, d, l) << endl;
	}
}
