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

int i, j, k, l, n, m, d, ln, ntst, tall, res=inf;
char c, r[1001], g[1001];
int w[10], p[10];

void gen(int np)
{
   if (np==k) {
       int i=0, j, ret=1;
      while (i<ln) {
        for(j=i; j<i+k; j++) g[j]=r[i+p[j-i]]; i+=k;
      }
        i=0; j=1;
    while (j<ln) {
      if (g[i]!=g[j]) { ret++; i=j; }
        j++;
    }
        res=min(res, ret);
   } else {
       fo(i, k)
         if (!w[i]) {
             w[i]=1; p[np]=i; gen(np+1); w[i]=0;
         }
   }
}

int main()
{
  freopen("D-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
   scanf("%d\n", &tall);
  ff(ntst, tall) {
       scanf("%d\n", &k); res=inf;
    gets(r); for(ln=0; r[ln]; ln++);
     memset(w, 0, sizeof(w)); gen(0);
     printf("Case #%d: %d\n", ntst, res);
  }
      return 0;
} 
