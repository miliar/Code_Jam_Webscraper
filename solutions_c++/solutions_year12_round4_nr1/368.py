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

vi v;

bool Solve()
{
    int n;
    cin >> n;
    vi x(n + 1, 0);
    vi y(n + 1, 0);
    FOR(i, n)
        cin >> x[i] >> y[i];
    cin >> x.back();
    vi d(n + 1, -1);
    d[0] = x[0];
    FOR(i, d.size()) if (d[i] != -1) {
        for (int j = i + 1; j < (int)d.size(); j++)
            if (d[i] + x[i] >= x[j])
                d[j] = max(d[j], min(y[j], x[j] - x[i]));
    }
    return d.back() >= 0;
}

int main()
{
    freopen("c:\\my\\in.txt", "r", stdin);
    freopen("c:\\my\\out.txt", "w", stdout);

    int t;
    cin >> t;
    FOR(i, t)
    {
        cout << "Case #" << (i + 1) << ": ";
        if (Solve())
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}