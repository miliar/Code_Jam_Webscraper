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
#define pb push_back
#define mp make_pair
#define sz(v) int((v).size())
#define S(v) sort(v.begin(), v.end())

typedef vector<string> vs;
typedef vector<int> vi;
typedef long long ll;

inline ll sqr(ll x) { return x*x; }
inline ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
inline ll lcm(ll x, ll y) { return x/gcd(x, y)*y; }

const double eps = 1e-11;
const ll linf = 123456789066391630LL;
const int z = 1000001;
const int inf = 966391630;
const int md = 100000007;
const int dx[]={-1, 0, 1, 0, -1, -1, 1, 1};
const int dy[]={0, 1, 0, -1, -1, 1, -1, 1};

int i, j, k, l, n, m, sq, d, ntst, tall, res;
char c, r[1001];

int main()
{
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int dx, dy, p1, p2;
  bool g;
  double s1, s2, s3, so;
   scanf("%d\n", &tall);
  ff(ntst, tall) {
      scanf("%d%d%d", &n, &m, &sq);
     printf("Case #%d: ", ntst);
       g=0;
    if (n*m<sq) printf("IMPOSSIBLE\n"); else
      {
           so=(double)sq/2.0;
         for(dx=1; dx<=n; dx++)
           for(dy=1; dy<=m; dy++)
             for(p1=0; p1<=dx; p1++)
               for(p2=0; p2<=dy; p2++)
                if (!g) {
                   s1=(double)dy*(double)p1/2.0;
                   s2=(double)dx*(double)(dy-p2)/2.0;
                   s3=(double)p2*(double)(dx-p1)/2.0;
                 if (abs((double)dx*(double)dy-s1-s2-s3-so)<eps) {
                   printf("%d %d %d %d %d %d\n", p1, 0, dx, p2, 0, dy);
                     g=1;
                 }
               }
         if (!g) printf("IMPOSSIBLE\n");
      }
  }
      return 0;
} 
