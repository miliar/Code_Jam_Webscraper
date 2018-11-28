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

bool matches(string p, string s) {
    int n = s.size();
    int j = 0;
    REP(i, n) {
        set<char> v;
        if (p[j] == '(') {
            j++;
            while(p[j] != ')')
                v.insert(p[j++]);
            j++;
        } else {
            v.insert(p[j++]);
        }
        if (!v.count(s[i]))
            return false;
    }
    return true;
}

int main() {
    int len, nDic, nCases;
    cin >> len >> nDic >> nCases;

    vector<string> dic(nDic);
    REP(i, nDic)
        cin >> dic[i];

    REP(iCase, nCases) {
        string pattern;
        cin >> pattern;
        int res = 0;
        REP(i, nDic)
            if (matches(pattern, dic[i]))
                res++;
        cout << "Case #" << iCase+1 << ": " << res << endl;
    }

    return 0;
}
