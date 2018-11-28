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
#define ALL(a) a.begin(), a.end()
#define sqr(a) ((a) * (a))

typedef long long ll;


int main()
{
    int t;
    scanf("%d", &t);
    REP(i, t)
    {
        int n, k;
        scanf("%d%d", &n, &k);
        if (k % (1 << n) == (1 << n) - 1)
            printf("Case #%d: ON\n", i + 1);
        else
            printf("Case #%d: OFF\n", i + 1);
    }
}
