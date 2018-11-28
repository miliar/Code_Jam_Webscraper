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

int r[2000];

ll x[2000], y[2000];

bool isOK(ll xx, ll yy, int i)
{
    int j;
    fo(j,i)
        if ( hypot(x[j] - xx, y[j] - yy) < r[i] + r[j] )
            {
                return false;
            }
    return true;
}

int main(void)
{
    int t, tt, i, j, n, w, l;
    cin >> t;
    fo(tt, t)
        {
            cin >> n >> w >> l;
            fo(i,n) cin >> r[i];

            x[0] = y[0] = 0;

            for(i = 1; i < n; i++)
                {
                    bool ok = false;
                    ll xx, yy;
                    while(!ok)
                        {
                            xx = ((ll)rand() * rand()) % w;
                            yy = ((ll)rand() * rand()) % l;
                            ok = isOK(xx, yy, i);
                            if (ok == true)
                                {
                                    while(isOK(xx / 2, yy / 2, i))
                                        {
                                            xx = xx / 2;
                                            yy = yy / 2;
                                        }
                                }
                        }
                    x[i] = xx;
                    y[i] = yy;
                }
            
            cout << "Case #" << tt + 1 << ": ";
            fo(i,n) cout << x[i] << " " << y[i] << " ";
            cout << endl;            
        }
}
