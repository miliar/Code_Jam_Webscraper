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

const int Maxn = 1000000+10;
const int INF = 0x7f7f7f7f;
const double eps = 1e-10;
const double pi = acos(-1.0);
inline int realcmp(double a, double b){ return (a>b+eps) ? 1 : ((a+eps<b)?-1:0); }

struct Item
{
    int u, v, sp;
    Item() {}
    Item(int a, int b, int c): u(a), v(b), sp(c) {}
    bool operator < (const Item &t) const
    {
        if( sp == t.sp )
            return u < t.u;
        return sp < t.sp;
    }
};

int a[Maxn];

int main()
{
    double t;
    int cas, L, S, R, n, u, v, w, p;
    ios::sync_with_stdio(0);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    cin>>cas;
    for(int c=1; c<=cas; c++)
    {
        cin>>L>>S>>R>>t>>n;
        for(int i=0; i<L; i++)
            a[i] = 0;
        for(int i=0; i<n; i++)
        {
            cin>>u>>v>>w;
            for(int j=u; j<v; j++)
                a[j] = w;
        }

        p=0;  v=a[0];
        vector<Item> vt;
        for(int i=1; i<=L; i++)
        {
            if( a[i] == v )
                continue;
            else
            {
                vt.push_back(Item(p, i, v));
                v = a[i];
                p = i;
            }
        }
        //if( p != L )
            vt.push_back(Item(p, L, a[L]));

        double ans=0;
        sort(vt.begin(), vt.end());
        for(int i=0; i<sz(vt); i++)
        {
            //cout<<vt[i].u<<vt[i].v<<vt[i].sp<<endl;
            if( realcmp(t, 0) == 1 )
            {
                if( t*(vt[i].sp+R) < 1.0*vt[i].v-vt[i].u )
                {
                    ans += (1.0*vt[i].v-vt[i].u-t*(vt[i].sp+R))/(vt[i].sp+S);
                }
                double tmp=min(t*(vt[i].sp+R), 1.0*vt[i].v-vt[i].u);
                ans += tmp/(vt[i].sp+R);
                t -= tmp/(vt[i].sp+R);
            }
            else
            {
                ans += 1.0*(vt[i].v-vt[i].u)/(vt[i].sp+S);
            }
        }
        printf("Case #%d: %.9lf\n", c, ans);
    }

    return 0;
}
