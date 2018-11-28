#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <math.h>
using namespace std;

#define FOR(i,s,e) for (int i = int(s); i != int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
typedef pair<int, int> P;

string rpi(vector<string>& lis) {
    int size = lis.size();
    //    vector<double> ret;
    vector<double> wp, owp, oowp;
    vector<int> matches;
    vector<P> wins_loses;
    //    ret.assign(size, 0);
    wp.assign(size, 0);
    owp.assign(size, 0);
    oowp.assign(size, 0);
    matches.assign(size, 0);
    wins_loses.assign(size, P(0, 0) );

    FOR(i, 0, size) {
        int wins = 0;
        int loses = 0;
        FORIT(it, lis[i]) {
            if (*it == '0')
                ++loses;
            else if (*it == '1')
                ++wins;
        }
        wp[i] = (double)wins / (loses + wins);
        wins_loses[i] = P(wins, loses);
        //        cout << wp[i] << ',';
    }
    //    cout << endl;

    FOR(i, 0, size) {
        double total = 0;
        FOR(j, 0, size) {
            if (i == j) continue;
            if (lis[i][j] != '.') {
                if (lis[j][i] == '1') {
                    total += (double)(wins_loses[j].first - 1) / (wins_loses[j].first + wins_loses[j].second - 1);
                } else if (lis[j][i] == '0') {
                    total += (double)(wins_loses[j].first ) / (wins_loses[j].first + wins_loses[j].second - 1);
                } else {
                    total += wp[j];
                }
            }
            //            cout << total << endl;
        }
        owp[i] = total / (wins_loses[i].first + wins_loses[i].second);
        //        cout << owp[i] << ',';
    }
    //    cout << endl;

    FOR(i, 0, size) {
        double total = 0;
        FOR(j, 0, size) {
            if (i == j)  continue;
            if (lis[i][j] != '.')
                total += owp[j];
        }
        oowp[i] = total / (wins_loses[i].first + wins_loses[i].second);
    }

    string ret("\n");
    char buf[256];
    FOR(i, 0, size) {
        sprintf(buf, "%.8f\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
        ret += buf;
    }
    return ret;
}

string gcjMain() {
    int N;
    scanf("%d\n", &N);

    vector<string> lis;
    FOR(i, 0, N) {
        char buf[256];
        scanf("%s\n", buf);
        lis.push_back(buf);
    }

    return rpi(lis);
}

int main(void) {
    int n;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; ++i) {
        printf("Case #%d: %s", i, gcjMain().c_str());
    }
}

