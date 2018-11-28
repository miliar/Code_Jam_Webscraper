#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iterator>
#include <functional>
#include <utility>
#include <numeric>
#include <complex>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) ((c).begin()), ((c).end())

struct Train {
    int side;
    int start;
    int goal;
};

int readTime() {
    int h, m;
    scanf("%d:%d", &h, &m);
    return h*60+m;
}

int n;
vector< vector<int> > g;

vector<bool> visited;
vector<int> matching;
 
bool augment(int left) {
    if (left < 0)
        return true;
    if (visited[left])
        return false;
    visited[left] = true;
    REP(i, g[left].size()) {
        int right = g[left][i];
        if (augment(matching[right])) {
            matching[right] = left;
            return true;
        }
    }
    return false;
}
void match() {
    matching.assign(n, -1);
    REP(left, n) {
        visited.assign(n, false);
        augment(left);
    }
}

int main() {

    int nCases;
    cin >> nCases;

    REP(iCase, nCases) {

        int penalty;
        cin >> penalty;

        int left, right;
        cin >> left >> right;

        vector<Train> trains;
        REP(i, left+right) {
            Train t;
            t.side = (i < left ? 0 : 1);
            t.start = readTime();
            t.goal = readTime() + penalty;
            trains.push_back(t);
        }

        n = left+right;
        g.clear();
        g.resize(n);
        REP(i, n) {
            Train& a = trains[i];
            REP(j, n) {
                Train& b = trains[j];
                if (a.side != b.side && b.start >= a.goal)
                    g[i].push_back(j);
            }
        }

        match();
        int res_left = left, res_right = right;
        REP(i, n)
            if (matching[i] >= 0)
                (i < left ? res_left : res_right)--;

        cout << "Case #" << iCase+1 << ": ";
        cout << res_left << " " << res_right << endl;

    }

    return 0;
}
