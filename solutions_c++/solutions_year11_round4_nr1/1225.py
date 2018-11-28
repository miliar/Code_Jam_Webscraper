#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iostream>
#include <sstream>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <cstring>
#include <utility>
#include <cctype>
#include <vector>
#include <string>
#include <bitset>
#include <cmath>
#include <queue>
#include <stdio.h>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
#define REP(i,n) for(int i=0;i<n;i++)
#define TR(i,x) for(typeof(x.begin()) i=x.begin();i!=x.end();i++)
#define ALL(x) x.begin(),x.end()
#define SORT(x) sort(ALL(x))
#define CLEAR(x) memset(x,0,sizeof(x))
#define FILL(x,c) memset(x,c,sizeof(x))

using namespace std;

const double eps = 1e-8;

#define PB push_back
#define MP make_pair

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<long double> VD;
typedef pair<int,int> PII;
typedef long long LL;
typedef unsigned long long ULL;

map<int,int> in;
double F[10023];
int R[10023],S[10023];
bool V[10023];

struct xx
{
    double b,e,d;
    bool operator < (const xx &p) const
    {
        return d < p.d;
    }
} a[10023];

int main()
{
    int T;
    cin >> T;
    for (int cs = 0;cs < T;++cs)
    {
        int n,x,s,r,t;
        cin >>x >> s >> r >> t >> n;
        double mi,mx;
        mx = 0;
        if (r < s) r = s;
        for (int i = 0;i < n;++i)
        {
            cin >> a[i].b >> a[i].e >> a[i].d;
            mx += a[i].e - a[i].b;
        }
        sort(a,a+n);
        double ans = 0,tot = n,ss = s,rr = r,rest = t;
        mx = x - mx;
        if (rest > 0)
        {
            if (rest * rr >= mx)
            {
                ans += mx/rr;
                rest -= mx/rr;
            }
            else
            {
                ans += rest;
                ans += (mx - rest*rr)/ss;
                rest = 0;
            }
        }
        else
            ans += mx/ss;
        for (int i = 0;i < n;++i)
        {
            if (rest > 1e-8)
            {
                if ((a[i].e - a[i].b)/(rr + a[i].d) - rest < -(1e-8))
                {
                    ans += (a[i].e - a[i].b)/(rr + a[i].d);
                    rest -= (a[i].e - a[i].b)/(rr + a[i].d);
                } else
                {
                    ans += rest;
                    ans += (a[i].e - a[i].b - rest * (rr + a[i].d))/(ss + a[i].d);
                    rest = 0;
                }
            }
            else
                ans += (a[i].e - a[i].b)/(ss + a[i].d);
        }
        memset(S,0,sizeof(S));
        cout << "Case #" << cs+1 << ": ";
        printf("%.8f\n",ans);
    }
    return 0;

}
