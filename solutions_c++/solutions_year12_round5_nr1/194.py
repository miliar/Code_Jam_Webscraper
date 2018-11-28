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

int main(void)
{
    int t, tt, i, j, n;
    cin >> t;
    int a[10000], p[10000];
    vector < pair < int , int > > v;
    fo(tt, t)
        {
            v.clear();
            cin >> n;
            fo(i,n)
                {
                    cin >> a[i];
                }
            fo(i,n)
                {
                    cin >> p[i];
                    v.pb( mp( - p[i], i));
                }
            sort(all(v));
            cout << "Case #" << tt + 1 << ": ";
            fo(i,n) cout << v[i].second << " ";
            cout << endl;
        }
}
