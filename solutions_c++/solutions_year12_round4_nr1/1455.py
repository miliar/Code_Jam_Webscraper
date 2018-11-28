#include <algorithm>
#include <cstdio>
#include <iostream>
#include <map>
#include <queue>
#include <vector>
using namespace std;
#define For(i,x) for (int i=0; i<(int)(x); i++)
#define mp make_pair

bool calc(int len, vector<pair<int, int> >& v) {
    map<pair<int, int>, int> used; // pair<pos, vine>

    queue<pair<int, int> > q; // pair<pos, vine>
    q.push(mp(0, 0));
    while (!q.empty()) {
        int pos = q.front().first;
        int vine = q.front().second;
        q.pop();

        if (v[vine].first + (v[vine].first - pos) >= len) return true;

        if (used[mp(pos, vine)]++) continue;

        const int d = v[vine].first - pos;
        for (int i = vine+1; i < (int)v.size(); i++) {
            if (pos + d * 2 >= v[i].first) {
                // v[vine].first
                // v[i].first - v[i].second
                const int pos2 = max(v[vine].first, v[i].first - v[i].second);
                q.push(mp(pos2, i));
            }
            else break;
        }

    }
    return false;
}

int main() {
    int ncases;
    scanf("%d", &ncases);

    For(cc, ncases) {
        int n;
        scanf("%d", &n);

        vector<pair<int, int> > v;
        For(i, n) {
            int a, b;
            scanf("%d %d", &a, &b);
            v.push_back(mp(a, b));
        }

        int len;
        scanf("%d", &len);
        printf("Case #%d: %s\n", cc+1, calc(len, v) ? "YES" : "NO");
    }
}




