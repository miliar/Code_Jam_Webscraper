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

ll a[100000];

int main(void)
{
    int t, tt, i, j, n, m;
    cin >> t;
    fo(tt, t)
        {
            vector < pair < ll, ll > > v;
            v.clear();
            cin >> n;
            fo(i,n)
                {
                    int dd, ll;
                    cin >> dd >> ll;
                    v.pb( mp(dd, ll) );
                }
            cin >> m;
            sort(all(v));
            
            int j = 1;
            bool pos = false;
            memset(a, -1, sizeof(a));
            a[0] = 0;
            fo(i,n)
                {
                    if (a[i] == -1)
                        break;
                    ll dist = v[i].first + min(v[i].second, v[i].first - a[i]);
                    while(j < n && dist >= v[j].first)
                        {
                            a[j] = v[i].first;
                            j++;
                        }
                    if (dist >= m)
                        {
                            pos = true;
                            break;
                        }
                }

            cout << "Case #" << tt + 1 << ": ";
            if (pos) cout << "YES" << endl;
            else cout << "NO" << endl;
        }
}
