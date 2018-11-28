#include <algorithm>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <utility>
#include <vector>
using namespace std;
typedef pair<int, int> pii;

int main()
{
    char line[199200];
    int T, n;
    scanf("%d%*c", &T);
    for (int t = 1; t <= T; t++) {
        char who;
        int where, m;
        vector<pii> a[2];
        gets(line);
        stringstream ss(line);
        ss >> m;
        for (int i = 0; i < m; i++) {
            ss >> who >> where;
            a[who == 'O'].push_back(pii(where, i));
        }

        int p[2] = {1, 1}, it[2] = {}, res = 0;
        while (it[0] < a[0].size() || it[1] < a[1].size()) {
            int first = it[0] == a[0].size() || it[1] < a[1].size() && a[1][it[1]].second < a[0][it[0]].second, time = abs(p[first]-a[first][it[first]].first)+1;
            res += time;
            for (int j = 0; j < 2; j++)
                if (it[j] < a[j].size()) {
                    int dist = abs(p[j]-a[j][it[j]].first);
                    if (dist + (j == first) <= time) {
                        p[j] = a[j][it[j]].first;
                        if (j == first) it[j]++;
                    } else {
                        if (p[j] < a[j][it[j]].first) {
                            p[j] += time;
                            p[j] = min(p[j], a[j][it[j]].first);
                        }
                        else {
                            p[j] -= time;
                            p[j] = max(p[j], a[j][it[j]].first);
                        }
                    }
                }
        }
        printf("Case #%d: %d\n", t, res);
    }
}
