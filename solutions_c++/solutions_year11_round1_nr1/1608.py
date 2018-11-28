#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <cctype>
#include <ctime>
#include <cstdlib>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <cassert>

#define eps 1e-9
#define inf int(1e9)
#define inflong __int64(1e18)
#define abs(a) (((a) < 0) ? -(a) : (a))
#define sqr(a) ((a) * (a))
#define taskname "a"
#define sz(a) (int)a.size()
#define mp make_pair
#define pb push_back
#define forn(i, x, y) for (int i = (x); i <= (y); i++)
#define ford(i, y, x) for (int i = (y); i >= (x); i--)
                       
using namespace std;

const int maxn = int(2e5);
const int maxnn = int(2e3);
const double pi = M_PI;

typedef long long ll;
typedef long double ld;
typedef vector <int> vi;
typedef vector <vi> vii;
typedef vector <bool> vb;
typedef vector <vb> vbb;
typedef vector <ll> vl;
typedef vector <vl> vll;

int t, pd, pg;
ll n;

int gcd(int a, int b)
{
  while (b > 0)
  {
    int ta = a;
    a = b, b = ta % b;
  }
  return a;
}

int main()
{
  freopen(taskname".in", "r", stdin);
  freopen(taskname".out", "w", stdout);
  scanf("%d", &t);
  for (int i = 1; i <= t; i++)
  {
    scanf("%I64d %d %d", &n, &pd, &pg);
    printf("Case #%d: ", i);
   
    if (pd == 0 && pg == 0)
    {
      printf("Possible\n");
      continue;
    }
    if (pd * pg == 0)
    {
      if (pg == 0)
        printf("Broken\n");
      else
      {
        if (pg == 100)
          printf("Broken\n");
        else
          printf("Possible\n");
      }
     continue;      
    }
    int gcdd = gcd(100, pd);
    int mind = 100 / gcdd;
    
    gcdd = gcd(100, pg);
    int ming = 100 / gcdd;
    int tt = ming;
    while (ming < mind)
      ming += tt;
    
    if ((ll)mind <= n && (ming * pg) >= (pd * mind) && ming - mind >= (pg * ming - pd * mind) / 100)
      printf("Possible\n");
    else
      printf("Broken\n");
  }    
  return 0;
}


