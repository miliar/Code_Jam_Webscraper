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
const int md = 100000007;
const int dx[]={-1, 0, 1, 0, -1, -1, 1, 1};
const int dy[]={0, 1, 0, -1, -1, 1, -1, 1};
const int max_ = 100001;

int i, j, k, l, n, m, res, tnow, tall, a[max_], h, p, b[101][101], d[101][1024], pl;
char c;

bool yes(int i, int j)
{
    return ((1<<i & j)>0);
}

bool ok(int i, int j)
{
  fo(l, m)
     if (!b[i][l] && yes(l, j)) return 0;
    return 1;
}

int hp(int j)
{
     int r=0;
    fo(l, m)
      r+=yes(l, j);
    return r;
}

bool cor(int y, int mo, int mn)
{
   ff(l, m-1)
     if (yes(l, mn)) {
        if (yes(l-1, mn)) return 0;
        if (yes(l-1, mo)) return 0;
     }
   fo(l, m-1)
     if (yes(l, mn)) {
        if (yes(l+1, mn)) return 0;
        if (yes(l+1, mo)) return 0;
     }
     return 1;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    freopen("C-small-attempt0.in", "r", stdin);
    //freopen("C-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
      scanf("%d\n", &tall);
    ff(tnow, tall) {
         scanf("%d%d\n", &n, &m);
       fo(j, m) b[0][j]=0;
       ff(i, n) {
         fo(j, m) {
              scanf("%c", &c); b[i][j]=(c=='.');
         }
           scanf("\n");
       }
          h=1<<m; 
             memset(d, 0, sizeof(d));
       fo(i, h) d[0][i]=0;
       ff(i, n)
         fo(mn, h)
           if (ok(i, mn))
             fo(mo, h)
               if (cor(i, mo, mn)) {
                     pl=hp(mn);
                   d[i][mn]=max(d[i][mn], pl+d[i-1][mo]);  
               }
       res=0;
        fo(l, h) res=max(res, d[n][l]);
         printf("Case #%d: %d\n", tnow, res);
    }
       return 0;
}
 
