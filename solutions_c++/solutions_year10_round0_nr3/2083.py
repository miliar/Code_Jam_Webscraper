#include <cstdio>
#include <cstring>
#include <vector>
#include <iostream>
using namespace std;

const int maxn = 1010;
int n, r, k;
long long g[maxn];
vector<long long> p;  
long long ans;

void work()
{
    int i, j, tmp, head, tail, shead, stail;
    p.clear();
    shead = stail = 0;
    long long now = g[0];
    while (stail < n - 1 && now + g[stail + 1] <= k)
    { now += g[++stail]; }
    p.push_back(now);
    head = (stail + 1) % n; tail = head;
    bool found = false; 
    for (i = 1; i < r; ++i)
    {
        now = g[head];
        tmp = (tail + 1) % n;
        while (head != tmp && now + g[tmp] <= k)
        {
            now += g[tmp];
            tmp = (tmp + 1) % n;
        }
        if (now + g[tmp] > k || head == tmp)
        { tail = ((tmp - 1) % n + n) % n; }
        else tail = tmp;
        if (head == shead && stail == tail)
            break;
        else p.push_back(now);
        head = (tail + 1) % n; tail = head;
    }
    int m = p.size();
    ans = 0;
    for (int i = 0; i < m; ++i) ans += p[i];
    ans *= (r / m);
    for (int i = 0; i < r % m; ++i) ans += p[i];
  //  cout << m << endl;
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d%d%d", &r, &k, &n);
        for (int i = 0; i < n; ++i) cin >> g[i];
       /// for (int i = 0; i < n; ++i) cout << g[i] << ' '; cout << endl;
        work();
        cout << "Case #" << t << ": " << ans << endl;
    }
    return 0;
}
