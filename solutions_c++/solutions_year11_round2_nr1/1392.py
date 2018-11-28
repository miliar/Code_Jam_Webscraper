#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <complex>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <climits>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cassert>

using namespace std;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<(n); ++i)
#define FOR(var,start,end) for (int var=(start); var<=(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(end); --var)
#define FOREACH(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

// typedef long long LL;
typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<bool> VB;
typedef vector< vector<int> > VVI;
typedef vector< vector<bool> > VVB;

struct Team {
    Team() {
        wp = 0.0;
        owp = 0.0;
        oowp = 0.0;
    }

    double wp;
    double owp;
    double oowp;
};

int main() {
    int nTests = 0;
    cin >> nTests;

    FOR (test, 1, nTests) {

        int nTeams = 0;
        cin >> nTeams;

        vector<string> table;
        REP (i, nTeams) {
            string line;
            cin >> line;
            table.PB(line);
        }

        // REP (i, nTeams) {
        //     cout << table[i] << endl;
        // }

        vector<Team> teams(nTeams, Team());
        REP (i, nTeams) {
            int gamesPlayed = 0;
            REP (j, nTeams) {
                teams[i].wp += (table[i][j] == '1') ? 1.0 : 0.0;
                if (table[i][j] != '.') {
                    ++gamesPlayed;
                }
            }
            // cout << gamesPlayed << endl;
            // cout << teams[i].wp << endl;
            teams[i].wp /= (double)gamesPlayed;
            // cout << "wp: " << teams[i].wp << endl;
            double owp = 0.0;
            int cnt = 0;
            REP (k, nTeams) {
                if (i != k && table[k][i] != '.') {
                    ++cnt;
                    int gamesPlayed = 0;
                    double wp = 0.0;
                    REP (l, nTeams) {
                        if (l != i) {
                            wp += (table[k][l] == '1') ? 1.0 : 0.0;
                            if (table[k][l] != '.') {
                                ++gamesPlayed;
                            }
                        }
                    }
                    wp /= (double)gamesPlayed;
                    // cout << "wp2: " << wp << endl;
                    owp += wp;
                }
            }
            // cout << owp << endl;
            if (cnt > 0) {
                owp /= cnt;
            }
            teams[i].owp = owp;
            // cout << "owp: " << teams[i].owp << endl;
        }

        REP (i, nTeams) {
            double oowp = 0.0;
            int cnt = 0;
            REP (k, nTeams) {
                if (i != k && table[k][i] != '.') {
                    oowp += teams[k].owp;
                    ++cnt;
                }
            }
            if (cnt > 0) {
                oowp /= cnt;
            }
            teams[i].oowp = oowp;
        }

        cout << "Case #" << test << ":\n";

        REP (i, nTeams) {
            Team t = teams[i];
            printf("%.15f\n", 0.25 * t.wp + 0.50 * t.owp + 0.25 * t.oowp);
        }
    }

    return 0;
}
