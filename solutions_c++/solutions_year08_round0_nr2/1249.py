#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

#define MAXN 1000000000
typedef long long LL;

class state {
public:
    int start;
    int end;
};

vector<state> mma(105);
vector<state> mmb(105);

void run() {
    int turn;
    int na, nb;
    cin >> turn;
    cin >> na >> nb;
    for (int i = 0; i < na; ++i) {
        string s1, s2;
        cin >> s1 >> s2;
        int tt[4];

        tt[0] = s1[0] - '0', tt[1] = s1[1] - '0', tt[2] = s1[3] - '0', tt[3] = s1[4] - '0';
        mma[i].start = (tt[0] * 10 + tt[1]) * 60 + (tt[2] * 10 + tt[3]);
        
        tt[0] = s2[0] - '0', tt[1] = s2[1] - '0', tt[2] = s2[3] - '0', tt[3] = s2[4] - '0';
        mma[i].end = (tt[0] * 10 + tt[1]) * 60 + (tt[2] * 10 + tt[3]);
    }

    for (int i = 0; i < nb; ++i) {
        string s1, s2;
        cin >> s1 >> s2;
        int tt[4];

        tt[0] = s1[0] - '0', tt[1] = s1[1] - '0', tt[2] = s1[3] - '0', tt[3] = s1[4] - '0';
        mmb[i].start = (tt[0] * 10 + tt[1]) * 60 + (tt[2] * 10 + tt[3]);

        tt[0] = s2[0] - '0', tt[1] = s2[1] - '0', tt[2] = s2[3] - '0', tt[3] = s2[4] - '0';
        mmb[i].end = (tt[0] * 10 + tt[1]) * 60 + (tt[2] * 10 + tt[3]);
    }

    int reta = 0, retb = 0;
    int dda = 0, ddb = 0;

    for (int k = 0; k < 1440; ++k) {
        for (int i = 0; i < na; ++i) {
            if (k == mma[i].end + turn) {
                ++ddb;
            }
        }
        for (int i = 0; i < nb; ++i) {
            if (k == mmb[i].end + turn) {
                ++dda;
            }
        }
        for (int i = 0; i < na; ++i) {
            if (k == mma[i].start) {
                if (dda > 0) {
                    --dda;
                } else {
                    ++reta;
                }
            }
        }
        for (int i = 0; i < nb; ++i) {
            if (k == mmb[i].start) {
                if (ddb > 0) {
                    --ddb;
                } else {
                    ++retb;
                }
            }
        }
    }

    cout << reta << " " << retb << endl;
}

int main() {
    int kase;
    cin >> kase;
    for (int k = 1; k <= kase; ++k) {
        cout << "Case #" << k << ": ";
        run();
    }
    return 0;
}
