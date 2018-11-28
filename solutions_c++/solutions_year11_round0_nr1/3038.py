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

int go()
{
    int N;
    string robot;
    int p;

    cin >> N;

    int t = 0;
    int ot = 0, op = 1;
    int bt = 0, bp = 1;
    forz(N)
    {
        cin >> robot >> p;
        if (robot == "O")
        {
            int mt = ot + abs(op - p);
            int nt = max(mt, t);
            ot = t = nt + 1;
            op = p;
        }
        else
        {
            assert(robot == "B");
            int mt = bt + abs(bp - p);
            int nt = max(mt, t);
            bt = t = nt + 1;
            bp = p;
        }
        PRINT("Pressed (%s, %d) at time %d.\n", robot.c_str(), p, t);
    }
    return t;
}

int main()
{
    ios::sync_with_stdio(false);
    int T;
    cin >> T;
    forz(T)
        cout << "Case #" << i+1 << ": " << go() << '\n';
    return 0;
}
