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


int k;
string s;
vector<int> adaptor;

int eval() {
    int result = 2147480000;
    vector<int> q;
    REP(i, k) {
        q.pb(i);
    }
    do {
        char lastchar = 0;
        int count = 0;
        REP(i, s.size()) {
            int realpos = (i/k) * k + q[i % k];
            if (lastchar != s[realpos]) {
                lastchar = s[realpos];
                count++;
            }
        }
        result = min(result, count);
    }   while (next_permutation(q.begin(), q.end()));
    
    return result;

}

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int test;
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);
        cin >> k;
        cin >> s;
        printf("%d\n", eval());
    }
}

