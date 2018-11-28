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

#define TRACE(x...) x
#define PRINT(x...) TRACE(printf(x))
#define WATCH(x) TRACE(cout << #x" = " << x << '\n')

#define forz(p)     for(int i = 0; i < p; ++i)
#define foriz(i, p) for(int i = 0; i < p; ++i)
#define tr(x)       for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define read(n)     (scanf("%d", &(n)) == 1)

#define PRINT_PAIR(p) TRACE(cout << "(" << p.first <<", " << p.second << ")" << endl)

const int INF = 0x3f3f3f3f;
const double EPS = 1e-7;

int blades[512][512];

inline int cmpD(double x, double y, double tol = EPS)
{
    return (x <= y + tol) ? (x + tol < y) ?  -1 : 0 : 1;
}

bool can(int r1, int c1, int r2, int c2)
{
    //PRINT("CAN(%d, %d, %d, %d)\n", r1, c1, r2, c2);
    pair<double, double> center = make_pair((r1+r2), (c1+c2));
    double rmass = 0.0;
    double cmass = 0.0;
    int tcells = 0;
    int tmass = 0.0;
    for(int r = r1; r <= r2; ++r)
    {
        for(int c = c1; c <= c2; ++c)
        {
            if ((r == r1 and (c == c1 or c == c2))
                or
                (r == r2 and (c == c1 or c == c2)))
                continue;
            rmass += 2*r*blades[r][c];
            cmass += 2*c*blades[r][c];
            tmass += blades[r][c];
            tcells++;
        }
    }
    pair<double, double> mass_center = make_pair(rmass*1.0/tmass, cmass*1.0/tmass);
    //PRINT_PAIR(center);
    //PRINT_PAIR(mass_center);

    return (!cmpD(center.first, mass_center.first)) and (!cmpD(center.second, mass_center.second));
}

void go()
{
    int R, C, D;
    scanf("%d %d %d\n", &R, &C, &D);
    memset(blades, 0, sizeof(blades));
    for(int r = 1; r <= R; ++r)
    {
        for(int c = 1; c <= C; ++c)
        {
            blades[r][c] = int(getchar() - '0') + D;;
        }
        getchar();
    }

    int K = -1;

    for(int r1 = 1; r1 <= R; ++r1) for(int c1 = 1; c1 <= C; ++c1)
    for(int diff = 2; (r1+diff <= R) && (c1+diff <= C); ++diff)
    {
        int r2 = r1 + diff;
        int c2 = c1 + diff;
        if (can(r1, c1, r2, c2))
        {
            K = max(K, diff+1);
        }
    }

    if (K < 3)
    {
        puts("IMPOSSIBLE");
    }
    else
    {
        printf("%d\n", K);
    }

}

int main()
{
    int T;
    read(T);
    forz(T)
    {
        printf("Case #%d: ", i+1);
        go();
    }
    return 0;
}
