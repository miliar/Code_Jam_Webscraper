#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cctype>
#include <cstring>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <iterator>
#include <functional>
#include <utility>
#include <complex>
#include <numeric>
#include <algorithm>

#include <gmpxx.h>

using namespace std;

#define FOR(i,a,b) for(typeof(a) i=(a);i<(b);i++)

int main() {
    int T;
    cin >> T;
    FOR(it,1,T+1) {
        map<string, string> cc;
        set<string> dd;
        int C, D, N;
        cin >> C;
        FOR(i,0,C) {
            string co;
            cin >> co;
            cc[co.substr(0,2)] = co.substr(2,1);
        }
        cin >> D;
        FOR(i,0,D) {
            string _do;
            cin >> _do;
            dd.insert(_do);
        }
        cin >> N;
        string str;
        cin >> str;
        
        vector<string> inp(str.size(), "");
        FOR(i,0,N) inp[i] += str[i];
        
        vector<string> res;
        FOR(i,0,N) {
            if(res.size() && cc.find(res[res.size() - 1] + inp[i]) != cc.end()) {
                string val = cc[res[res.size() - 1] + inp[i]];
                res.pop_back();
                res.push_back(val);
            } else if (res.size() && cc.find(inp[i] + res[res.size() - 1]) != cc.end()) {
                string val = cc[inp[i] + res[res.size() - 1]];
                res.pop_back();
                res.push_back(val);
            } else {
                int des = false;
                FOR(j,0,res.size()) {
                    if(dd.find(res[j] + inp[i]) != dd.end() || dd.find(inp[i] + res[j]) != dd.end()) {
                        des = true;
                        res.clear();
                    }
                }
                if(!des) {
                    res.push_back(inp[i]);
                }
            }
        }
        cout << "Case #" << it << ": [";
        if(res.size()) {
            cout << res[0];
            FOR(i,1,res.size()) cout << ", " << res[i];
        }
        cout << "]" << endl;
    }
    return 0;
}
