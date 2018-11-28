#pragma comment(linker, "/STACK:64000000")
#define _CRT_SECURE_NO_DEPRECATE
#include <cmath>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <queue>
#include <deque>
#include <algorithm>
#include <stack>

using namespace std;

#define mp make_pair
#define pb push_back
#define all(v) v.begin(), v.end()

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define for1(i, n) for (int i = 1; i <= (int)(n); i++)
#define forv(i, v) forn(i, v.size())

typedef pair<int, int> pii;
typedef long long ll;

#define NMAX 2005

int r[NMAX];
int n;
int w, h;
int x[NMAX], y[NMAX];
int vx[NMAX], vy[NMAX];
pii tmp[NMAX];
int wh[NMAX];

inline bool intersect(int l1, int r1, int l2, int r2)
{
    return max(l1, l2) < min(r1, r2);
}

inline bool intersect(int x1, int y1, int r1, int x2, int y2, int r2)
{
    return intersect(x1 - r1, x1 + r1, x2 - r2, x2 + r2) && intersect(y1 - r1, y1 + r1, y2 - r2, y2 + r2);
}

void place(int id)
{
    int cx = 0, cy = 0;
    vx[cx++] = 0;
    vy[cy++] = 0;

    forn(i, id)
    {
        vx[cx++] = x[i] + r[i] + r[id];
        vy[cy++] = y[i] + r[i] + r[id];
    } 

    sort(vx, vx + cx);
    sort(vy, vy + cy);

    forn(i, cx)
    {
        if (vx[i] > w) break;
        forn(j, cy)
        {
            if (vy[j] > h) break;

            bool ok = true;

            forn(k, id)
            {
                if (intersect(x[k], y[k], r[k], vx[i], vy[j], r[id]))
                {
                    ok = false;
                    break;
                }    
            } 

            if (ok)
            {
                x[id] = vx[i];
                y[id] = vy[j];
                return;
            }
        }
    } 

    throw;
}

void solve(int tc)
{
    cerr << tc << endl;
    printf("Case #%d: ", tc);
    cin >> n >> w >> h;

    w *= 2;
    h *= 2;

    forn(i, n) cin >> r[i];

    forn(i, n) tmp[i] = mp(r[i], i);

    sort(tmp, tmp + n);
    reverse(tmp, tmp + n);

    forn(i, n) r[i] = tmp[i].first;

    forn(i, n) wh[tmp[i].second] = i;

    forn(i, n) r[i] *= 2;

    forn(i, n)
    {
        place(i);
    }

    forn(i, n)
    {
        int j = wh[i];
        printf("%.2lf %.2lf ", x[j] * 0.5 , y[j] * 0.5);
    }

    printf("\n");
}

int main()
{
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    int tc;
    cin >> tc;
    forn(it, tc) solve(it + 1);
    return 0;
}
