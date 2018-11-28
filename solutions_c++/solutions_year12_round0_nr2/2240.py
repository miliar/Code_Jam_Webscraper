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

void ASS(bool b)
{
    if (!b)
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

int bb[1024][2];

void Init()
{
    CLX(bb, 0xFF);
    FOR(i, 11)
        FOR(j, 11)
            FOR(k, 11)
            {
                vi v;
                v.push_back(i);
                v.push_back(j);
                v.push_back(k);
                sort(v.begin(), v.end());
                if (v[2] - v[0] > 2)
                    continue;
                int tot = i + j + k;
                int best = v[2];
                if (v[2] - v[0] == 2)
                    bb[tot][1] = max(bb[tot][1], best);
                else
                    bb[tot][0] = max(bb[tot][0], best);
            }
}

int d[128][128];
int tot[128];

int Solve()
{
    CLX(d, 0xFF);
    int n, s, p;
    cin >> n >> s >> p;
    FOR(i, n)
        cin >> tot[i];
    d[0][0] = 0;
    FOR(i, n)
    {
        FOR(j, i + 1)
            if (d[i][j] != -1)
            {
                FOR(z, 2)
                {
                    if (bb[tot[i]][z] != -1)
                        d[i + 1][j + z] = max(d[i + 1][j + z], d[i][j] + (int)(bb[tot[i]][z] >= p));
                }
            }
    }
    int res = d[n][s];
    ASS(res != -1);
    return res;
}

int main()
{
    Init();
    freopen("c:\\my\\in.txt", "r", stdin);
    freopen("c:\\my\\out.txt", "w", stdout);

    int t;
    cin >> t;
    FOR(i, t)
    {
        cout << "Case #" << (i + 1) << ": ";
        int res = Solve();
        cout << res << endl;
    }

    return 0;
}
