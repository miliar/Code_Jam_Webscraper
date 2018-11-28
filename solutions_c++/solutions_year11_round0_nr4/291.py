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

int n, a[Maxn];

int calc()
{
    int ans = 0;

    for(int i=1; i<=n; i++)
        if( a[i] != i )
            ans++;

    return ans;
}
int main()
{
    int cas;
    ios::sync_with_stdio(0);
    freopen("D-large.in", "r", stdin);
    freopen("D-large.out", "w", stdout);

    cin>>cas;
    for(int cc=1; cc<=cas; cc++)
    {
        cin>>n;
        for(int i=1; i<=n; i++)
            cin>>a[i];
        printf("Case #%d: %.9lf\n", cc, 1.0*calc());
    }

    return 0;
}
