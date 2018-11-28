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

int i, j, k, l, n, m, d, ntst, tall, res, g[z], c[z], leaf[z], v;

int calc(int node, int vol)
{
      int r=inf, q, p;
    if (node<=n) {
       if (g[node]) {
           if (vol) {
              q=calc(2*node, 1); p=calc(2*node+1, 1); if (q!=-1 && p!=-1) r=q+p;
            if (c[node]) {
              q=calc(2*node, 0); p=calc(2*node+1, 1); if (q!=-1 && p!=-1) r=min(r, 1+p+q);
              q=calc(2*node, 1); p=calc(2*node+1, 0); if (q!=-1 && p!=-1) r=min(r, 1+p+q);
            }
           } else {
              q=calc(2*node, 1); p=calc(2*node+1, 0); if (q!=-1 && p!=-1) r=q+p;
              q=calc(2*node, 0); p=calc(2*node+1, 1); if (q!=-1 && p!=-1) r=min(r, p+q);
              q=calc(2*node, 0); p=calc(2*node+1, 0); if (q!=-1 && p!=-1) r=min(r, p+q);
           }
         if (r==inf) r=-1;
              return r;
       } else {
           if (vol) {
               q=calc(2*node, 1); p=calc(2*node+1, 1); if (q!=-1 && p!=-1) r=min(r, p+q);
               q=calc(2*node, 0); p=calc(2*node+1, 1); if (q!=-1 && p!=-1) r=min(r, p+q);
               q=calc(2*node, 1); p=calc(2*node+1, 0); if (q!=-1 && p!=-1) r=min(r, p+q);
           } else {
               q=calc(2*node, 0); p=calc(2*node+1, 0); if (q!=-1 && p!=-1) r=min(r, p+q);
             if (c[node]) {
               q=calc(2*node, 0); p=calc(2*node+1, 1); if (q!=-1 && p!=-1) r=min(r, 1+p+q);
               q=calc(2*node, 1); p=calc(2*node+1, 0); if (q!=-1 && p!=-1) r=min(r, 1+p+q);
             }
           }
         if (r==inf) r=-1;
             return r;
       }
    } else {
        if (vol==leaf[node]) return 0; else return -1;
    }
}

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("output.txt", "w", stdout);
   scanf("%d\n", &tall);
  ff(ntst, tall) {
      scanf("%d%d", &m, &v); n=(m-1)/2;
    ff(i, n) scanf("%d%d", &g[i], &c[i]);
    ff(i, (m+1)/2) scanf("%d", &leaf[n+i]);
     res=calc(1, v);
       printf("Case #%d: ", ntst);
     if (res==-1) printf("IMPOSSIBLE\n"); else printf("%d\n", res);  
  }
      return 0;
}
