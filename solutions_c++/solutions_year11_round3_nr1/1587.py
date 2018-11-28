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

string gcjMain() {
    int R, C;
    scanf("%d %d\n", &R, &C);

    vector<string> lis;
    FOR(i, 0, R) {
        char buf[256];
        scanf("%s\n", buf);
        lis.push_back(buf);
    }

    bool found = true;
    while (found) {
        found = false;

        FOR(i, 0, R) {
            FOR(j, 0, C) {
                if (lis[i][j] == '#') {
                    found = true;

                    if (j+1 < C && lis[i][j+1] == '#' &&
                        i+1 < R && lis[i+1][j] == '#' &&
                        lis[i+1][j+1] == '#') {
                        lis[i][j] = '/'; lis[i][j+1] = '\\';
                        lis[i+1][j] = '\\'; lis[i+1][j+1] = '/';
                    } else {
                        return "\nImpossible\n";
                    }
                    goto loop;
                }
            }
        }
    loop:;
    }

    string ret("\n");

    FORIT(it, lis) {
        ret += *it;
        ret += "\n";
    }
    return ret;
}

int main(void) {
    int n;
    scanf("%d\n", &n);
    for (int i = 1; i <= n; ++i) {
        printf("Case #%d:%s", i, gcjMain().c_str());
    }
}

