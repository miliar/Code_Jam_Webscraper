#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

#define N 10

int n, m;
int st[N], ed[N];
vector < vector < int > > v;
int a[N];

bool ch(int lim) {
    bool ha[10] = {0};
    for (int i = 0; i < n; ++i)
        ha[ a[i] ] = 1;
    for (int i = 0; i < lim; ++i)
        if (!ha[i])
            return 0;
    for (vector < vector < int > >::iterator it = v.begin(); it != v.end(); ++it) {
        memset(ha, 0, sizeof(ha));
        for (vector < int >::iterator jt = it->begin(); jt != it->end(); ++jt)
            ha[ a[*jt] ] = 1;
        for (int i = 0; i < lim; ++i)
            if (!ha[i])
                return 0;
    }
    return 1;
}

bool dfs(int k, int lim) {
    if (k == n)
        return ch(lim);
    for (int i = 0; i < lim; ++i) {
        a[k] = i;
        if (dfs(k+1, lim)) return 1;
    }
    return 0;
}

int solve() {
    scanf("%d %d", &n, &m);
    for (int i = 0; i < m; ++i) {
        scanf("%d", &st[i]);
        --st[i];
    }
    for (int i = 0; i < m; ++i) {
        scanf("%d", &ed[i]);
        --ed[i];
        if (st[i] > ed[i]) swap(st[i], ed[i]);
    }

    v.clear();
    vector < int > iv;
    for (int i = 0; i < n; ++i)
        iv.push_back(i);
    v.push_back(iv);

    for (int i = 0; i < m; ++i) {
        vector < vector < int > > newv;
        for (vector < vector < int > >::iterator it = v.begin(); it != v.end(); ++it) {
            int cc = 0;
            for (vector < int >::iterator jt = it->begin(); jt != it->end(); ++jt) {
                if (*jt == st[i]) cc |= 1;
                if (*jt == ed[i]) cc |= 2;
                if (cc == 3) break;
            }
            if (cc == 3) {
                vector < int > v1, v2;
                sort(it->begin(), it->end());
                for (vector < int >::iterator jt = it->begin(); jt != it->end(); ++jt)
                    if (st[i] < *jt && *jt < ed[i])
                        v1.push_back(*jt);
                    else
                        v2.push_back(*jt);
                v1.push_back(st[i]); v1.push_back(ed[i]);
                newv.push_back(v1);
                newv.push_back(v2);
            } else
                newv.push_back(*it);
        }
        v = newv;
    }
    int ret = 1;
    while (dfs(0, ret)) ++ret;
    dfs(0, --ret);
    return ret;
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int t, cas = 0;
    scanf("%d", &t);
    while (t--) {
        printf("Case #%d: %d\n", ++cas, solve());
        for (int i = 0; i < n-1; ++i)
            printf("%d ", a[i]+1);
        printf("%d\n", a[n-1]+1);
    }
    return 0;
}
