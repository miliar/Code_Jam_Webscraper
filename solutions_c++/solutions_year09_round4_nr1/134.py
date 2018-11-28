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
    cin >> Tests;
    FOR(test, 1, Tests+1) {
        printf("Case #%d: ", test);

        int N;
        cin >> N;

        vector<int> v;

        string l;
        REP(i, N) {
            cin >> l;
            int q = -1;
            for (int j = N-1; j >= 0; j--) {
                if (l[j] == '1') {
                    q = j;
                    break;
                }
            }
            v.pb(q);
        }

        int total_moves = 0;

        REP(i, N) {
            for (int j = i; j < N; j++) {
                if (v[j] <= i) {
                    total_moves += (j-i);
                    for (int k = j-1; k >= i; k--) {
                        swap(v[k+1], v[k]);
                    }
                    break;
                }
            }
        }

        cout << total_moves <<endl;

    }

}
