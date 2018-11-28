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

string eq;
int K, N;

string words[1000];

int wcc[1000][256];

bool next_combination(vector<int>& v) {

    for (int i = v.sz - 1; i >= 0; i--) {
        if (v[i] + 1 < N) {
            v[i]++;
            for (int j = i + 1; j < v.sz; j++) {
                v[j] = 0;
            }
            return true;
        }
    }
    return false;
}

int main(int argc, char *argv[]) {
    freopen(argv[1], "r", stdin);
    int Tests;
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);

        cin >>eq >> K;
        cin >>N;

        memset( wcc, 0, sizeof(wcc));

        REP(i, N) {
            cin >> words[i];
            REP(j, words[i].sz) {
                wcc[i][words[i][j]]++;
            }
        }

        for (int k = 1; k <= K; k++) {
            vector<int> sel;
            REP(i, k) {
                sel.pb(0);
            }

            ll sum = 0;

            while (true) {
                ll mul = 1;
                REP(i, eq.sz) {

                    if (eq[i] == '+') {
                        sum += mul;
                        sum %= 10009;
                        mul = 1;
                    }
                    else {
                        int chsum = 0;
                        REP(zz, k) {
                            chsum += wcc[sel[zz]][eq[i]];
                        }
                        mul *= chsum;
                        mul %= 10009;
                    }
                }
                sum += mul;
                sum %= 10009;
                if (!next_combination(sel)) break;
            }

            cout <<sum;
            if (k == K) cout <<endl; else cout << " ";
        }
    }

}
