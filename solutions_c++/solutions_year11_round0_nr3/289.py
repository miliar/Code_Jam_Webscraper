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

int a[Maxn];

int main()
{
    int cas, n, sum, xxx;
    ios::sync_with_stdio(0);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    cin>>cas;
    for(int c=1; c<=cas; c++)
    {
        cin>>n;
        xxx = sum = 0;
        for(int i=0; i<n; i++)
        {
            cin>>a[i];
            sum += a[i];
            xxx ^= a[i];
        }
        if( xxx != 0 )
            printf("Case #%d: NO\n", c);
        else
        {
            sort(a, a+n);
            printf("Case #%d: %d\n", c, sum-a[0]);
        }
    }

    return 0;
}
