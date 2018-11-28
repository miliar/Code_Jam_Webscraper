#include <cstdio>
#include <iostream>
#include <algorithm>
#include <functional>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <cmath>
#include <cstdlib>
using namespace std;

#define MP make_pair
#define FF first
#define CC second
#define SS size()
#define PB push_back
#define BB begin()
#define EE end()
#define all(x)  (x).begin(), (x).end()
#define for0(a,b) for (int a = 0; a < (b); ++a)
#define for1(a,b) for (int a = 1; a < (b); ++a)

typedef long long LL;
typedef vector<int> vint;
typedef pair<int, int> pii;

#define EPS (1e-7)



int main() {
    int t;
    cin >> t;

    for0 (tcase, t) {
        set<pii> initial;
        int r;

        cin >> r;
        for0 (i, r) {
            int x1, x2, y1, y2;
            cin >> x1 >> y1 >> x2 >> y2;
            for (int y = y1; y <= y2; y++) {
                for (int x = x1; x <= x2; x++) {
                    initial.insert(MP(x, y));
                }
            }
        }

        int steps = 0;
        set<pii> next;
        set<pii> *current = &initial;
        set<pii> *future  = &next;
        while (current->SS >= 1) {
            steps++;
            //printf("Step %d. Current has %d\n", steps, current->SS);
            for (set<pii>::iterator it = current->BB;
            it != current->EE; ++it) {
                pii tcell = *it;
                pii north = tcell;
                pii west = tcell;
                pii south = tcell;
                pii east = tcell;
                north.second -= 1;
                south.second += 1;
                west.first -= 1;
                east.first += 1;
                pii northeast = tcell;
                pii southwest = tcell;
                northeast.first += 1;
                northeast.second -= 1;
                southwest.first -= 1;
                southwest.second += 1;
                
                if (current->count(west) || current->count(north))
                    future->insert(tcell);
                if (current->count(northeast))
                    future->insert(east);
                if (current->count(southwest))
                    future->insert(south);
            }

            set<pii> *swap = current;
            current = future;
            future = swap;
            future->clear();
        }

        printf("Case #%d: %d\n", tcase+1, steps);
    }

    return 0;
}

