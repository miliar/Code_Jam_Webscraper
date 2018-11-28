#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <memory>
#include <vector>
#include <string>
#include <bitset>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cmath>
#define sz(a) ((int)(a).size())
#define foreach(i, v) for(__typeof((v).begin()) i=(v).begin(); i!=(v).end(); i++)
using namespace std;
typedef long long llong;
typedef pair<int, int> Item;

const int Maxn = 1000+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int realcmp(double a, double b){ return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

int main()
{
    llong n;
    int cas, pd, pg;
    ios::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin>>cas;
    for(int c=1; c<=cas; c++)
    {
        bool flags=false;
        cin>>n>>pd>>pg;
        if( n > 300 )
        {
            if( pg==100 && pd==100 )
                flags = true;
            else if( pg==0 && pd==0 )
                flags = true;
            else if( pg<100 && pg>0 )
                flags = true;
        }
        else
        {
            for(int d=1; d<=n; d++)
                if( pd*d%100 == 0 )
                {
                    if( pg==100 && pd==100 )
                        flags = true;
                    else if( pg==0 && pd==0 )
                        flags = true;
                    else if( pg<100 && pg>0 )
                        flags = true;
                }
        }
        if( flags )
            printf("Case #%d: Possible\n", c);
        else
            printf("Case #%d: Broken\n", c);
    }

    return 0;
}
