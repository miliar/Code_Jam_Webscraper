#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int maxn = 1000 + 10;
const int inf = (-1u) >> 1;

int Case = 1, r, k, n;
int g[maxn], first[maxn];
int cycle_begin_num, cycle_num, begin_num, totot;

void init() {
    scanf ("%d%d%d", &r, &k, &n);
    for (int i = 0; i < n; ++i)
        scanf ("%d", &g[i]);
}

void get_cycle() {
    fill (first, first + n, -1);
    first[0] = 0;
    int now = 0, cnt = 0;
    totot = 0;
    while (true) {
        int tot = 0, bnow = now;
        while (tot + g[now] <= k) {
            tot += g[now];
            now = (now + 1) % n;
            if (now == bnow)
                break;
        }
        totot += tot;
        ++cnt;
        //printf ("now %d first[now] %d\n", now, first[now]);
        if (first[now] == -1)
            first[now] = cnt;
        else
            break;
    }
    cycle_begin_num = now;
    cycle_num = cnt - first[now];
    begin_num = first[now];
}

int get_on(int& cur) {
    int res = 0, tcur = cur;
    while (res + g[cur] <= k) {
        res += g[cur];
        cur = (cur + 1) % n;
        if (cur == tcur)
            break;
    }
    return res;
}

int get_on_time(int times, int begins) {
    int cnt = 0, ans = 0;
    while (cnt++ < times)
        ans += get_on(begins);
    return ans;
}

void solve() {
    printf ("Case #%d: ", Case++);
    get_cycle();
    if (r <= begin_num) {
        printf ("%d\n", get_on_time(r, 0));
        return ;
    }
    int ans = get_on_time(begin_num, 0);
    totot -= ans;
    r -= begin_num;
    ans += (r / cycle_num) * totot;
    r %= cycle_num;
    ans += get_on_time(r, cycle_begin_num);
    printf ("%d\n", ans);
}

#define SMALL
//#define LARGE

int main() {
    string name = "C";
    #ifdef SMALL
    freopen ((name + "-small-attempt1.in").c_str(), "r", stdin);
    freopen ((name + "-small.out").c_str(), "w", stdout);
    #endif
    #ifdef LARGE
    freopen ((name + "-large.in").c_str(), "r", stdin);
    freopen ((name + "-large.out").c_str(), "w", stdout);
    #endif
    
    int testCase;
    scanf ("%d\n", &testCase);
    while (testCase--) {
        init();
        solve();
    }
    
    return 0;
}

