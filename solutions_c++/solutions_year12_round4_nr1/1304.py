#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>

#define mp make_pair

using namespace std;

typedef long long ll;

ll n;
char dyn[10010][10010];
ll d[1<<14];
ll l[1<<14];
ll D;

bool rec(int cur, int from) {
    char& ret = dyn[cur][from];
    if (ret != -1) return ret;
    ll len = min(d[cur] - d[from], l[cur]);
    if (d[cur] + len >= D) return ret = 1;
    for(int i=cur+1; i<=n && d[cur]+len >= d[i]; ++i) {
        if (rec(i, cur)) return ret = 1;
    }
    return ret=0;
}

int main() {
    int i, j;
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int NT, T;
    cin>>NT;
    d[0] = 0;
    for(T=1; T<=NT; ++T) {
        cin>>n;
        for(i=1; i<=n; ++i) {
            cin>>d[i]>>l[i];
        }
        l[0] = d[1];
        cin>>D;
        memset(dyn, -1, sizeof(dyn));
        cout<<"Case #"<<T<<": "<<(rec(1, 0) ? "YES" : "NO")<<endl;
    }
    return 0;
}

