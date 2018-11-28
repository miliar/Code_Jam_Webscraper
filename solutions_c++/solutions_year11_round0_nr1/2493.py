#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> pi;
typedef unsigned long long ull;

#define x first
#define y second
#define mp make_pair


void solution() {
    int n;
    scanf("%d ", &n);
    vector<pi> pos[2];
    for (int i = 0; i < n; ++i) {
        int b;
        char bot;
        scanf("%c %d ", &bot, &b);
        if (bot == 'O') {
            pos[0].push_back(mp(i, b));
        } else {
            pos[1].push_back(mp(i, b));
        }
    }
    int turn = 1;
    int curr[2] = {0};
    int currPos[2] = {1, 1};    
    for (;; ++turn) {
        bool was[2] = {0};
        for (int i = 0; i < 2; ++i) {
            if (curr[i] < pos[i].size() && 
                (curr[1 - i] == pos[1 - i].size() || pos[i][curr[i]].x < pos[1 - i][curr[1 - i]].x) && 
                currPos[i] == pos[i][curr[i]].y) {

                ++curr[i];
                was[i] = true;
                break;
            }
        }
        for (int i = 0; i < 2; ++i) {
            if (!was[i] && curr[i] < pos[i].size() && currPos[i] != pos[i][curr[i]].y) {
                int delta = currPos[i] < pos[i][curr[i]].y ? 1 : -1;
                currPos[i] += delta;
            }
        }

        if (curr[0] == pos[0].size() && curr[1] == pos[1].size()) {
            break;
        }
    }
    printf("%d\n", turn);
}

int main() {

    //freopen("in.in", "rt", stdin);
    //freopen("out.out", "wt", stdout);

    //freopen("A-small.in", "rt", stdin);
    //freopen("A-small.out", "wt", stdout);

    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);

    //freopen("B-small.in", "rt", stdin);
    //freopen("B-small.out", "wt", stdout);

    //freopen("B-large.in", "rt", stdin);
    //freopen("B-large.out", "wt", stdout);


    //freopen("C-small.in", "rt", stdin);
    //freopen("C-small.out", "wt", stdout);

    //freopen("C-large.in", "rt", stdin);
    //freopen("C-large.out", "wt", stdout);

    int t = 0;
    scanf("%d\n", &t);
    for (int tt = 0; tt < t; tt++) {
        printf("Case #%d: ", tt + 1);
        solution();
    }

    return 0;
}