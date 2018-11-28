#define _CRT_SECURE_NO_DEPRECATE
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <ctime>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <math.h>
#include <queue>
#include <memory.h>
#include <iostream>
#include <stack>
#include <complex>
#include <list>

using namespace std;
 
void ASS(bool bb)
{
    if (!bb)
    {
        ++*(int*)0;
    }
}
 
#define FOR(i, x) for (int i = 0; i < (int)(x); i++)
#define CL(x) memset(x, 0, sizeof(x))
#define CLX(x, y) memset(x, y, sizeof(x))
 
#pragma comment(linker, "/STACK:106777216")
 
typedef vector<int> vi;

typedef long long LL;


struct S
{
    int r, x, y, id;
};

bool operator < (S a, S b)
{
    return a.r > b.r;
}

struct D
{
    int x, y, d;
    D()
    {
    }
    D(int xx, int yy, int dd)
    {
        x = xx;
        y = yy;
        d = dd;
    }
};

bool operator < (D a, D b)
{
    return a.x < b.x;
}

void Solve()
{
    int n, W, L;
    cin >> n >> W >> L;
    bool Swap = 0;
    if (W > L)
    {
        Swap = 1;
        swap(W, L);
    }
    vector<S> a(n);
    FOR(i, n) {
        cin >> a[i].r;
        a[i].id = i;
    }
    sort(a.begin(), a.end());
    vector<D> v;
    v.push_back(D(0, 0, L));
    FOR(i, n)
    {
        sort(v.begin(), v.end());
        int was = 0;
        FOR(j, v.size())
            if (v[j].d >= a[i].r * 2) {
                was = 1;
                D d = v[j];
                v.erase(v.begin() + j);
                a[i].x = min(W, d.x + a[i].r);
                a[i].y = min(L, d.y + a[i].r);
                v.push_back(D(d.x + a[i].r * 2, d.y, a[i].r * 2));
                v.push_back(D(d.x, d.y + a[i].r * 2, d.d - a[i].r * 2));
                break;
            }
        int x = was;
    }
    vector<S> ans(n);
    FOR(i, n)
        ans[a[i].id] = a[i];
    FOR(i, n) {
        if (Swap)
            swap(ans[i].x, ans[i].y);
        cout << " " << ans[i].x << " " << ans[i].y;
    }
    cout << endl;
}

int main()
{
    freopen("c:\\my\\in.txt", "r", stdin);
    freopen("c:\\my\\out.txt", "w", stdout);

    int t;
    cin >> t;
    FOR(i, t)
    {
        cout << "Case #" << (i + 1) << ":";
        Solve();
    }

    return 0;
}