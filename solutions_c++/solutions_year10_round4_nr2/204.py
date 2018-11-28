#include <iostream>
#include <queue>
#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <list>
#include <sstream>
#include <cmath>
#include <ctime>
#include <algorithm>

using namespace std;

#define FOR(i, a, b) for (int i = (a); i < (b); i++)
#define FOD(i, a, b) for (int i = (a); i >= (b); i--)
#define REP(i, a) for (int i = 0; i < (a); i++)
#define sz(a) ((int)a.size())
#define cl clear()
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;

int m[1024];
int t[512][512];
int L;

ll solve(int l, int need, int p)
{
    if (l == L - 1)
    {
        if (need > min(m[p * 2 + 1], m[p * 2]))
            return 10000000;
        else if (need == min(m[p * 2 + 1], m[p * 2]))
            return t[l][p];
        else
            return 0;
    }
    ll rt = min(t[l][p] + solve(l + 1, need, p * 2) + solve(l + 1, need, p * 2 + 1), solve(l + 1, need + 1, p * 2) + solve(l + 1, need + 1, p * 2 + 1));
    return rt;
}

int main()
{
    int T;
    scanf("%d", &T);
    REP(ii, T)
    {
        int p;
        scanf("%d", &p);
        L = p;
        REP(i, (1 << p))
            scanf("%d", &m[i]);
        FOD(i, p - 1, 0)
            REP(j, (1 << i))
                scanf("%d", &t[i][j]);
        printf("Case #%d: %d\n", ii + 1, solve(0, 0, 0));
    }
}
