#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
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
#include <ctime>
#include <iostream>

using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define SIZE(s) int((s).size())
#define FILL0(a) memset(a, 0, sizeof(a))
#define FILL1(a) memset(a, -1, sizeof(a))

typedef pair<int, int> PII;

vector<int> getRes(int T, vector< vector<PII> >& paths) {
    sort(ALL(paths[0]));
    sort(ALL(paths[1]));
    vector< vector<bool> > used(2, vector<bool>(105, false));

    vector<int> res(2, 0);
    vector<int> n(2);
    n[0] = SIZE(paths[0]);
    n[1] = SIZE(paths[1]);
    while (1) {
        vector<int> ind(2, 0);
        int min0 = 5000, min1 = 5000;
        for (int i = 0; i < n[0]; ++i) {
            if (!used[0][i]) {
                ind[0] = i;
                min0 = paths[0][i].first;
                break;
            }
        }
        for (int i = 0; i < n[1]; ++i) {
            if (!used[1][i]) {
                ind[1] = i;
                min1 = paths[1][i].first;
                break;
            }
        }
        if (min0 == 5000 && min1 == 5000)
            break;
        int next_turn = min0 < min1? 0: 1;
        int next_time = paths[next_turn][ind[next_turn]].first;
        ++res[next_turn];

        while (1) {
            while (ind[next_turn] < n[next_turn] &&
                    (paths[next_turn][ind[next_turn]].first < next_time || used[next_turn][ind[next_turn]]))
            {
                ++ind[next_turn];
            }
            if (ind[next_turn] >= n[next_turn])
                break;
            used[next_turn][ind[next_turn]] = true;
            next_time = paths[next_turn][ind[next_turn]].second;
            int mins = next_time % 100 + T;
            next_time /= 100;
            next_time *= 100;
            while (mins >= 60) {
                mins -= 60;
                next_time += 100;
            }
            next_time += mins;
            next_turn = 1 - next_turn;
        }
    }

    return res;
}

int main()
{
    int n;
    cin >> n;
    for (int i = 1; i <= n; ++i) {
        int T, NA, NB;
        cin >> T >> NA >> NB;
        vector< vector<PII> > paths(2);
        paths[0].resize(NA);
        for (int j = 0; j < NA; ++j) {
            string s;
            cin >> s;
            paths[0][j].first = atoi(&s[0]) * 100 + atoi(&s[3]);
            cin >> s;
            paths[0][j].second = atoi(&s[0]) * 100 + atoi(&s[3]);
        }
        paths[1].resize(NB);
        for (int j = 0; j < NB; ++j) {
            string s;
            cin >> s;
            paths[1][j].first = atoi(&s[0]) * 100 + atoi(&s[3]);
            cin >> s;
            paths[1][j].second = atoi(&s[0]) * 100 + atoi(&s[3]);
        }

        vector<int> res(2);
        if (NA == 0 || NB == 0) {
            res[0] = NA;
            res[1] = NB;
        }
        else {
            res = getRes(T, paths);
        }
        printf("Case #%d: %d %d\n", i, res[0], res[1]);
    }

    return 0;
}
