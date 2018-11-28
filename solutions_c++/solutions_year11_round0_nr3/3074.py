#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

#define TRACE(x...) 
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << '\n')

#define forz(p)     for(int i = 0; i < p; ++i)
#define foriz(i, p) for(int i = 0; i < p; ++i)
#define tr(x)       for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define read(n)     (scanf("%d", &(n)) == 1)

const int INF = 0x3f3f3f3f;
const double EPS = 1e-9;

inline int cmpD(double x, double y, double tol = EPS)
{
    return (x <= y + tol) ? (x + tol < y) ?  -1 : 0 : 1;
}

int blah[32];

string go(int n)
{
    forz(n) cin >> blah[i];

    int best = -1;
    foriz(mask, 1 << n)
    {
        int psum = 0, pxor = 0, bxor = 0;
        int p = 0, b = 0;
        forz(n)
        {
            if (mask & (1 << i))
            {
                psum += blah[i];
                bxor = bxor xor blah[i];
                b++;
            }
            else
            {
                pxor = pxor xor blah[i];
                p++;
            }
        }
        if ((pxor == bxor) && (p && b))
        {
            WATCH(psum);
            WATCH(p);
            WATCH(b);
            best = max(best, psum);
        }
    }

    if (best >= 0)
    {
        stringstream ss;
        ss << best;
        return ss.str();
    }
    return "NO";
}

int main()
{
    ios::sync_with_stdio(false);

    int T, N;
    cin >> T;
    forz(T)
    {
        cin >> N;
        cout << "Case #" << i+1 << ": " << go(N) << '\n';
    }
    return 0;
}
