#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <ctime>

using namespace std;

#define fo(i, n) for(int i=0; i<(n); i++)
#define ff(i, n) for(int i=1; i<=(n); i++)
#define fxy(i, n, m) for(int i=(n); i<=(m); i++)
#define fyx(i, n, m) for(int i=(n); i>=(m); i--)
#define pb push_back
#define mp make_pair
#define pii pair<int, int>
#define sz(v) int((v).size())
#define all(v) v.begin(), v.end()
#define S(v) sort(v.begin(), v.end())

typedef long long ll;

inline ll sqr(ll x) { return x*x; }
inline ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
inline ll lcm(ll x, ll y) { return x/gcd(x, y)*y; }

const double eps = 1e-11;
const ll linf = 123456789066391630LL;
const int inf = 966391630;
const int md = 10007;
const int dx[]={-1, 0, 1, 0, -1, -1, 1, 1};
const int dy[]={0, 1, 0, -1, -1, 1, -1, 1};
const int max_ = 100001;

int i, j, k, l, res, tnow, tall, a[max_], n, m, r, x, y, d[101][101];
bool g[101][101];

int calc(int x, int y)
{
    if (x<1 || y<1 || g[x][y]) return 0;
    if (d[x][y]==-1) {
        d[x][y]=(calc(x-1, y-2)+calc(x-2, y-1))%md;
    }
       return d[x][y];
}

int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("D-small-attempt0.in", "r", stdin);
    //freopen("D-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
      scanf("%d\n", &tall);
    ff(tnow, tall) {
      scanf("%d%d%d", &n, &m, &r);
        memset(g, 0, sizeof(g));
      fo(i, r) {
           scanf("%d%d", &x, &y);
          g[x][y]=1;
      }
        fo(i, n+1) fo(j, m+1) d[i][j]=-1;
        ff(i, n) d[n][1]=0;
        ff(i, m) d[1][m]=0;
      d[1][1]=1^g[1][1];
         printf("Case #%d: %d\n", tnow, calc(n, m));
    }
       return 0;
}
 
