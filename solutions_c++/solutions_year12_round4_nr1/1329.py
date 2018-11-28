#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <deque>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
using namespace std;

#define MAX 10000

typedef pair<int,int> pii;
#define d first
#define l second

int n;
pii v[MAX+3];
int U;

bool dp[MAX+3][MAX+3];
bool vis[MAX+3][MAX+3];
bool sol(int i, int j) // on i, from j
{
    if (j>=0 && vis[i][j]) return dp[i][j];
    int di = v[i].d, dj = j==-1?0:v[j].d;
    int D = min(v[i].l, di-dj);
    bool ok = (U-v[i].d<=D);
    for (int k=i+1; !ok && k<n && v[k].d-v[i].d<=D; ++k) ok = sol(k,i);
    if (j>=0) vis[i][j] = true, dp[i][j] = ok;
    return ok;
}

int main()
{
    //freopen("in.txt", "rt", stdin);
    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A-small-attempt0.out", "wt", stdout);
    int T;
    cin>>T;
    for (int cas=1; cas<=T; ++cas)
    {
        memset(vis, false, sizeof vis);
        cin>>n;
        for (int i=0; i<n; ++i) cin>>v[i].d>>v[i].l;
        cin>>U;
        sort(v, v+n);
        bool ok = sol(0, -1);
        if (ok) printf("Case #%d: YES\n", cas);
        else printf("Case #%d: NO\n", cas);
    }
    return 0;
}
