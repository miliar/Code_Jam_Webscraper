#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <queue>

using namespace std;

int dy[] = { 1, 0, -1, 0 };
int dx[] = { 0, 1, 0, -1 };

int ll, bb, rr, tt;

map<int, set<int> > vert;
map<int, set<int> > horz;

void add(int x1, int y1, int x2, int y2) {
    if (x1 == x2) {
        vert[y1 <? y2].insert(x1);
    } else {
        horz[x1 <? x2].insert(y1);
    }
}

int go();

int process() {
    vert.clear();
    horz.clear();

    int L; cin >> L;
    int x = 0, y = 0;
    int d = 0;
    int xx, yy;
    ll = rr = 0;
    bb = tt = 0;
    for (int i = 0; i < L; i++) {
        string s; int t; cin >> s >> t;
        for (int j = 0; j < t; j++) {
            for (int k = 0; k < s.size(); k++) {
                switch (s[k]) {
                    case 'F':
                        xx = x; yy = y;
                        x += dx[d]; y += dy[d];
                        ll <?= x; rr >?= x;
                        bb <?= y; tt >?= y;
                        add(xx, yy, x, y);
                        break;
                    case 'R':
                        d++; if (d == 4) d = 0;
                        break;
                    case 'L':
                        d--; if (d < 0) d = 3;
                        break;
                }
            }
        }
    }

    return go();
}

int go() {
    set<pair<int, int> > all;
    for (int y = bb; y < tt; y++) {
        set<int>& sx = vert[y];
        set<int>::iterator it = sx.begin();
        while (true) {
            if (it == sx.end()) break;
            it++;
            if (it == sx.end()) break;
            int first = *it;
            it++;
            if (it == sx.end()) break;
            for (int i = first; i < *it; i++)
                all.insert(make_pair(i, y));
        }
    }
    for (int x = ll; x < rr; x++) {
        set<int>& sy = horz[x];
        set<int>::iterator it = sy.begin();
        while (true) {
            if (it == sy.end()) break;
            it++;
            if (it == sy.end()) break;
            int first = *it;
            it++;
            if (it == sy.end()) break;
            for (int i = first; i < *it; i++)
                all.insert(make_pair(x, i));
        }
    }
    return all.size();
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        cout << "Case #" << t << ": " << process() << endl;
    }
    return 0;
}

