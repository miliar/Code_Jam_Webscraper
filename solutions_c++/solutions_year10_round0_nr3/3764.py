/*
 * Author: iSea
 * Created Time:  2010/5/8 20:09:57
 * File Name: C.cpp
 */
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <queue>
#include <vector>
#include <map>

using namespace std;

const int maxn = 1000 + 10;
const int inf = (-1u) >> 1;

int Case = 1, r, k, n;
int g[maxn], first[maxn];
int cycle_begin_num, cycle_num, begin_num;
long long totot;

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
        long long tot = 0;
        int bnow = now;
        while (tot + g[now] <= k) {
            tot += g[now];
            now = (now + 1) % n;
            if (now == bnow)
                break;
        }
        totot += tot;
        ++cnt;
        if (first[now] == -1)
            first[now] = cnt;
        else
            break;
    }
    cycle_begin_num = now;
    cycle_num = cnt - first[now];
    begin_num = first[now];
}

long long get_on(int& cur) {
    long long res = 0;
    int tcur = cur;
    while (res + g[cur] <= k) {
        res += g[cur];
        cur = (cur + 1) % n;
        if (cur == tcur)
            break;
    }
    return res;
}

long long get_on_time(int times, int begins) {
    int cnt = 0, ans = 0;
    while (cnt++ < times)
        ans += get_on(begins);
    return ans;
}

void solve() {
    printf ("Case #%d: ", Case++);
    get_cycle();
    if (r <= begin_num) {
        printf ("%I64d\n", get_on_time(r, 0));
        return ;
    }
    long long ans = get_on_time(begin_num, 0);
    totot -= ans;
    r -= begin_num;
    ans += ((long long)r / cycle_num) * totot;
    r %= cycle_num;
    ans += get_on_time(r, cycle_begin_num);
    printf ("%I64d\n", ans);
}

int main() {
    freopen ("out.txt", "w", stdout);
    
    int testCase;
    scanf ("%d\n", &testCase);
    while (testCase--) {
        init();
        solve();
    }
    
    return 0;
}

