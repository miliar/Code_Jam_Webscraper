// Powered by FTH

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

const string WELCOME = "welcome to code jam";

void add(int& a, int b) {
    a = (a + b) % 10000;
}

int solve(string s) {
    const int n = s.size();
    const int m = WELCOME.size();
    vector< vector<int> > dp(n+1, vector<int>(m+1, 0));
    dp[0][0] = 1;
    REP(i, n) {
        REP(j, m) {
            if (s[i] == WELCOME[j])
                add(dp[i+1][j+1], dp[i][j]);
            add(dp[i+1][j], dp[i][j]);
        }
        add(dp[i+1][m], dp[i][m]);
    }
    return dp[n][m];
}

int main() {

    int nCases;
    {
        string s;
        getline(cin, s);
        istringstream is(s);
        is >> nCases;
    }

    REP(iCase, nCases) {
        string s;
        getline(cin, s);
        printf("Case #%d: %04d\n", iCase+1, solve(s));
    }

    return 0;
}
