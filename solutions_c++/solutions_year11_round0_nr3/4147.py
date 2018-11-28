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
#define fo(i,n) for(i=0;i<n;i++)
#define all(x) x.begin(),x.end()
#define pb push_back
#define mp make_pair
#define sz(x) x.size()
using namespace std;

typedef long long ll;

int main(void)
{
    int i, n, m, t, a;
    freopen("c.in", "r", stdin);freopen("c.out", "w", stdout);
    cin >> m;
    fo(t,m)
        {
            cin >> n;
            int x = 0, minA = 1000001;
            ll s = 0;
            fo(i,n)
                {
                    cin >> a;
                    x ^= a;
                    s += a;
                    minA = min(a, minA);
                }
            cout << "Case #" << t+1 << ": ";
            if (!x)
                {
                    cout << s - minA << endl;
                }
            else
                cout << "NO" << endl;
        }
}
