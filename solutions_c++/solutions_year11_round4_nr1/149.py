#include <iostream> 
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

pair<int, pair<int, int> > a[1010];
int len, n, v_walk, v_run, max_time;

void init() {
    scanf("%d%d%d%d%d", &len, &v_walk, &v_run, &max_time, &n);
    for (int i = 1; i <= n; i ++)
        scanf("%d%d%d", &a[i].second.first, &a[i].second.second, &a[i].first);
}

double tot_time, rest;

void cal(int _len, int _v) {
    double len = (double)_len;
    double v = (double)_v;
    double v2 = (double)(_v-v_walk+v_run);
    double tt = len / v2;
    if (tt <= rest) {
        rest -= tt;
        tot_time += tt;
    } else {
        tot_time += rest;
        len -= rest*v2;
        rest = 0.0;
        tot_time += len / v;
    }
}

void solve(int case_index) {
    sort(a+1, a+n+1);
    for (int i = 1; i <= n; i ++)
        len -= a[i].second.second - a[i].second.first;
    rest = (double)max_time;
    tot_time = 0.0;
    cal(len, v_walk);
    for (int i = 1; i <= n; i ++)
        cal(a[i].second.second-a[i].second.first, a[i].first+v_walk);
    printf("Case #%d: %.9lf\n", case_index, tot_time);
}

int main() {
    freopen("a-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int case_count;
    scanf("%d", &case_count);
    for (int i = 1; i <= case_count; i ++) {
        init();
        solve(i);
    }
    return 0;
}
