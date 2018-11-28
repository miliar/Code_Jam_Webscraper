#define _CRT_SECURE_NO_DEPRECATE
#pragma warning(disable:4530)
#include <string>
#include <vector>
#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <set>
#include <cmath>
#include <map>
#include <cassert>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,x) for(typeof((x).begin())it=(x).begin();it!=(x).end();++it)
#define all(x) (x).begin(),(x).end()
#define CLR(x,v) memset(x,v,sizeof(x))
#define pb push_back
#define sz size()
#define exist(c,x) ((c).find(x)!=(c).end())
#define cexist(c,x) (find(all(c),x)!=(c).end())
#define SMIN(a, b) a = min((a),(b))
#define SMAX(a, b) a = max((a),(b))

typedef long long ll;

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    int L, D;
    vector<string> cand;
    cin >>L >>D;
    cin >> Tests;

    REP(i, D) {
        string s;
        cin >> s;
        cand.pb(s);
    }
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        string pattern;
        bool mask[20][256];
        memset(mask, 0, sizeof(mask));
        cin >>pattern;
        int p = 0;
        REP(i, L) {
            if (pattern[p] == '(') {
                p++;
                while (pattern[p] != ')') {
                    mask[i][pattern[p]] = true;
                    p++;
                }
                p++;
            }
            else {
                mask[i][pattern[p]] = true;
                p++;
            }
        }
        int count = 0;
        REP(i, D) {
            bool matches = true;
            REP(j, L) {
                if (!mask[j][cand[i][j]]) {
                    matches = false;
                    break;
                }
            }
            if (matches) count ++;
        }
        cout <<count <<endl;
    }
    return 0;

}
