#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <vector>
#include <set>
#include <algorithm>

#define maxn 10010
#define Fup(i, s, t) for (int i = s; i <= t; i ++)
#define Fdn(i, s, t) for (int i = s; i >= t; i --)
#define Path(i, s) for (int i = s; i; i = d[i].next)

using namespace std;

int d[maxn], l[maxn], q[maxn], f[maxn];
bool ins[maxn];
int n, D;

void init()
{
    cin >> n;
    Fup(i, 1, n)
        cin >> d[i] >> l[i];
    cin >> D;
    d[++ n] = D;
}

void solve()
{
    memset(f, -1, sizeof(f));
    f[1] = d[1];
    int head = 0, tail = 1;
    q[0] = 1;
    ins[1] = true;
    while (head != tail){
        int u = q[head];
        Fup(i, 1, n)
            if (abs(d[i] - d[u]) <= f[u])
                if (f[i] < min(abs(d[i] - d[u]), l[i])){
                    f[i] = min(abs(d[i] - d[u]), l[i]);
                    if (!ins[i]){
                        ins[i] = true;
                        q[tail] = i;
                        tail ++;
                        if (tail > n)
                            tail = 0;
                    }
                }
        ins[u] = false;
        head ++;
        if (head > n)
            head = 0;
    }
    if (f[n] >= 0)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
}

int main()
{
//    freopen("temp.in", "r", stdin);
//    freopen("temp.out", "w", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    Fup(i, 1, t){
        cout << "Case #" << i << ": ";
        init();
        solve();
    }
    return 0;
}
