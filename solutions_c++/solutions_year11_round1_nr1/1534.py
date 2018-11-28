#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG

#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif

#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)

bool solve(int n, int pd, int pg)
{
    if(pd < 100 and pg == 100) return false;
    if(pd > 0 and pg == 0) return false;
    FORN(d, 1, n + 1){
        int wd = d * pd;
        if(wd % 100 == 0){
            return true;
        }
    }

    return false;
}

int main()
{
    int NTC;
    scanf("%d", &NTC);
    FORN(TC, 0, NTC){
        int n, pd, pg;
        scanf("%d %d %d", &n, &pd, &pg);
        printf("Case #%d: %s\n", TC + 1, solve(n, pd, pg) ? "Possible" : "Broken");
    }
    
}
