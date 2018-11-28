#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <complex>
#include <numeric>
#include <tuple>

#define INF 1023456789
#define SQR(x) ((x)*(x))
#define INIT(x,y) memset((x),(y),sizeof((x)))
#define SIZE(x) ((int)((x).size()))
#define REP(i, n) for (__typeof(n) i=0;i<(n);++i)
#define FOR(i, a, b) for (__typeof(a) i=(a);i<=(b);++i)
#define FORD(i, a, b) for (__typeof(a) i=(a);i>=(b);--i)
#define FORE(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

#define DEBUG
#ifdef DEBUG
#define DBG(x) cerr << #x << ": " << (x) << endl;
#else
#define DBG(x)
#endif

using namespace std;
 
typedef long long LL;
typedef pair<int,int> PI;
typedef tuple<int,int,int>trio;

int X,O,T;
char a[10][10];

inline void init()
{
        X=O=T=0;
}

inline void add(int r,int c)
{
        if (a[r][c]=='O') O++;
        else if (a[r][c]=='X') X++;
        else if (a[r][c]=='T') T++;
}

inline bool answer(int t)
{
        t++;
        if (X+T==4) 
        {
                printf("Case #%d: X won\n",t);
                return true;
        }
        if (O+T==4) 
        {
                printf("Case #%d: O won\n",t);
                return true;
        }
        return false;
}

int main()
{
        int T;
        scanf("%d",&T);
        REP(i,T)
        {
                REP(j,4) scanf("%s",a[j]);
                bool found=false;
                REP(r,4) 
                {
                        init();
                        REP(c,4) add(r,c);
                        if (answer(i)) {found=true;break;}
                }
                if (found) continue;
                REP(c,4)
                {
                        init();
                        REP(r,4) add(r,c);
                        if (answer(i)) {found=true;break;}
                }
                if (found) continue;
                init();
                REP(j,4) add(j,j);
                if (answer(i)) continue;
                init();
                REP(j,4) add(j,3-j);
                if (answer(i)) continue;
                REP(r,4) REP(c,4) if (!found && a[r][c]=='.')
                {
                        printf("Case #%d: Game has not completed\n",i+1);
                        found=true;
                }
                if (!found) printf("Case #%d: Draw\n",i+1);
        }
        return 0;
}
