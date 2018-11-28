#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <complex>

using namespace std;

typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;

const int N_MAX = 10;
const int ITER = 5;
int n;
int x[N_MAX], y[N_MAX];
LL r[N_MAX];
int w, l;
bool ok;

int rnd()
{
    return (rand() << 15) | rand();
}

void rec(int i)
{
    if (i == n)
    {
        ok = true;
    }
    else
    {
        for (int it = 0; it < ITER; ++it)
        {
            int cx = rnd() % w, cy = rnd() % l;

            bool cur = true;
            for (int j = 0; j < i; ++j)
                if (r[i] * r[i] + 2 * r[i] * r[j] + r[j] * r[j] > LL(cx - x[j]) * (cx - x[j]) + LL(cy - y[j]) * (cy - y[j]))
                {
                    cur = false;
                    break;
                }
            if (cur)
            {
                x[i] = cx; y[i] = cy;
                rec(i + 1);
                if (ok) return;
            }
        }
    }
}

int main()
{
    int nTests;
    cin >> nTests;

    for (int test = 1; test <= nTests; ++test)
    {
        cin >> n >> w >> l;
        w++, l++;

        for (int i = 0; i < n; ++i)
            cin >> r[i];

        ok = false;
        while (!ok)
        {
            //random_shuffle(r, r + n);
            rec(0);
        }
        cout << "Case #" << test << ":";
        for (int i = 0; i < n; ++i) cout << ' ' << x[i] << ' ' << y[i];
        cout << '\n';
    }
    return 0;
}
