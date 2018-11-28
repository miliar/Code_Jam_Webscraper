#include <stdio.h>
#include <algorithm>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <math.h>
#include <queue>
#include <string.h>
#include <sstream>
#define mst(a,v) memset(a, v, sizeof(a))
#define msk(s,p) for(p=(s-1)&s;p=(p-1)&s)
#define _USE_MATH_DEFINES
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define mp make_pair
#define sz(x) ((int)x.size())
using namespace std;

typedef long long ll;

ll h[3000];
vector < int > prev[3000];

const ll hh = 1000000000;
ll mxh[3000];

bool fill(int st, int en)
{
    int i;
    if (st > en) return true;
    if (st == en)
        {
            return (sz(prev[en]) == 0);
        }
    if (!sz(prev[en])) return false;

    ll nh = h[en];    
    fo(i,sz(prev[en]))
        {
            int y = prev[en][i];
            if (y < st) return false;
            if (sz(prev[en]) == 1)
                nh = min(nh, mxh[y]);
            else
                nh = min(nh, mxh[y] - 1);
        }

    //cout << st << " " << en << " " << sz(prev[en]) << " " << nh << endl;
    
    int j = st;
    fo(i,sz(prev[en]))
       {
           int y = prev[en][i];
           //cout << y << " " << nh << endl;
           mxh[y] = h[y] = nh;
           
           double mn = ((double)(h[en] - h[y])) / (en - y);
           double val = h[y] - mn;
           int stp = st - 1;
           if (i > 0) stp = prev[en][i-1];
           for(j = y - 1; j > stp; j--)
               {
                   mxh[j] = min(mxh[j], (ll) (val - 3));
                   mxh[j] = min(mxh[j], nh-1);
                   //cout << en << " " << j << " " << 
                   val -= mn;
               }
           if (!fill(stp + 1, y))
               {
                   return false;
               }
       }
    return true;
}

int main(void)
{
    int t, tt, i, j, n, x;
    cin >> t;
    fo(tt, t)
        {
            cin >> n;
            fo(i,n) prev[i].clear();
            fo(i,(n-1))
                {
                    cin >> x;
                    prev[x-1].pb(i);
                }

            fo(i,n) mxh[i] = hh;
            h[n-1] = hh;
                                   
            cout << "Case #" << tt + 1 << ": ";
            bool pos = fill(0, n-1);
            if (!pos)
                {
                    cout << "Impossible" << endl;
                    continue;                    
                }
            fo(i,(n-1)) cout << h[i] << " ";
            cout << h[n-1] << endl;
        }
}
