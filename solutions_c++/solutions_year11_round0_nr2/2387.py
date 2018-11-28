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
    int c, d, n;
    scanf("%d ", &c);
    vector<vector<char> > opp(300, vector<char>(300, 0));
    vector<vector<char> > comp(300, vector<char>(300, 0));
    char buf[200] = {0};
    for (int i = 0; i < c; ++i) {
        scanf("%s ", buf);
        comp[buf[0]][buf[1]] = comp[buf[1]][buf[0]] = buf[2];
    }
    scanf("%d ", &d);
    for (int i = 0; i < d; ++i) {
        scanf("%s ", buf);
        opp[buf[0]][buf[1]] = opp[buf[1]][buf[0]] = true;
    }
    scanf("%d ", &n);
    scanf("%s", buf);
    vector<char> res;
    for (int i = 0; i < n; ++i) {
        if (res.size() == 0) {
            res.push_back(buf[i]);
            continue;
        }
        if (comp[buf[i]][res.back()]) {        
            char toPush = comp[buf[i]][res.back()];            
            res.pop_back();
            res.push_back(toPush);
            continue;
        }
        bool was = false;
        for (int j = 0; j < res.size(); ++j) {
            if (opp[res[j]][buf[i]]) {
                res.clear();
                was = true;
                break;
            }
        }
        if (!was) {
            res.push_back(buf[i]);
        }
    }
    printf("[");
    for (int i = 0; i < res.size(); ++i) {        
        printf("%c", res[i]);
        if (i != res.size() - 1) {
            printf(", ");
        }
    }
    printf("]\n");
}

int main() {

    //freopen("in.in", "rt", stdin);
    //freopen("out.out", "wt", stdout);

    freopen("B-small.in", "rt", stdin);
    freopen("B-small.out", "wt", stdout);

    //freopen("B-large.in", "rt", stdin);
    //freopen("B-large.out", "wt", stdout);

    int t = 0;
    scanf("%d\n", &t);
    for (int tt = 0; tt < t; tt++) {
        printf("Case #%d: ", tt + 1);
        solution();
    }

    return 0;
}