#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int T, tc;
long long l, t, n;
int dist[2000];
bool built[2000];
long long mintime;

void check() {
    int i;
    long long tmpt = 0;
    for (i = 0; i < n; i++) {
        if (built[i]) {
            if (t <= tmpt) {
                tmpt += dist[i];
            } else if (t < tmpt + 2 * dist[i]) {
                tmpt += (t - tmpt) + (dist[i] - (t - tmpt) / 2);
            } else {
                tmpt += dist[i] * 2;
            }
        } else {
            tmpt += dist[i] * 2;
        }
    }
    if (tmpt < mintime) mintime = tmpt;
}

void work(int k) {
    if (k >= l) {
        check();
        return;
    }
    int i;
    for (i = 0; i < n; i++) {
        if (built[i]) continue;
        built[i] = true;
        work(k + 1);
        built[i] = false;
    }
}

int main() {
    int c, aa;
    int i, j;

    freopen("B-small-attempt3.in", "r", stdin);
    freopen("B-small.out", "w", stdout);

    cin >> T;
    
    for (tc = 1; tc <= T; tc++) {
        cin >> l >> t >> n >> c;
        for (i = 0; i < c; i++) {
            cin >> aa;
            for (j = i; j < n; j += c) dist[j] = aa;
        }
        memset(built, 0, sizeof(built));
        mintime = 9223372036854775807LL;
        work(0);
        cout << "Case #" << tc << ": " << mintime << endl;
    }
    
    return 0;
}
