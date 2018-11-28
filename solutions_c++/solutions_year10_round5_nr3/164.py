/*
 * Author: Dumbear
 * Created Time:  2010/6/12 22:13:43
 * File Name: 
 */
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
#define out(v) cerr << #v << ": " << (v) << endl
#define SZ(v) ((int)(v).size())
const int maxint = -1u>>1;
template <class T> bool get_max(T& a, const T &b) {return b > a? a = b, 1: 0;}
template <class T> bool get_min(T& a, const T &b) {return b < a? a = b, 1: 0;}

int t, n, ans;
map<int, int> V;

void solve();
void dfs(int p, int v);

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d", &n);
    V.clear();
    for (int i = 0; i < n; ++i) {
        int p, v;
        scanf("%d%d", &p, &v);
        V[p] += v;
    }
    ans = 0;
    for (map<int, int>::iterator i = V.begin(); i != V.end(); ++i) {
        dfs(i->first, i->second);
    }
    printf("Case #%d: %d\n", ++t, ans);
}

void dfs(int p, int v) {
    if (v >= 2) {
        V[p - 1] += v / 2;
        V[p + 1] += v / 2;
        V[p] = v % 2;
        ans += v / 2;
        dfs(p - 1, V[p - 1]);
        dfs(p + 1, V[p + 1]);
    }
}
