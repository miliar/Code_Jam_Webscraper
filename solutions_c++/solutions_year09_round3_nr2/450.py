#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define sz size()
#define PB push_back
#define clr(x) memset(x, 0, sizeof(x))
#define forn(i,n) for(__typeof(n) i = 0; i < (n); i++)
#define ford(i,n) for(int i = (n) - 1; i >= 0; i--)
#define forv(i,v) forn(i, v.sz)
#define For(i, st, en) for(__typeof(en) i = (st); i < (en); i++)

using namespace std;
typedef long long ll;

int main()
{
	int cases = 0;
    scanf("%d\n", &cases);
    forn(n, cases)
    {
        int fly = 0;
        scanf("%d\n", &fly);
        double x = 0.0, y = 0.0, z = 0.0, u = 0.0, v = 0.0, w = 0.0;
        forn(i, fly)
        {
           int px, py, pz, vx, vy, vz;
           scanf("%d %d %d %d %d %d\n", &px, &py, &pz, &vx, &vy, &vz);
           x += px;
           y += py;
           z += pz;
           u += vx;
           v += vy;
           w += vz;
        }
        x /= fly;
        y /= fly;
        z /= fly;
        u /= fly;
        v /= fly;
        w /= fly;
        double dmin = 0.0, tmin = 0.0;
        if(u == 0.0 && v == 0.0 && w == 0.0)
            tmin = 0.0;
        else
        {
            tmin = -(x*u+y*v+z*w) / (u*u+v*v+w*w);
            if(tmin < 0)
                tmin = 0.0;
        }
        double minx, miny, minz;
        minx = x + tmin*u;
        miny = y + tmin*v;
        minz = z + tmin*w;
        dmin = pow(minx*minx+miny*miny+minz*minz, 0.5);

        printf("Case #%d: %.12lf %.12lf\n", n+1, dmin, tmin);
    }
	return 0;
}
