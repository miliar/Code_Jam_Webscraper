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

int t, n, l, rr;
int a[maxn];

int main()
{
  freopen(taskname".in", "r", stdin);
  freopen(taskname".out", "w", stdout);
  scanf("%d", &t);
  for (int i = 1; i <= t; i++)
  {
    printf("Case #%d: ", i);
    scanf("%d%d%d", &n, &l, &rr);
    for (int j = 0; j < n; j++)
      scanf("%d", &a[j]);
    bool out = false;
    for (int x = l; x <= rr; x++)
    {
      bool OK = true;
      for (int j = 0; j < n; j++)
      {
        if (x % a[j] != 0 && a[j] % x != 0)
        {
          OK = false;
          break;
        }
      }
      if (!OK)
        continue;  
      printf("%d\n", x);
      out = true;
      break;
    }
    if (!out)
      printf("NO\n");
  }                
  return 0;
}


