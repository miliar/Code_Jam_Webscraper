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

bool used[Maxn];
int d[Maxn], l[Maxn];

int main()
{
    int cas, n, m;
    ios::sync_with_stdio(0);
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);

    cin>>cas;
    for(int c=1; c<=cas; c++)
    {
        cin>>n;
        for(int i=1; i<=n; i++)
            cin>>d[i]>>l[i];
        cin>>m;

        int ans = 0;
        queue<Item> que;
        que.push(Item(0, 1));
        while( !que.empty() )
        {
            Item t = que.front();
            que.pop();
            int maxn = d[t.second]+min(l[t.second], d[t.second]-d[t.first]);
            ans = max(ans, maxn);
            if( ans >= m )
                break;
            for(int i=t.second+1; i<=n; i++)
                if( maxn >= d[i] )
                    que.push(Item(t.second, i));
        }
        printf("Case #%d: ", c);
        if( ans >= m )
            printf("YES\n");
        else
            printf("NO\n");
    }

    return 0;
}
