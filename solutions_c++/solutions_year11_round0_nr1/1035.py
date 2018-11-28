#include <iostream>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <cstdio>

using namespace std;

int n;
int p[105];
char r[105];

queue<int> q;
int dist[105][105][105];

int main() {
    freopen("robot.in", "r", stdin);
    freopen("robot.out", "w", stdout);
    int tests; cin >> tests;
    for (int testID = 1; testID <= tests; ++testID) {
        cin >> n;
        for (int i = 0; i < n; ++i)
            cin >> r[i] >> p[i];
        while (!q.empty()) q.pop();
        q.push(0);
        q.push(1);
        q.push(1);
        memset(dist, -1, sizeof(dist));
        dist[0][1][1] = 0;
        while (!q.empty()) {
            int at = q.front(); q.pop();
            int orange = q.front(); q.pop();
            int blue = q.front(); q.pop();
            if (at == n) {
                cout << "Case #" << testID << ": " << dist[at][orange][blue] << endl;
                break;
            }
            for (int d1 = -1; d1 <= 1; ++d1)
                for (int d2 = -1; d2 <= 1; ++d2) {
                    int norange = orange + d1;
                    int nblue = blue + d2;
                    if (norange < 1 || norange > 100) continue;
                    if (nblue < 1 || nblue > 100) continue;
                    if (dist[at][norange][nblue] != -1) continue;
                    dist[at][norange][nblue] = dist[at][orange][blue] + 1;
                    q.push(at);
                    q.push(norange);
                    q.push(nblue);
                }
            if (r[at] == 'O' && p[at] == orange) {
                for (int d2 = -1; d2 <= 1; ++d2) {
                    int norange = orange;
                    int nblue = blue + d2;
                    if (norange < 1 || norange > 100) continue;
                    if (nblue < 1 || nblue > 100) continue;
                    if (dist[at + 1][norange][nblue] != -1) continue;
                    dist[at + 1][norange][nblue] = dist[at][orange][blue] + 1;
                    q.push(at + 1);
                    q.push(norange);
                    q.push(nblue);
                }
            }
            if (r[at] == 'B' && p[at] == blue) {
                for (int d1 = -1; d1 <= 1; ++d1) {
                    int norange = orange + d1;
                    int nblue = blue;
                    if (norange < 1 || norange > 100) continue;
                    if (nblue < 1 || nblue > 100) continue;
                    if (dist[at + 1][norange][nblue] != -1) continue;
                    dist[at + 1][norange][nblue] = dist[at][orange][blue] + 1;
                    q.push(at + 1);
                    q.push(norange);
                    q.push(nblue);
                }
            }
        }
    }
    return 0;
}
