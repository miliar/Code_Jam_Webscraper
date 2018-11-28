#include <cstdio>
#include <cstring>
#include <string>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <vector>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#define MAXN (1 << 10)
#define INF
#define EPS (1e-10)
#define x first
#define y second
using namespace std;
#warning use cin/cout or %I64d for long integers

typedef long double dbl;

dbl len, walk, run, t;
int n;
int from[MAXN], to[MAXN];
dbl add[MAXN];

int used[MAXN];

inline void solve()
{
    dbl walkLen = len;

    for (int i=0; i < n; ++i)
        walkLen -= to[i]-from[i];

    memset(used, 0, sizeof(used));

    dbl leftLen = len;
    dbl leftTime = t;
    dbl sol = 0;

    if (leftTime > EPS)
    {
        dbl S = leftTime*run;
        if (S+EPS > walkLen) // we run untill the end
        {
            dbl tm = walkLen/run;
            sol += tm;
            leftTime -= tm;
        }
        else
        {   // we run as much as we can...
            sol += leftTime;
            walkLen -= leftTime*run;
            leftTime = -EPS;
            // ..and then we walk till the end
            double tm = walkLen/walk;
            sol += tm;
        }
    }
    else
    {// we walk till the end
        double tm = walkLen/walk;
        sol += tm;
    }

    for (int i=0; i < n; ++i)
        if (leftTime > EPS)
        {
            //cout << leftTime << endl;
            int idx = -1;
            for (int j=0; j < n; ++j)
                if (!used[j])
                {
                    if (idx == -1 || add[idx] > add[j]+EPS)
                        idx = j;
                }
            if (idx == -1) break;
            used[idx] = 1;
            //cout << "found " << idx << endl;

            dbl vel = add[idx] + run;
            dbl tm = leftTime;

            dbl S = vel*tm;
            dbl s = to[idx]-from[idx];
            if (S < s+EPS)
            {
                s -= S;
                leftTime -= tm;

                sol += tm;
                sol += s / (walk + add[idx]);
                break;
            }
            else
            {
                tm = s / vel;
                leftTime -= tm;
                sol += tm;
            }
        }
        else break;

        for (int i=0; i < n; ++i)
            if (!used[i])
            {
                dbl vel = walk + add[i];
                dbl s = to[i]-from[i];

                sol += s/vel;
            }

        cout << setprecision(10) << fixed << sol << endl;
}

inline void read()
{
    cin >> len >> walk >> run >> t >> n;

    for (int i=0; i < n; ++i)
        cin >> from[i] >> to[i] >> add[i];
}

int main()
{
    int brt, testNo = 0;

    scanf("%d", &brt);
    while (brt--)
    {
        read();
        printf("Case #%d: ", ++testNo);
        solve();
    }

    return 0;
}
